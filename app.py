from flask import Flask, request, render_template
app = Flask(__name__)
import json
import os

if not os.path.exists('data.json'):
    with open('data.json', 'w') as f:
        json.dump({}, f)
@app.route('/',methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        user=request.form['username']
        password=request.form['password']
        with open('data.json', 'r') as f:
            data = json.load(f)
        if user in data and data[user][0] == password:
            return render_template('base.html', username=user)
        else:
            print("INVALID USERNAME OR PASSWORD")
            return render_template('index.html', error="Invalid username or password")
    return render_template('index.html')

@app.route('/register',methods=['POST', 'GET'])
def register():
    if request.method=='POST':
        email=request.form['email']
        name=request.form['name']
        user=request.form['username']
        password=request.form['password']
        with open('data.json', 'r') as f:
            data = json.load(f)
        if user in data:
            return render_template('register.html', error="Username already exists")
        else:
            data[user] = [password, email, name]
            with open('data.json', 'w') as f:
                json.dump(data, f)
            return render_template('index.html', message="Registration successful, please login")
    return render_template('register.html')
if __name__ == '__main__':
    app.run(debug=True)
