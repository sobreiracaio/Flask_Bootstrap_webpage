from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)


app.config['SECRET_KEY'] = 'a1e4c51b5a440f3fbf1f3e96126a354a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from community_site import routes