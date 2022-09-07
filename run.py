from market.models import User , Item
from flask import Flask, render_template, redirect, url_for , flash
from flask_sqlalchemy import SQLAlchemy
from market.forms import RegisterForm
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market2.db'
app.config['SECRET_KEY'] = '239kf389fj38f3j83j38'
db = SQLAlchemy(app)
    
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
                             password_defense=form.password1.data)
        
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    
    if form.errors !={}:
        for err_msg in form.errors.values():
            flash(f'There was an error of Creating: {err_msg}', category = 'danger')        
    return render_template('register.html',form=form)

if __name__=="__run__":
    app.run(debug=True)