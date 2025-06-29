from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(3, 30)])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 50)])
    submit = SubmitField('Sign Up')


class Login(FlaskForm):
    email = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


