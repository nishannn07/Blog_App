from model.models import User
from flask import abort, session
from app import db
from flask import flash, redirect, url_for

def register_user(form):
    # if User.query.filter_by(email=form.email.data).first()
    #     abort(400, 'Email is already in use')
    
    if User.userNameExits(form.username.data) and User.emailExits(form.email.data):
        abort(400, "Username or email already exits")
    new_user = User(username = form.username.data, email = form.email.data, password = form.password.data)
    db.session.add(new_user)
    db.session.commit()

def user_login(form):
    user = User.query.filter_by(email=form.email.data, password=form.password.data).first()
    if user is None: 
        flash("wrong email or password", "danger")
        return redirect(url_for('login'))
    else:
        session['id'] = user.id
        session['uname'] = user.username