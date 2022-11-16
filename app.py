import os
import re
import requests

from flask import Flask, render_template, flash, redirect, session, g, jsonify, url_for, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Diet, SavedRecipe
from forms import UserRegisterForm, UserLoginForm, UserEditForm, DIET_CHOICES
from sqlalchemy.exc import IntegrityError
from dotenv import load_dotenv
import werkzeug.exceptions as ex


app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv("API_KEY")

uri = (
    os.environ.get('DATABASE_URL', 'postgresql:///recipe_generator'))
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "temp_key")
app.config['API_KEY'] = os.environ.get("API_KEY", API_KEY)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
print(os.environ.get("API_KEY"))
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

# toolbar = DebugToolbarExtension(app)

connect_db(app)

CURR_USER_KEY = "curr_user"
BASE_URL = "https://api.spoonacular.com/recipes"


@app.before_request
def add_user_to_g():
    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
    else:
        g.user = None


def do_login(user):
    session[CURR_USER_KEY] = user.id


def do_logout():
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.after_request
def add_header(req):
    """Add non-caching headers on every request."""

    req.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    req.headers["Pragma"] = "no-cache"
    req.headers["Expires"] = "0"
    req.headers['Cache-Control'] = 'public, max-age=0'
    return req

# error handling
@app.errorhandler(404)
def not_found(e):
    res = requests.get("https://http.cat/404")
    file = open("static/images/httpstatus/404.png", "wb")
    file.write(res.content)
    file.close()
    return render_template("404.html"), 404


@app.errorhandler(405)
def method_not_allowed(e):
    res = requests.get("https://http.cat/405")
    file = open("static/images/httpstatus/405.png", "wb")
    file.write(res.content)
    file.close()
    return render_template("405.html"), 405


class apiCallLimit(ex.HTTPException):
    code = 402
    description = 'Exceed API Calls Limit'


def handle_402(e):
    res = requests.get("https://http.cat/402")
    file = open("static/images/httpstatus/402.png", "wb")
    file.write(res.content)
    file.close()
    return render_template("402.html")


app.register_error_handler(apiCallLimit, handle_402)


@app.route("/")
def homepage():
    if not g.user:
        flash("Please log in first", "alert alert-warning")
        return redirect(url_for("login_user"))
    return render_template("homepage.html")


@app.route("/register", methods=["GET", "POST"])
def register_user():
    if g.user:
        flash("Please log out first", "alert alert-warning")
        return redirect(url_for("homepage"))
    form = UserRegisterForm()
    if form.validate_on_submit():
        user = User.register(username=form.username.data,
                             password=form.password.data,
                             email=form.email.data
                             )
        diets = [Diet.query.get(diet)
                 for diet in form.diet_preferences.data]
        user.diet_preferences.extend(diets)
        try:
            db.session.add(user)
            db.session.commit()
            do_login(user)
            flash(f"Welcome, {user.username}!", "alert alert-info")
            return redirect(url_for("homepage"))
        except IntegrityError as e:
            db.session.rollback()
            if "users_username_key" in str(e):
                form.username.errors.append("username already exists")
            if "users_email_key" in str(e):
                form.email.errors.append("email already exists")
    return render_template("register.html", form=form, diets=DIET_CHOICES)


@app.route("/login", methods=["GET", "POST"])
def login_user():
    if g.user:
        flash("You already logged in", "alert alert-warning")
        return redirect(url_for("homepage"))
    form = UserLoginForm()

    if form.validate_on_submit():
        user = User.authenticate(username=form.username.data,
                                 password=form.password.data)
        if user:
            do_login(user)
            flash(f"Welcome back, {user.username}!", "alert alert-info")
            return redirect(url_for("homepage"))

        form.password.errors = ["invalid username or password"]

    return render_template("login.html", form=form)


@app.route("/logout", methods=["POST"])
def logout_user():
    do_logout()
    flash(f"Goodbye, {g.user.username}!", "alert alert-info")
    return redirect(url_for("login_user"))


@app.route("/recipes", methods=["POST"])
def search_recipes():
    ingredients = request.json["ingredients"]
    response = requests.get(
        f"{BASE_URL}/complexSearch?includeIngredients={ingredients}&apiKey={API_KEY}&addRecipeNutrition=true&fillIngredients=true&number=6")
    if response.status_code == 402:
        raise apiCallLimit
    return response.json()


@app.route("/recipe/<int:id>")
def get_recipe_details(id):
    if not g.user:
        flash("Please log in first", "alert alert-warning")
        return redirect(url_for("login_user"))
    # get recipe
    recipe_response = requests.get(
        f"{BASE_URL}/{id}/information?apiKey={API_KEY}")
    if recipe_response.status_code == 402:
        raise apiCallLimit
    recipe = recipe_response.json()
    # get user saved recipes id
    saves_id = [save.recipe_id for save in g.user.saves]
    # get ingredients
    ingredients_response = requests.get(
        f"{BASE_URL}/{id}/ingredientWidget.png?apiKey={API_KEY}", headers={"Accept": "image/png"})
    file = open(f"static/images/ingredients/{id}.png", "wb")
    file.write(ingredients_response.content)
    file.close()
    # get nutrition label
    nutrition_response = requests.get(
        f"{BASE_URL}/{id}/nutritionLabel.png?apiKey={API_KEY}&showIngredients=true", headers={"Content-Type": "image/png"})
    file2 = open(f"static/images/nutritions/{id}.png", "wb")
    file2.write(nutrition_response.content)
    file2.close()
    return render_template("recipe.html", recipe=recipe, saves_id=saves_id)


@app.route("/recipe/<int:id>/save", methods=["POST"])
def save_recipe(id):
    recipe_response = requests.get(
        f"{BASE_URL}/{id}/information?apiKey={API_KEY}&includeNutrition=true")
    recipe = recipe_response.json()
    saved_recipe = SavedRecipe(
        recipe_id=recipe["id"], recipe_title=recipe["title"], recipe_summary=recipe["summary"], recipe_calories=recipe["nutrition"]["nutrients"][0]["amount"], user_id=session[CURR_USER_KEY])
    diets = [Diet.query.filter(Diet.diet_label == diet).first()
             for diet in recipe["diets"]]
    diet_labels = [diet for diet in diets if diet is not None]
    saved_recipe.diet_categories.extend(diet_labels)
    db.session.add(saved_recipe)
    db.session.commit()
    return jsonify({"message": "success"})


@app.route("/recipe/<int:id>/unsave", methods=["POST"])
def unsave_recipe(id):
    recipe = SavedRecipe.query.filter(SavedRecipe.recipe_id == id).first()
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"message": "success"})


@app.route("/user/<int:id>/saved-recipes")
def get_saved_recipes(id):
    if not g.user:
        flash("Please log in first", "alert alert-warning")
        return redirect(url_for("login_user"))
    user = User.query.get_or_404(id)
    saved_recipes = user.saves
    return render_template("saved_recipes.html", recipes=saved_recipes)


@app.route("/user/<int:id>/edit", methods=["GET", "POST"])
def edit_user(id):
    if not g.user:
        flash("Please log in first", "alert alert-warning")
        return redirect(url_for("login_user"))
    user = User.query.get_or_404(id)
    form = UserEditForm(obj=user)
    user_diets = [pre.id for pre in user.diet_preferences]

    if form.validate_on_submit():
        if User.authenticate(username=user.username, password=form.password.data):
            print("validated")
            user.username = form.username.data
            user.email = form.email.data
            diets = [Diet.query.get(diet)
                     for diet in form.diet_preferences.data]
            user.diet_preferences = diets
            try:
                db.session.commit()
                flash(f"Your profile has been updated", "alert alert-info")
                return redirect(url_for("homepage"))
            except IntegrityError as e:
                db.session.rollback()
                if "users_email_key" in str(e):
                    form.email.errors.append("email already exists")
                if "users_username_key" in str(e):
                    form.username.errors.append("username already exists")
        else:
            errors = list(form.password.errors)
            errors.append(
                "Invalid password. Please try again.")
            form.password.errors = tuple(errors)

    return render_template("edit_user.html", user_diets=user_diets, form=form, DIET_CHOICES=DIET_CHOICES)
