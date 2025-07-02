<h1>1.Clone the Repository</h1>

```
git clone https://github.com/abhijeetkumar097/Blog.git
```

<div style="color:lightgreen;">Go inside the folder </div></br>

<h1>2.Set Up Virtual Environment </h1>

```
python -m venv venv
```

<div style="color:green;font-size:20px;">#On Windows</div>

```
venv\Scripts\activate
```

<div style="color:green;font-size:20px;"># On macOS/Linux</div>

```
source venv/bin/activate
```

<h1>Install Required Packages</h1>

```
pip install -r requirements.txt
```

<h1>4. Set Up config.py</h1>

<div style="padding:30px">
<div>MAIL_USERNAME = 'your_email@example.com'</div>
<div>MAIL_PASSWORD = 'your_app_password'</div>
</div>

<h1>5. Set Up the Database</h1>

```
flask db init            
```

```
flask db migrate -m "Initial migration"
```

```
flask db upgrade
```

<h1>6. Run the App</h1>

```
flask run
```