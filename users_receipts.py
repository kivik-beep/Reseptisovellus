from db import db
## users favorites and own receipts

def add_favorite(user_id, recipe_id):
    sql = "INSERT INTO favorites (user_id, recipe_id) VALUES (:user_id, :recipe_id)"
    db.session.execute(sql, {"user_id":user_id, "recipe_id":recipe_id})
    db.session.commit()
    return 
    
def get_favorites(id):
    sql = "SELECT r.id, r.name FROM favorites as f, recipe as r WHERE f.recipe_id = r.id AND f.user_id=:user_id"
    return db.session.execute(sql, {"user_id": id}).fetchall()

def check_favorite(user_id, recipe_id):
    sql = "SELECT * FROM favorites WHERE user_id=:user_id AND recipe_id=:recipe_id"
    result = db.session.execute(sql, {"user_id": user_id, "recipe_id": recipe_id}).fetchall()
    return bool(result)

def remove_favorite(user_id, recipe_id):
    sql = "DELETE FROM favorites WHERE user_id=:user_id AND recipe_id=:recipe_id"
    db.session.execute(sql, {"user_id": user_id, "recipe_id": recipe_id})
    db.session.commit()
    return

def all_added_by_user(user_id):
    sql = "SELECT id, name FROM recipe WHERE user_id=:user_id"
    return db.session.execute(sql, {"user_id": user_id}).fetchall()
