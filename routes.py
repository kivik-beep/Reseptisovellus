from app import app
import visits
from flask import render_template, request, redirect

@app.route("/")
def index():
    visits.add_visit()
    counter = visits.get_counter
    return render_template("index.html", counter=counter) 

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user.login(username, password):
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
    return "Täällä tulee näkymään kaikki reseptit"

@app.route("/recipe/<int:id>")
def recipe(id):
    return "tällä sivulla on resepti no. " + str(id)
