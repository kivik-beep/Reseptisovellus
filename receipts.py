from db import db
import incredients

def add_recipe(name, user_id, serves, instructions, active, passive, increds):
    sql = """INSERT INTO recipe (name, user_id, instructions, serves, active, passive)
            VALUES (:name, :user_id, :instructions, :serves, :active, :passive) RETURNING id"""
    recipe_id = db.session.execute(sql, {"name":name, "user_id":user_id,
                                         "instructions":instructions, "serves":serves,
                                         "active": active, "passive":passive}).fetchone()[0]

    for row in increds.split("\n"):
        parts = row.strip().split("+")
        if len(parts) != 3:
            continue

        quantity = parts[0]
        scale = parts[1]
        inc_name = parts[2].lower()

        if incredients.is_incredient(inc_name):
            incredient_id = incredients.get_incredient(inc_name)[0]
        else:
            sql = "INSERT INTO incredient (name, type) VALUES (:inc_name, :type) RETURNING id"
            incredient_id = db.session.execute(sql, {"inc_name":inc_name, "type":0}).fetchone()[0]

        sql = """INSERT INTO incredients (recipe_id, incredient_id, quantity, scale)
                VALUES (:recipe_id, :incredient_id, :quantity, :scale)"""
        db.session.execute(sql, {"recipe_id":recipe_id, "incredient_id": incredient_id,
                                 "quantity":quantity, "scale":scale})



    db.session.commit()
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


# different recipe sortings
def get_all_containing(incredient_id):
    sql = """SELECT r.id, r.name FROM recipe as r, incredients as i
            WHERE i.recipe_id=r.id AND i.incredient_id=:incredient_id"""
    return db.session.execute(sql, {"incredient_id":incredient_id}).fetchall()

def all_with_tag(tag_name):
    sql = """SELECT r.id, r.name FROM recipe as r, tags as t
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

