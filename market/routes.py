from market.__init__ import app
from flask import render_template, redirect, url_for
from market.models import Item, User
from market.forms import RegisterForm
from market import db
@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html")

@app.route('/run')
def market_page():
    items = Item.query.all()
    return render_template("market.html", items = items)

@app.route('/register')
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data,
                             email_address = form.email_address,
                             password=form.password1.data)
        
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    return render_template('register.html',form=form)

if __name__=="__run__":
    app.run(debug=True)