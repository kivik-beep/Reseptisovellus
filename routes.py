from flask import render_template, request, redirect, session, abort
from app import app
import users
import receipts
import users_receipts
import incredients
import tags

@app.route("/")
def index():
    return render_template("index.html", name=users.username())

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"].lower()
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        error_name, error_match, error_length = "","",""
        if password1 != password2:
            error_match = "Salasanat eivät täsmää"
        if len(username) < 4:
            error_name = "Käyttäjänimen oltava vähintään neljän merkin mittainen. "
        if users.is_taken(username):
            error_name = "Käyttäjänimi on jo varattu"
        if len(password1) < 5:
            error_length = "Salasanan oltava vähintään kuuden merkin mittainen. "
        if error_name != "" or error_length != "" or error_match != "":
            return render_template("register.html", e_name=error_name, e_match=error_match,
                                   e_length=error_length, name=username)
        if users.register(username, password1):
            return redirect("/welcome")
        else:
            return render_template("register.html",
                                   e_name="Rekisteröinti ei onnistunut")

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
            return render_template("login.html", error="Väärä käyttäjätunnus tai salasana")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/favorites")
def favorites():
    return render_template("favorites.html", name=users.username(),
                           recipes=users_receipts.get_favorites(users.user_id()))

@app.route("/my_recipes")
def my_recipes():
    return render_template("users_recipes.html", name=users.username(),
                           recipes=users_receipts.receipts_from(users.user_id()))

@app.route("/new", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        if (session["csrf_token"] != request.form["csrf_token"]):
            return abort(403)
        name = request.form["name"]
        user_id = users.user_id()
        serve = request.form["serves"]
        active = request.form["active"]
        passive = request.form["passive"]
        incs = request.form["incredients"]
        instructions = request.form["instructions"]

        # e = error
        name_e, servings_e, inc_e, inst_e = "", "", "", ""

        if name == "":
            name_e = "Anna reseptille nimi"
        if len(name) > 20:
            name_e = "Nimi saa olla enintään 20 merkkiä pitkä"
        if receipts.is_name_taken(name):
            name_e = "nimi on jo varattu, keksi toinen tai lisää vaikka numero"
        if instructions == "":
            inst_e = "Anna reseptille valmistusohjeet"
        if serve == "":
            servings_e = "Anna reseptille annosmäärä"
        if incs == "":
            inc_e = "Anna reseptille ainekset"

        if name_e != "" or servings_e != "" or inc_e != "" or inst_e != "":
            return render_template("new.html", error1=name_e, error2=servings_e, error3=inc_e,
                                   error4=inst_e, name=name, serves=serve, active=active,
                                   passive=passive, incredients=incs,
                                   instructions=instructions)

        r_id = receipts.add_recipe(name, user_id, serve, instructions, active, passive, incs)
        #incredients.add_incredients_to_recipe(incs, r_id)
        return redirect("/recipe/"+str(r_id))
    else:
        return render_template("new.html")

@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
    if request.method == "POST":
        if (session["csrf_token"] != request.form["csrf_token"]):
            return abort(403)
        data = receipts.get_receipt(id)
        incredient_data = incredients.get_incredients(id)
        user_id = users.user_id()
        if users_receipts.is_favorite(user_id, id):
            users_receipts.remove_favorite(user_id, id)
            like = "tykkää"
        else:
            users_receipts.add_favorite(user_id, id)
            like = "tykätty"
        return render_template("recipe.html", favorite_button=like, id=str(id), name=data[1],
                               creator=users.username_recipe(data[2]), serves=data[4],
                               active=data[5], passive=data[6], total=data[5] + data[6],
                               instructions=data[3], incredients=incredient_data)
    elif receipts.is_id_taken(id):
        data = receipts.get_receipt(id)
        incredient_data = incredients.get_incredients(id)
        if users_receipts.is_favorite(users.user_id(), id):
            like = "tykätty"
        else:
            like = "tykkää"
        return render_template("recipe.html", favorite_button=like, id=str(id), name=data[1],
                               creator=users.username_recipe(data[2]), serves=data[4],
                               active=data[5], passive=data[6], total=data[5] + data[6],
                               instructions=data[3], incredients=incredient_data)
    else:
        return render_template("error.html", message="Reseptiä ei ole vielä luotu!")

@app.route("/modify/<int:id>", methods=["GET", "POST"])
def modify(id):
    if request.method == "POST":
        if (session["csrf_token"] != request.form["csrf_token"]):
            return abort(403)
        name_error, serving_error, instruction_error = "", "", ""
        if "name" in request.form:
            name_error = receipts.chage_name(request.form["r_name"], id)
        if "serves" in request.form:
            serving_error = receipts.change_servings(request.form["r_serves"], id)
        if "active" in request.form: 
            receipts.change_active_time(request.form["t_active"], id)
        if "passive" in request.form:           
            receipts.change_passive_time(request.form["t_passive"], id)
        if "change_instructions" in request.form:
            instruction_error = receipts.change_instructions(request.form["instructions"], id)
        if "inc" in request.form:
            print("muutetaan aineksia")
            print(request.form)
        if "new_inc" in request.form:
            print("lisätään uusi aines")
        if "tag" in request.form:
            print("Muutetaan tagia")
        if "new_tag" in request.form:
            tag = request.form["add_new_tag"]
            tags.add_tag(tag, id)
            recipe_tags = tags.tags_for_recipe(id)
        recipe_tags = tags.tags_for_recipe(id)
        rec = receipts.get_receipt(id)
        incs = incredients.get_incredients(id)

        if "ready" in request.form:
            redirect("/recipe/"+str(id))         
        return render_template("modify.html", id=str(id), recipe=rec, incredients=incs, tags=recipe_tags,
                                name_error=name_error, serving_error=serving_error, 
                                instruction_error=instruction_error)

    else: 
        rec = receipts.get_receipt(id)
        incs = incredients.get_incredients(id)
        recipe_tags = tags.tags_for_recipe(id)
        return render_template("modify.html", id=str(id), recipe=rec, incredients=incs, tags=recipe_tags)



@app.route("/recipes", methods=["GET", "POST"])
def recipes():
    if request.method == "POST":
        recipes = receipts.get_all()
        heading = "Kaikki reseptit:"
        tag_list = tags.tags_all()
        if "search" in request.form:
            incredient = request.form["incredient"].lower()
            if incredients.is_incredient(incredient):
                incredient_id = incredients.get_incredient(incredient)[0]
                incredient_containing_recipes = receipts.get_all_containing(incredient_id)
                return render_template("recipes.html",
                                       list_heading="Reseptit joissa mukana " + str(incredient),
                                       recipes=incredient_containing_recipes, tags=tag_list)
            if len(incredient) > 0:
                return render_template("recipes.html",
                                       error="Ei reseptejä joissa mukana sana " + str(incredient),
                                       list_heading="Kaikki reseptit:", recipes=recipes, tags=tag_list) 
        if "Anew" in request.form:
            heading = "Kaikki reseptit, uusin ensin:"
        if "Apopular" in request.form:
            recipes = receipts.all_order_by_favorite()
            heading="Kaikki reseptit, suosituin ensin:"
        if "Aspeed" in request.form:
            recipes = receipts.all_order_by_time()
            heading="Kaikki reseptit, nopein ensin:"
        if "Aincredients" in request.form:
            recipes = receipts.all_order_by_inc_quantity()
            heading="Kaikki reseptit, ainesmäärän mukaan:"
        for tag in tag_list:
            if tag[0] in request.form:
                recipes = receipts.all_with_tag(tag[0])
                heading = "Reseptit tagilla "+tag[0]

        return render_template("recipes.html", list_heading=heading, recipes=recipes, tags=tag_list)
    if request.method == "GET":
        recipes = receipts.get_all()
        heading = "Kaikki reseptit:"
        tag_list = tags.tags_all()
        return render_template("recipes.html", list_heading=heading, recipes=recipes, tags=tag_list)


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")
