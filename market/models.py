from market.__init__ import db

class User(db.Model):
    number = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=70), nullable=False, unique=True)
    password_defense = db.Column(db.String(length=60), nullable=False)
    budge =db.Column (db.Integer(), nullable=False, default=10000)
    items = db.relationship('Item', backref="owned_user", lazy=True)
    
    
class Item(db.Model):
    number = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=150), nullable=False, unique=True )
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=15), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(),db.ForeignKey('user.number'))
    
    def __repr__(self):
        return f"Item{self.name}"