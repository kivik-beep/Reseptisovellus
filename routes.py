from operator import truediv
from app import app
from flask import render_template, request, redirect
import users
import receipts
import users_receipts
import incredients

@app.route("/")
def index():
    return render_template("index.html", name = users.username()) 

@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("register.html", error = "Salasanat eivät täsmää")
        if len(username) < 4:
            return render_template("register.html", error = "Käyttäjänimen oltava vähintään neljän merkin mittainen")
        if len(password1) < 5:
            return render_template("register.html", error = "Salasanan oltava vähintään kuuden merkin mittainen")
        if users.register(username, password1):
            return redirect("/welcome")
        else:
            return render_template("register.html", error = "Rekisteröinti ei onnistunut, kokeile toista käyttäjänimeä")

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
            return render_template("login.html", error = "Väärä käyttäjätunnus tai salasana")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/favorites")
def favorites():
    return render_template("users_recipes.html", name = users.username(), type = "suosikki", recipes = users_receipts.get_favorites(users.user_id()))

@app.route("/my_recipes")
def my_recipes():
    return render_template("users_recipes.html", name = users.username(), type = "lisäämät ", recipes = users_receipts.all_added_by_user(users.user_id()))

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
        if bool(receipts.does_receipt_name_exist(name)):
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
            return render_template("new.html", error1 = error1, error2 = error2, error3 = error3, error4 = error4, name = name, 
                                    serves = serves, active = active, passive = passive, incredients = incredients, instructions = instructions)

        recipe_id = receipts.add_recipe(name, user_id, serves, instructions, active, passive, incredients)
        return redirect("/recipe/"+str(recipe_id))
    else:
        return render_template("new.html")

@app.route("/recipe/<int:id>", methods = ["GET", "POST"])
def recipe(id):
    if request.method == "POST":
        print("pyyntö on post")
        data = receipts.get_receipt(id)
        incredient_data = incredients.get_incredients(id)
        user_id = users.user_id()
        if users_receipts.check_favorite(user_id, id):
            print("ruoka oli suosikki, poistetaan")
            users_receipts.remove_favorite(user_id, id)
            like = "tykkää"
        else:
            print("ei kuulunut suosikkeihin, lisätään")
            users_receipts.add_favorite(user_id, id)
            like = "tykätty"
        return render_template("recipe.html", favorite_button = like, id = str(id), name = data[1], creator = users.username_recipe(data[2]), 
                                serves = data[4], active = data[4],passive = data[5], total = data[4] + data[5], instructions = data[3], 
                                incredients = incredient_data)
    elif receipts.does_receipt_id_exist(id):
        data = receipts.get_receipt(id)
        incredient_data = incredients.get_incredients(id)
        if users_receipts.check_favorite(users.user_id(), id):
            like = "tykätty"
        else:
            like = "tykkää"
        return render_template("recipe.html", favorite_button = like, id = str(id), name = data[1], creator = users.username_recipe(data[2]), 
                                serves = data[4], active = data[4], passive = data[5], total = data[4] + data[5], instructions = data[3], 
                                incredients = incredient_data)
    else:
        return render_template("error.html", message = "Reseptiä ei ole vielä luotu!")

@app.route("/recipes", methods = ["GET", "POST"])
def recipes():
    if request.method == "POST":
        incredient = request.form["incredient"]
        if bool(incredients.is_incredient(incredient)):
            incredient_id = incredients.get_incredient(incredient)[0]
            incredient_containing_recipes = receipts.get_receipts_containing(incredient_id)
            return render_template("recipes.html", list_heading = "Reseptit joissa mukana " + str(incredient), recipes = incredient_containing_recipes)
        else:
            current_recipes = receipts.get_all()
            return render_template("recipes.html", error = "Ei reseptejä joissa mukana aines " + str(incredient), list_heading = "Kaikki reseptit:", 
                                    recipes = current_recipes)
    else:
        current_recipes = receipts.get_all()
        return render_template("recipes.html", list_heading = "Kaikki reseptit:", recipes = current_recipes)

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")
