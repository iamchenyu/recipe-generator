from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()
db = SQLAlchemy(session_options={"expire_on_commit": False})


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    saves = db.relationship(
        "SavedRecipe", backref="user", cascade="all, delete-orphan")

    diet_preferences = db.relationship(
        "Diet", lazy='subquery', secondary="diet_preferences", backref="users")

    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"

    @classmethod
    def register(cls, **kwargs):
        hashed_pwd = bcrypt.generate_password_hash(
            kwargs["password"]).decode("UTF-8")
        kwargs["password"] = hashed_pwd
        return cls(**kwargs)

    @classmethod
    def authenticate(cls, username, password):
        user = User.query.filter(cls.username == username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user


class DietPreference(db.Model):
    __tablename__ = "diet_preferences"

    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"), primary_key=True)
    diet_id = db.Column(db.Integer, db.ForeignKey(
        "diets.id"), primary_key=True)

    def __repr__(self):
        return f"<Diet Preference: User #{self.user_id} - Diet #{self.diet_id}>"


class SavedRecipe(db.Model):
    __tablename__ = "saved_recipes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, nullable=False)
    recipe_title = db.Column(db.Text, nullable=False)
    recipe_summary = db.Column(db.Text)
    recipe_calories = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    diet_categories = db.relationship(
        "Diet", lazy='subquery', secondary="diet_categories", backref="recipes")

    def __repr__(self):
        return f"<Saved Recipe #{self.id}: {self.recipe_title}, #{self.recipe_id}>"


class Diet(db.Model):
    __tablename__ = "diets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    diet_label = db.Column(db.Text, nullable=False, unique=True)

    def __repr__(self):
        return f"<Diet #{self.id}: {self.diet_label}>"


class DietCategory(db.Model):
    __tablename__ = "diet_categories"

    recipe_id = db.Column(db.Integer, db.ForeignKey(
        "saved_recipes.recipe_id"), primary_key=True)
    diet_id = db.Column(db.Integer, db.ForeignKey(
        "diets.id"), primary_key=True)

    def __repr__(self):
        return f"<Diet Category: Recipe #{self.recipe_id} - Diet #{self.diet_id}>"
