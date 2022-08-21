from os import abort
from flask import Flask, render_template


app = Flask(__name__)\
    
@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/market')
def market_page():
    items = [
        {"id":1, "name":"Iphone- 13 pro MaX", "barcode":"566595929595678", "price": "1400$"},
        {"id":2, "name":"Acer-Aspire 5", "barcode":"85455655656785", "price": "1899$"},
        {"id":3, "name":"Keyboard-Razer mamba", "barcode":"566595929595678", "price": "140$"}     
    ]
    return render_template("market.html", items = items )
