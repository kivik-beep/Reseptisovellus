from db import db


def add_incredient(name):
    sql = "INSERT INTO incredient (name, type) VALUES (:inc_name, :type) RETURNING id"
    incredient_id = db.session.execute(sql, {"inc_name":name, "type":0}).fetchone()[0]
    return incredient_id

def get_incredient(inc_name):
    sql = "SELECT id FROM incredient WHERE name=:name"
    incredient = db.session.execute(sql, {"name": inc_name}).fetchone()[0]
    print(incredient, inc_name)
    return incredient

def get_incredient_with(inc_name):
    sql = "SELECT id FROM incredient WHERE name LIKE :name"
    incredient = db.session.execute(sql, {"name": '%'+inc_name+'%'}).fetchall()
    return incredient

def is_incredient(inc_name):
    sql = "SELECT * FROM incredient WHERE name=:name"
    incredient = db.session.execute(sql, {"name": inc_name}).fetchall()
    return bool(incredient)

def get_incredients(recipe_id):
    sql = """SELECT I.quantity, I.scale, N.name, N.id FROM incredients as I, incredient as N
          WHERE I.incredient_id = N.id AND I.recipe_id=:recipe_id"""
    incredients = db.session.execute(sql, {"recipe_id": recipe_id}).fetchall()
    return incredients

def is_used(incredient):
    sql = """SELECT ii.incredient_id FROM incredient as i, incredients as ii
          WHERE i.id = ii.incredient_id AND i.name LIKE :word GROUP BY ii.incredient_id"""
    result = db.session.execute(sql, {"word": '%'+incredient+'%'}).fetchall()
    return len(result)

def add_incredients(incredient_data, recipe_id):
    for row in incredient_data.split("\n"):
        parts = row.strip().split("+")
        if len(parts) < 2:
            continue
        try:
            quantity = float(parts[0])
            scale = parts[1]
            name = parts[2:]
        except:
            quantity = 1
            scale = parts[0]
            name = parts[1:]
        inc_name = ""
        for part in name:
            inc_name += part + " "
        inc_name = inc_name.lower()

        if is_incredient(inc_name):
            incredient_id = get_incredient(inc_name)
        else:
            incredient_id = add_incredient(inc_name)
        add_incredient_parts(recipe_id, incredient_id, quantity, scale)

def change_incredient(recipe_id, inc_id, new_quantity, new_scale, new_name):
    if is_incredient(new_name):
        incredient_id = get_incredient(new_name)
    else:
        incredient_id = add_incredient(new_name)

    remove_connection(recipe_id, inc_id)
    add_incredient_parts(recipe_id, incredient_id, new_quantity, new_scale)
    

def add_incredient_parts(recipe_id, incredient_id, quantity, scale):
    sql = """INSERT INTO incredients (recipe_id, incredient_id, quantity, scale)
             VALUES (:recipe_id, :incredient_id, :quantity, :scale)"""
    db.session.execute(sql, {"recipe_id":recipe_id, "incredient_id": incredient_id,
                             "quantity":quantity, "scale":scale})
    db.session.commit()

def remove_connection(recipe_id, incredient_id):
    sql = """DELETE FROM incredients WHERE recipe_id=:recipe_id AND incredient_id=:incredient_id"""
    db.session.execute(sql, {"recipe_id":recipe_id, "incredient_id": incredient_id})
    db.session.commit()

#CREATE TABLE incredient (
#    id SERIAL PRIMARY KEY,
#    name TEXT UNIQUE,
#    type TEXT
#);

#CREATE TABLE incredients (
#    recipe_id INTEGER REFERENCES recipe ON DELETE CASCADE,
#    incredient_id INTEGER REFERENCES incredient,
#    quantity DECIMAL,
#    scale TEXT
#);

