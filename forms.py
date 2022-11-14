from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SelectMultipleField, widgets
from wtforms.validators import InputRequired, Email, EqualTo, Length, URL, Optional

DIET_CHOICES = [(1, "Gluten Free"),
                (2, "Ketogenic"), (3, "Vegetarian"), (4, "Lacto Vegetarian"), (5, "Ovo Vegetarian"), (6, "Lacto Vegetarian"), (7, "Vegan"), (8, "Pescetarian"), (9, "Paleolithic"), (10, "Primal"), (11, "Low FODMAP"), (12, "Whole30"), (13, "Dairy Free")]


class UserRegisterForm(FlaskForm):
    username = StringField("Username", validators=[
                           InputRequired("username can't be empty"), Length(
                               min=1, max=20, message="username length should be between 1 and 20 characters")])
    password = PasswordField("Password", validators=[
                             InputRequired("password can't be empty"), EqualTo("confirm", message="password must match")])
    confirm = PasswordField("Confirm Password", validators=[
        InputRequired("password can't be empty")])

    email = EmailField("Email Address", validators=[
                       InputRequired("email address can't be empty"), Email("not a valid email address")])
    diet_preferences = SelectMultipleField(
        "Diet Label", coerce=int, validators=[Optional()], choices=DIET_CHOICES, option_widget=widgets.CheckboxInput(), widget=widgets.ListWidget(prefix_label=False))


class UserLoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired("username can't be empty"), Length(
        min=1, max=20, message="username length should be between 1 and 20 characters")])
    password = PasswordField("Password", validators=[
                             InputRequired("password can't be empty")])


class UserEditForm(FlaskForm):
    username = StringField("Username", validators=[
                           InputRequired("username can't be empty"), Length(
                               min=1, max=20, message="username length should be between 1 and 20 characters")])
    password = PasswordField("Password", validators=[
                             InputRequired("password can't be empty")])
    email = EmailField("Email Address", validators=[
                       InputRequired("email address can't be empty"), Email("not a valid email address")])
    diet_preferences = SelectMultipleField(
        "Diet Label", coerce=int, validators=[Optional()], choices=DIET_CHOICES, option_widget=widgets.CheckboxInput(), widget=widgets.ListWidget(prefix_label=False))
