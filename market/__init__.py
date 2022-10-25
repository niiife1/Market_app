from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
SECRET_KEY = os.urandom(32)
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market2.db'
app.config['SECRET_KEY'] = SECRET_KEY
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
login_manager = LoginManager()
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from market import routes