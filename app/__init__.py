from flask import Flask
from app.routes import routes

def create_app():
	app = Flask(__name__)
	app.register_blueprint(routes,url_prefix = "/")

	return app