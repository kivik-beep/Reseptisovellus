from db import db
import incredients

def add_recipe(name, user_id, serves, instructions, active, passive, increds):
    sql = """INSERT INTO recipe (name, user_id, instructions, serves, active, passive) 
            VALUES (:name, :user_id, :instructions, :serves, :active, :passive) RETURNING id"""
    recipe_id = db.session.execute(sql, {"name":name, "user_id":user_id, "instructions":instructions, "serves":serves, "active": active, "passive":passive}).fetchone()[0]

    for row in increds.split("\n"):
        parts = row.strip().split("-")
        if len(parts) != 3:
            continue

        quantity = parts[0]
        scale = parts[1]
        inc_name = parts[2]

        if incredients.is_incredient(inc_name):
            incredient_id = incredients.get_incredient(inc_name)[0]
        else:
            incredient_id = incredients.add_incredient(inc_name, 0)

        incredients.add_incredients_to_recipe(recipe_id, incredient_id, quantity, scale)

    db.session.commit()
    return recipe_id

def get_all():
    sql = "SELECT id, name FROM recipe"
    return db.session.execute(sql).fetchall()

def count_receipts():
    sql = "SELECT COUNT(*) FROM recipe"
    return db.session.execute(sql).fetchone()[0]

def get_receipt(id):
    sql = "SELECT * FROM recipe WHERE id=:id"
    result = db.session.execute(sql, {"id": id}).fetchall()
    data = result[0]
    return data

def is_id_taken(id):
    sql = "SELECT id FROM recipe WHERE id=:id"
    result = db.session.execute(sql, {"id": id}).fetchall()
    return bool(result)

def is_name_taken(name):
    sql = "SELECT id FROM recipe WHERE name=:name"
    result = db.session.execute(sql, {"name": name}).fetchall()
    return bool(result)


def get_all_containing(incredient_id):
    sql = """SELECT r.id, r.name FROM recipe as r, incredients as i 
            WHERE i.recipe_id=r.id AND i.incredient_id=:incredient_id"""
    return db.session.execute(sql, {"incredient_id":incredient_id}).fetchall()