from unicodedata import category
from market.models import User , Item
from flask import Flask, render_template, redirect, url_for , flash
from flask_sqlalchemy import SQLAlchemy
from market.forms import RegisterForm,LoginForm
from flask_login import LoginManager
from flask_login import login_user
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market2.db'
app.config['SECRET_KEY'] = '239kf389fj38f3j83j38'
db = SQLAlchemy(app)
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
login_manager = LoginManager()
@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/run')
def market_page():
    items = Item.query.all()
    return render_template("market.html", items = items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data,
                             email_address = form.email_address.data,
                             password=form.password1.data)
        
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    
    if form.errors !={}:
        for err_msg in form.errors.values():
            flash(f'There was an error of Creating: {err_msg}', category = 'danger')        
    return render_template('register.html',form=form)



@app.route('/login', methods=['GET','POST'] )
    
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.get(form.username.data)
        if attempted_user and  attempted_user.check_password_correct(attempted_password=form.password.data):    
           login_user(attempted_user)
           flash(f"Success! You  Login {attempted_user.username}", category='success')
           return redirect(url_for('market_page'))
        else:
           flash('Username or password not match!! Try again',category="danger")
    return render_template('login.html', form=form)