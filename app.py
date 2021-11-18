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
    return "Täällä voit luoda uuden käyttäjätunnuksen"

@app.route("/login")
def login():
    return "Tällä sivulla voit kirjautua sisään"

@app.route("/your-page")
def welcome():
    return "sisäänkirjautuminen palauttaa tänne, täällä samat vaihtoehdot kuin etusivulla + uusi resepti"
    
@app.route("/new")
def new():
    return "Täällä voit luoda uuden reseptin"
    
