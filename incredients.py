from db import db
## incredients, receipts incredients and tags

def add_incredient(name, type):
    sql = "INSERT INTO incredient (name, type) VALUES (:inc_name, :type) RETURNING id"
    incredient_id = db.session.execute(sql, {"inc_name":name, "type":type}).fetchone()[0]
    return incredient_id

def remove_incredient(id):
    return

def add_incredients_to_recipe(recipe_id, incredient_id, quantity, scale):
    sql = """INSERT INTO incredients (recipe_id, incredient_id, quantity, scale) 
        VALUES (:recipe_id, :incredient_id, :quantity, :scale)"""
    db.session.execute(sql, {"recipe_id":recipe_id, "incredient_id": incredient_id, "quantity":quantity, "scale":scale})
    db.session.commit()
    return

def get_incredient(name):
    sql = "SELECT * FROM incredient WHERE name=:name"
    incredient = db.session.execute(sql, {"name": name}).fetchall()
    return incredient[0]

def is_incredient(name):
    sql = "SELECT * FROM incredient WHERE name=:name"
    incredient = db.session.execute(sql, {"name": name}).fetchall()
    return bool(incredient)

def get_incredients(recipe_id):
    sql = "SELECT I.quantity, I.scale, N.name FROM incredients as I, incredient as N WHERE I.incredient_id = N.id AND I.recipe_id=:recipe_id"
    incredients = db.session.execute(sql, {"recipe_id": recipe_id}).fetchall()
    return incredients