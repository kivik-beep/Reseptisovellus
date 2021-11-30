from operator import truediv
from app import app
from flask import render_template, request, redirect
import users
import foods

@app.route("/")
def index():
    return render_template("index.html", name=users.username()) 

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html", error="")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("register.html", error="Salasanat eivät täsmää")
        if len(username)<3:
            return render_template("register.html", error="Käyttäjänimen oltava vähintään neljän merkin mittainen")
        if len(password1)<5:
            return render_template("register.html", error="Salasanan oltava vähintään kuuden merkin mittainen")
        if users.register(username, password1):
            return redirect("/welcome")
        else:
            return render_template("register.html", error="Rekisteröinti ei onnistunut, kokeile toista käyttäjänimeä")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", error="")
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

@app.route("/favourites")
def favourites():
    return render_template("favourites.html", name=users.username(), type="suosikki", recipes=foods.get_favourites(users.user_id()))

@app.route("/new", methods=["get", "post"])
def add_recipe():
    if request.method == "GET":
        return render_template("new.html")
    
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
        if bool(foods.is_taken(name)):
            error1="nimi on jo varattu, keksi toinen tai lisää vaikka numero"
        if instructions == "":
            error4="Anna reseptille valmistusohjeet"
        if serves == "":
            error2="Anna reseptille annosmäärä"
        if incredients == "":
            error3="Anna reseptille ainekset"
        if active == "":
            active = 0
        if passive == "":
            passive = 0
        if error1 != "" or error2 != "" or error3 != "" or error4 != "":
            return render_template("new.html", error1=error1, error2=error2, error3=error3, error4=error4, name=name, serves=serves, active=active, passive=passive, incredients=incredients, instructions=instructions)

        recipe_id = foods.add_recipe(name,user_id,serves,instructions,active,passive,incredients)
        return redirect("/recipe/"+str(recipe_id))
    else:
        return render_template("new.html")


@app.route("/recipes")
def recipes():
    current_recipes= foods.get_all()
    return render_template("recipes.html", recipes=current_recipes)

@app.route("/recipe/<int:id>")
def recipe(id):
        if foods.is_created(id):
            data = foods.get_recipe(id)
            incredient_data = foods.get_incredients(id)
            return render_template("recipe.html", id=str(id), name=data[1], creator=users.username_recipe(data[2]), serves=data[4], active=data[4],passive=data[5], total=data[4]+data[5], instructions=data[3], incredients=incredient_data)
        else:
            return render_template("error.html", message="Reseptiä ei ole vielä luotu!")

@app.route("/my_recipes")
def my_recipes():
    return render_template("favourites.html", name=users.username(), type="lisäämät ", recipes=foods.get_mine(users.user_id()))

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")
