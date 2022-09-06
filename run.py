from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

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
