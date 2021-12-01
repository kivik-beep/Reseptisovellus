
from db import db

def get_all():
    sql = "SELECT id, name FROM recipe"
    return db.session.execute(sql).fetchall()
    

def add_recipe(name, user_id, serves, instructions, active, passive, incredients):
    sql = """INSERT INTO recipe (name, user_id, instructions, serves, active, passive) 
            VALUES (:name, :user_id, :instructions, :serves, :active, :passive) RETURNING id"""
    recipe_id = db.session.execute(sql, {"name":name, "user_id":user_id, "instructions":instructions, "serves":serves, "active": active, "passive":passive}).fetchone()[0]

    for row in incredients.split("\n"):
        parts = row.strip().split("-")
        if len(parts) != 3:
            continue

        quantity = parts[0]
        scale = parts[1]
        inc_name = parts[2]

        if bool(is_incredient(inc_name)):
            incredient_id = get_incredient(inc_name)[0]
        else:
            sql = "INSERT INTO incredient (name, type) VALUES (:inc_name, :type) RETURNING id"
            incredient_id = db.session.execute(sql, {"inc_name":inc_name, "type":0}).fetchone()[0]

        sql = """INSERT INTO incredients (recipe_id, incredient_id, quantity, scale) 
                VALUES (:recipe_id, :incredient_id, :quantity, :scale)"""
        db.session.execute(sql, {"recipe_id":recipe_id, "incredient_id": incredient_id, "quantity":quantity, "scale":scale})
    
    db.session.commit()
    return recipe_id

def get_incredient(name):
    sql = "SELECT * FROM incredient WHERE name=:name"
    incredient = db.session.execute(sql, {"name": name}).fetchall()
    return incredient[0]

def is_incredient(name):
    sql = "SELECT * FROM incredient WHERE name=:name"
    incredient = db.session.execute(sql, {"name": name}).fetchall()
    return bool(incredient)

def get_recipe(id):
    sql = "SELECT * FROM recipe WHERE id=:id"
    result = db.session.execute(sql, {"id": id}).fetchall()
    data = result[0]
    return data

def add_favourite(user_id, recipe_id):
    sql = "INSERT INTO favorites (user_id, recipe_id) VALUES (:user, :recipe)"
    db.session.execute(sql, {"user_id":user_id, "recipe_id":recipe_id})
    return 
    
def get_favourites(id):
    sql = "SELECT r.id, r.name FROM favorites as f, recipe as r WHERE f.recipe_id = r.id AND f.user_id=:user_id"
    return db.session.execute(sql, {"user_id": id}).fetchall()

def get_mine(id):
    sql = "SELECT id, name FROM recipe WHERE user_id=:user_id"
    return db.session.execute(sql, {"user_id": id}).fetchall()

def is_created(id):
    sql = "SELECT id FROM recipe WHERE id=:id"
    result = db.session.execute(sql, {"id": id}).fetchall()
    return bool(result)

def get_count():
    sql = "SELECT COUNT(*) FROM recipe"
    return db.session.execute(sql).fetchone()[0]

def is_taken(name):
    sql = "SELECT id FROM recipe WHERE name=:name"
    result = db.session.execute(sql, {"name": name}).fetchall()
    return bool(result)

def get_incredients(recipe_id):
    sql = "SELECT I.quantity, I.scale, N.name FROM incredients as I, incredient as N WHERE I.incredient_id = N.id AND I.recipe_id=:recipe_id"
    incredients = db.session.execute(sql, {"recipe_id": recipe_id}).fetchall()
    return incredients

def get_all_containing(incredient_id):
    sql = "SELECT r.id, r.name FROM recipe as r, incredients as i WHERE i.recipe_id=r.id AND i.incredient_id=:incredient_id"
    return db.session.execute(sql, {"incredient_id":incredient_id}).fetchall()