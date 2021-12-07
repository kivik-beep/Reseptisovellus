from operator import truediv
from app import app
from flask import render_template, request, redirect
import users
import receipts
import users_receipts
import incredients

@app.route("/")
def index():
    return render_template("index.html", name=users.username()) 

@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        error_name = ""
        error_match = ""
        error_length = ""
        if password1 != password2:
            error_match = "Salasanat eivät täsmää"
        if len(username) < 4:
            error_name="Käyttäjänimen oltava vähintään neljän merkin mittainen"
        if len(password1) < 5:
            error_length="Salasanan oltava vähintään kuuden merkin mittainen"
        if error_name != "" and error_length != "" and error_match != "":
            return render_template("register.html", e_name = error_name, e_match = error_match, e_length = error_length)
        if users.register(username, password1):
            return redirect("/welcome")
        else:
            return render_template("register.html", error_name="Rekisteröinti ei onnistunut, kokeile toista käyttäjänimeä")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/welcome")
        else:
            return render_template("login.html", error="Väärä käyttäjätunnus tai salasana")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/favorites")
def favorites():
    return render_template("favorites.html", name=users.username(), recipes=users_receipts.get_favorites(users.user_id()))

@app.route("/my_recipes")
def my_recipes():
    return render_template("users_recipes.html", name=users.username(), recipes=users_receipts.receipts_from(users.user_id()))

@app.route("/new", methods = ["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        name = request.form["name"]
        user_id = users.user_id()
        serves = request.form["serves"]
        active = request.form["active"]
        passive = request.form["passive"]
        incredients = request.form["incredients"]
        instructions = request.form["instructions"]

        error1 = ""
        error2 = ""
        error3 = ""
        error4 = ""

        if name == "":
            error1="Anna reseptille nimi"
        if len(name)> 20:
            error1="Nimi saa olla enintään 20 merkkiä pitkä"
        if bool(receipts.is_name_taken(name)):
            error1 = "nimi on jo varattu, keksi toinen tai lisää vaikka numero"
        if instructions == "":
            error4 = "Anna reseptille valmistusohjeet"
        if serves == "":
            error2 = "Anna reseptille annosmäärä"
        if incredients == "":
            error3 = "Anna reseptille ainekset"
        if active == "":
            active = 0
        if passive == "":
            passive = 0
        if error1 != "" or error2 != "" or error3 != "" or error4 != "":
            return render_template("new.html", error1=error1, error2=error2, error3=error3, error4=error4, name=name, 
                                    serves=serves, active=active, passive=passive, incredients=incredients, instructions=instructions)

        recipe_id = receipts.add_recipe(name, user_id, serves, instructions, active, passive, incredients)
        return redirect("/recipe/"+str(recipe_id))
    else:
        return render_template("new.html")

@app.route("/recipe/<int:id>", methods = ["GET", "POST"])
def recipe(id):
    if request.method == "POST":
        data = receipts.get_receipt(id)
        incredient_data = incredients.get_incredients(id)
        user_id = users.user_id()
        if users_receipts.is_favorite(user_id, id):
            users_receipts.remove_favorite(user_id, id)
            like = "tykkää"
        else:
            users_receipts.add_favorite(user_id, id)
            like = "tykätty"
        return render_template("recipe.html", favorite_button=like, id=str(id), name=data[1], creator=users.username_recipe(data[2]), 
                                serves=data[4], active=data[5],passive=data[6], total= data[5] + data[6], instructions=data[3], 
                                incredients=incredient_data)
    elif receipts.is_id_taken(id):
        data = receipts.get_receipt(id)
        incredient_data = incredients.get_incredients(id)
        if users_receipts.is_favorite(users.user_id(), id):
            like = "tykätty"
        else:
            like = "tykkää"
        return render_template("recipe.html", favorite_button=like, id=str(id), name=data[1], creator=users.username_recipe(data[2]), 
                                serves=data[4], active=data[5], passive=data[6], total= data[5] + data[6], instructions=data[3], 
                                incredients=incredient_data)
    else:
        return render_template("error.html", message = "Reseptiä ei ole vielä luotu!")

@app.route("/modify/<int:id>", methods = ["GET", "POST"])
def modify(id):
    recipe = receipts.get_receipt(id)
    incs = incredients.get_incredients(id)
    return render_template("modify.html", recipe=recipe, incredients=incs)

@app.route("/recipes", methods = ["GET", "POST"])
def recipes():
    if request.method == "POST":
        incredient = request.form["incredient"].lower()
        if incredients.is_incredient(incredient):
            incredient_id = incredients.get_incredient(incredient)[0]
            incredient_containing_recipes = receipts.get_all_containing(incredient_id)
            return render_template("recipes.html", list_heading = "Reseptit joissa mukana " + str(incredient), recipes=incredient_containing_recipes)
        elif len(incredient) > 0:
            current_recipes = receipts.get_all()
            return render_template("recipes.html", error="Ei reseptejä joissa mukana aines " + str(incredient), list_heading="Kaikki reseptit:", recipes = current_recipes)
    else:
        current_recipes = receipts.get_all()
        return render_template("recipes.html", list_heading="Kaikki reseptit:", recipes=current_recipes)
    
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")
