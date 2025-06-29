from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from forms import UserForm, Login
from postForm import PostForm
from flask_restful import Resource

# class HelloWorld(Resource):
#     def get(self):
#         return {'message' : User.emailExits()}, 200

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from model.models import *
from controller import post_controller, auth_controller

@app.route('/', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        auth_controller.user_login(form)
        return redirect(url_for('index'))
    return render_template('Login.html', form=form)
    
@app.route('/dashboard')
def index():
    if 'id' not in session:
        flash("Please log in first", "warning")
        return redirect(url_for('login'))

    posts = post_controller.list_posts(session['id'])
    drafts=post_controller.list_draft(session['id'])
    draft_forms = [PostForm.from_draft(d) for d in drafts]
    combined = list(zip(draft_forms, drafts))
    form = PostForm()
    # if form.validate_on_submit():
    #     new_post = Post(title=form.title.data, content=form.post.data, user_id=session['id'])
    #     db.session.add(new_post)
    #     db.session.commit()
    return render_template('home.html', username=session['uname'], posts=posts, form=form, combined=combined)
    # return post_controller.list_posts(session['id'])

@app.route('/signup', methods=['GET', 'POST'])
def SingUp():
    form = UserForm()
    if form.validate_on_submit():
        auth_controller.register_user(form)
        return redirect(url_for('login'))
    return render_template('signUp.html', form = form)

@app.route('/post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        if form.submit.data:
            new_post = Post(title=form.title.data, content=form.post.data, is_published=True, user_id=session['id'])
            tags = [
                post_controller.getOrCreateTag(name)
                for name in [form.tag1.data, form.tag2.data, form.tag3.data]
                if name 
            ]
            new_post.tags = tags
        elif form.draft.data:
             new_post = Post(title=form.title.data, content=form.post.data, is_published=False, user_id=session['id'])
        
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    # return render_template('post.html', form=form)

@app.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    if 'id' not in session:
        flash("please log in", 'warning')
        return redirect(url_for('login'))
    
    post = post_controller.get_post(post_id)

    if post.user_id != session['id']:
        flash("Unauthorized", "danger")
        return redirect(url_for('index'))
    
    post.is_deleted = True
    db.session.commit()
    flash('Post deleted', 'success')
    return redirect(url_for('index'))

@app.route('/update_draft/<int:draft_id>', methods=['POST'])
def update_draft(draft_id):
    form = PostForm()
    if form.validate_on_submit():
        post_controller.update_post(draft_id, form)
        if form.submit.data:
            post_controller.save_draft(draft_id)
    return redirect(url_for('index'))

@app.route('/posts', methods=['GET', 'POST'])
def getPosts():
    if request.method == 'POST':
        
        posts = post_controller.search(request.form.get('text'), request.form.get('name'))
        return render_template('allpost.html', posts=posts)
    
    posts = post_controller.all_post()
    return render_template('allpost.html', posts=posts)
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
# from flask_restful import Api

# api = Api(app)
# api.add_resource(HelloWorld, '/api/hello', endpoint='hello_world')

if __name__ == '__main__':
    app.route(debug=True)