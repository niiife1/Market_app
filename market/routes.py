from market.__init__ import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm

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
    return render_template('register.html',form=form)

if __name__=="__run__":
    app.run(debug=True)