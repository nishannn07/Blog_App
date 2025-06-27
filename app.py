import os
import json
from flask import Flask, request, render_template, flash, redirect, url_for

from models.base import Base, engine
from routes.post_routes import post_bp

app = Flask(__name__)
app.secret_key = os.urandom(24)

DATA_FILE = 'data.json'
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({}, f)

app.register_blueprint(post_bp)
import models.post
import models.user
import models.tag
import models.association
Base.metadata.create_all(engine)


@app.route('/', methods=['POST', 'GET'])
def index():
    """Handles user login using the JSON file."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open(DATA_FILE, 'r') as f:
            users = json.load(f)
        user_data = users.get(username)
        if user_data and user_data[0] == password:
            flash('Login successful!', 'success')
            return render_template('base.html', username=username)
        else:
            flash('Invalid username or password', 'danger')
            return render_template('index.html')
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    """Handles new user registration using the JSON file."""
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']

        with open(DATA_FILE, 'r') as f:
            users = json.load(f)

        if username in users:
            flash('Username already exists', 'danger')
            return render_template('register.html')
        
        users[username] = [password, email, name]
        
        with open(DATA_FILE, 'w') as f:
            json.dump(users, f, indent=4)

        flash('Registration successful, please login.', 'success')
        return redirect(url_for('index'))
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)