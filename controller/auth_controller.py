from model.models import User, Token
from flask import abort, session
from app import db
from flask import flash, redirect, url_for, current_app
from flask_mailman import EmailMessage
import random

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

def get_user_id_by_reset_token(token):
    try:
        token_obj = Token.query.filter_by(token=int(token)).first()
        user_id = token_obj.user_id
    except (ValueError, TypeError, AttributeError):
        user_id = None
    
    return user_id

def send_password_reset_email(email):
    if '@' not in email:
        flash("Invalid email format!", "warning")
    
    user = User.query.filter_by(email = email).first()
    if not user:
        flash("No such user with this Email", "warning")
    else: 
        random_token=random.randrange(12123, 99429)
        new_token = Token(user_id=user.id, token=random_token)
        db.session.add(new_token)
        db.session.commit()

        msg = EmailMessage(
            subject='Password Reset Request',
            body=f'''To reset your password, visit the following link:
    {url_for('reset_token', token=new_token.token, _external=True)}
    ''',
            from_email=current_app.config['MAIL_USERNAME'],
            to=[user.email]
        )
        msg.send()
        flash('Check your Mail', 'info')
