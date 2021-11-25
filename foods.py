
from db import db

def get_all():
    sql = "SELECT id, name FROM recipes"
    return db.session.execute(sql).fetchall()

def add_recipe(name,serves,instructions,active,passive,incredients):
    sql = """INSERT INTO recipes (name, instructions, serves, active, passive) 
            VALUES (:name, :instructions, :serves, :active, :passive) RETURNING id"""
    recipe_id = db.session.execute(sql, {"name":name, "instructions":instructions, "serves":serves, "active": active, "passive":passive}).fetchone()[0]

    for row in incredients.split("\n"):
        parts = row.strip().split("-")
        if len(parts) != 3:
            continue

        sql = "INSERT INTO incredient (name) VALUES (:inc_name)"
        incredient_id = db.session.execute(sql, {"name":parts[2]})

        sql = """INSERT INTO incredients (recipe_id, incredient_id, quantity) 
            VALUES (:recipe_id, :incredient_id, :quantity"""

        db.session.execute(sql, {"recipe_id":recipe_id, "incredient_id":incredient_id, "quantity":parts[0]})
    
    db.session.commit()
    return recipe_id

