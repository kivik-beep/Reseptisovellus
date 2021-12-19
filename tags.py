from db import db


def add_tag(tag_name, recipe_id):
    taken = recipe_has_tag(tag_name, recipe_id)
    if len(tag_name) and not taken:
        sql = "INSERT INTO tag (name, recipe_id) VALUES (:tag_name, :recipe_id)"
        db.session.execute(sql, {"tag_name":tag_name, "recipe_id":recipe_id})
        db.session.commit()

def recipe_has_tag(tag_name, recipe_id):
    sql = "SELECT * FROM tag WHERE name=:tag_name AND recipe_id=:recipe_id"
    result = db.session.execute(sql, {"tag_name":tag_name, "recipe_id":recipe_id}).fetchall()
    return bool(result)

def rename_tag(tag_name, new_name, recipe_id):
    taken = recipe_has_tag(new_name, recipe_id)
    if len(new_name) and not taken:
        sql = "UPDATE tag SET name=:new_name WHERE name=:tag_name AND recipe_id=:recipe_id"
        db.session.execute(sql, {"new_name":new_name, "tag_name":tag_name, "recipe_id":recipe_id})
        db.session.commit()

def remove_tag(tag_name, recipe_id):
    sql = "DELETE FROM tag WHERE name=:tag_name AND recipe_id=:recipe_id"
    db.session.execute(sql, {"tag_name":tag_name, "recipe_id":recipe_id})
    db.session.commit()

def tags_for_recipe(recipe_id):
    sql = "SELECT name FROM tag WHERE recipe_id=:recipe_id"
    tags = db.session.execute(sql, {"recipe_id":recipe_id}).fetchall()
    return tags

def tags_all():
    sql = "SELECT name FROM tag GROUP BY name"
    tags = db.session.execute(sql).fetchall()
    return tags