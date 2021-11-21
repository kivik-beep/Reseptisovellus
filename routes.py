from app import app
import users
from flask import render_template, request, redirect

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eivät täsmää")
        if users.register(username, password1):
            return redirect("/welcome")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/welcome")
        else:
            return render_template("error.html", message="Väärä käyttäjätunnus tai salasana")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/favourites")
def favourites():
    return render_template("favourites.html")

@app.route("/new")
def new():
    return "Täällä voit luoda uuden reseptin"

@app.route("/recipes")
def recipes():
    return render_template("recipes.html")

@app.route("/recipe/<int:id>")
def recipe(id):
    return "tällä sivulla on resepti no. " + str(id)

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")
