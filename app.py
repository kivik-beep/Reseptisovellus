from flask import Flask
from flask import redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    db.session.execute("INSERT INTO visitors (time) VALUES (NOW())")
    db.session.commit()
    result = db.session.execute("SELECT COUNT(*) FROM visitors")
    counter = result.fetchone()[0]
    return render_template("index.html", counter=counter) 

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/welcome", methods=["POST"])
def welcome():
    return render_template("welcome.html", name=request.form["name"])

@app.route("/new")
def new():
    return "Täällä voit luoda uuden reseptin"

@app.route("/recipies")
def recipies():
    return "Täällä tulee näkymään kaikki reseptit"

@app.route("/recipes/<int : id>")
def recipies(id):
    return "Tälle sivulle tulee ohje reseptiin " + str(id)
