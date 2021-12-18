from db import db


def add_incredient(name, type):
    sql = "INSERT INTO incredient (name, type) VALUES (:inc_name, :type) RETURNING id"
    incredient_id = db.session.execute(sql, {"inc_name":name, "type":type}).fetchone()[0]
    return incredient_id

def add_incredients_to_recipe(recipe_id, incredient_id, quantity, scale):
    sql = """INSERT INTO incredients (recipe_id, incredient_id, quantity, scale)
        VALUES (:recipe_id, :incredient_id, :quantity, :scale)"""
    db.session.execute(sql, {"recipe_id":recipe_id, "incredient_id": incredient_id,
                             "quantity":quantity, "scale":scale})
    db.session.commit()

def get_incredient(inc_name):
    sql = "SELECT * FROM incredient WHERE name=:name"
    incredient = db.session.execute(sql, {"name": inc_name}).fetchone()[0]
    return incredient[0]

def is_incredient(inc_name):
    sql = "SELECT * FROM incredient WHERE name=:name"
    incredient = db.session.execute(sql, {"name": inc_name}).fetchall()
    return bool(incredient)

def get_incredients(recipe_id):
    sql = """SELECT I.quantity, I.scale, N.name FROM incredients as I, incredient as N
          WHERE I.incredient_id = N.id AND I.recipe_id=:recipe_id"""
    incredients = db.session.execute(sql, {"recipe_id": recipe_id}).fetchall()
    return incredients

def add_incredients(incredient_data, recipe_id):
    for row in incredient_data.split("\n"):
        parts = row.strip().split("+")
        if parts[0].isnumeric():
            quantity = parts[0]
            scale = parts[1]
            name = parts[2:]
        else:
            quantity = 1
            scale = parts[0]
            name = parts[1:]
        inc_name = ""
        
        for part in name:
            inc_name += part
        inc_name = inc_name.lower()

        if is_incredient(inc_name):
            incredient_id = get_incredient(inc_name)
        else:
            sql = "INSERT INTO incredient (name, type) VALUES (:inc_name, :type) RETURNING id"
            incredient_id = db.session.execute(sql, {"inc_name":inc_name, "type":0}).fetchone()[0]

        sql = """INSERT INTO incredients (recipe_id, incredient_id, quantity, scale)
                VALUES (:recipe_id, :incredient_id, :quantity, :scale)"""
        db.session.execute(sql, {"recipe_id":recipe_id, "incredient_id": incredient_id,
                                 "quantity":quantity, "scale":scale})
        db.session.commit()