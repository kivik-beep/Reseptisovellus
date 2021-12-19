from db import db

def add_recipe(name, user_id, serves, instructions, active, passive):
    if active == "":
        active = 0
    if passive == "":
        passive = 0
    sql = """INSERT INTO recipe (name, user_id, instructions, serves, active, passive)
            VALUES (:name, :user_id, :instructions, :serves, :active, :passive) RETURNING id"""
    recipe_id = db.session.execute(sql, {"name":name, "user_id":user_id,
                                         "instructions":instructions, "serves":serves,
                                         "active": float(active), "passive":float(passive)}).fetchone()[0]
    return recipe_id

def get_all():
    sql = "SELECT id, name FROM recipe ORDER BY id DESC"
    return db.session.execute(sql).fetchall()

def count_receipts():
    sql = "SELECT COUNT(*) FROM recipe"
    return db.session.execute(sql).fetchone()[0]

def get_receipt(r_id):
    sql = "SELECT * FROM recipe WHERE id=:id"
    result = db.session.execute(sql, {"id": r_id}).fetchall()
    data = result[0]
    return data

def is_id_taken(r_id):
    sql = "SELECT id FROM recipe WHERE id=:id"
    result = db.session.execute(sql, {"id": r_id}).fetchall()
    return bool(result)

def is_name_taken(r_name):
    sql = "SELECT id FROM recipe WHERE name=:name"
    result = db.session.execute(sql, {"name": r_name}).fetchall()
    return bool(result)

def get_name(r_id):
    sql = "SELECT name FROM recipe WHERE id=:id"
    return db.session.execute(sql, {"id": r_id}).fetchone()[0]

# different recipe sortings
def get_all_containing(incredient_id):
    sql = """SELECT r.id, r.name FROM recipe as r, incredients as i
            WHERE i.recipe_id=r.id AND i.incredient_id=:incredient_id"""
    return db.session.execute(sql, {"incredient_id":incredient_id}).fetchall()

def all_with_tag(tag_name):
    sql = """SELECT r.id, r.name FROM recipe as r, tag as t
            WHERE t.recipe_id=r.id AND t.name=:tag_name"""
    return db.session.execute(sql, {"tag_name":tag_name}).fetchall()


# different recipe orders
def all_order_by_favorite():
    sql = """SELECT r.id, r.name FROM recipe as r LEFT JOIN favorites as f
    ON r.id = f.recipe_id GROUP BY r.id ORDER BY COUNT(f.recipe_id)"""
    return db.session.execute(sql).fetchall()

def all_order_by_inc_quantity():
    sql = """SELECT r.id, r.name FROM recipe as r, incredients as I
            WHERE r.id = I.recipe_id GROUP BY r.id ORDER BY COUNT(i.recipe_id)"""
    return db.session.execute(sql).fetchall()

def all_order_by_time():
    sql = "SELECT id, name FROM recipe ORDER BY (active + passive)"
    return db.session.execute(sql).fetchall()


# change recipt info
def chage_name(new_name, recipe_id):
    taken = is_name_taken(new_name)
    if not taken:
        sql = "UPDATE recipe SET name=:new_name WHERE id=:recipe_id"
        db.session.execute(sql, {"new_name":new_name, "recipe_id":recipe_id})
        db.session.commit()
        return ""
    if new_name == get_name(recipe_id):
        return ""
    return "Nimi '"+new_name+"' on jo varattu"

def change_servings(new_serves, recipe_id):
    sql = "UPDATE recipe SET serves=:serves WHERE id=:recipe_id"
    db.session.execute(sql, {"serves":new_serves, "recipe_id":recipe_id})
    db.session.commit()

def change_active_time(new_time, recipe_id):
    if not len(new_time):
        new_time = 0
    sql = "UPDATE recipe SET active=:active WHERE id=:recipe_id"
    db.session.execute(sql, {"active":float(new_time), "recipe_id":recipe_id})
    db.session.commit()

def change_passive_time(new_time, recipe_id):
    if not len(new_time):
        new_time = 0
    sql = "UPDATE recipe SET passive=:passive WHERE id=:recipe_id"
    db.session.execute(sql, {"passive":float(new_time), "recipe_id":recipe_id})
    db.session.commit()

def change_instructions(new_instructions, recipe_id):
    if len(new_instructions):
        sql = "UPDATE recipe SET instructions=:instructions WHERE id=:recipe_id"
        db.session.execute(sql, {"instructions":new_instructions, "recipe_id":recipe_id})
        db.session.commit()
        return ""
    return "Ohje ei voi olla tyhjä"

  #  CREATE TABLE recipe (
  #  id SERIAL PRIMARY KEY,
  #  name TEXT UNIQUE,
  #  user_id INTEGER REFERENCES users,
  #  instructions TEXT,
  #  serves INTEGER,
  #  active DECIMAL,
  #  passive DECIMAL
  #  );