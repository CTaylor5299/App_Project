from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
#from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@35.242.182.10/fpl"
app.config["SECRET_KEY"] = "asdasda"

db = SQLAlchemy(app)

from application import routes