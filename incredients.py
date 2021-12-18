from db import db
## incredients and tags

# incredients
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
    incredient = db.session.execute(sql, {"name": inc_name}).fetchall()
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


# tags
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
    sql = "UPDATE tag SET :new_name WHERE name=:tag_name AND recipe_id=:recipe_id"
    db.session.execute(sql, {"new_name":new_name,"tag_name":tag_name, "recipe_id":recipe_id})
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
    sql = "SELECT name FROM tag"
    tags = db.session.execute(sql).fetchall()
    return tags