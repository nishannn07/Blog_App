from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from flask import Flask, render_template
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title=StringField('Title',validators=[DataRequired(message="Title cannot be empty."), Length(max=100)])
    body=TextAreaField('Body',validators=[DataRequired(message="Body cannot be empty.")])
    is_published=BooleanField('Publish Now.')
    submit = SubmitField('Submit')