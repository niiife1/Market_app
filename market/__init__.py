from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
SECRET_KEY = os.urandom(32)
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market2.db'
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
