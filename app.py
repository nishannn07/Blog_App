from flask import Flask
from routes.post_routes import bost_bp
app.register_blueprint(bost_bp)