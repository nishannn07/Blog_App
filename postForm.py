from wtforms import TextAreaField, StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    post = TextAreaField('Post', validators=[DataRequired()])
    # user = SelectField('Author', coerce=int(), validators=[DataRequired()])
    # user = IntegerField('Author', validators=[DataRequired()])
    tag1 = StringField('tag1')
    tag2 = StringField('tag2')
    tag3 = StringField('tag3')
    submit = SubmitField('Post')
    draft = SubmitField('Draft')


    @classmethod
    def from_draft(cls, post):
        form = cls()
        form.title.data = post.title
        form.post.data = post.content

        if len(post.tags) > 0: form.tag1.data = post.tags[0].name
        if len(post.tags) > 1: form.tag2.data = post.tags[1].name
        if len(post.tags) > 2: form.tag3.data = post.tags[2].name

        return form