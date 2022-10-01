import imp
from market.__init__ import db, login_manager
from market import bcrypt

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class User(db.Model):
    number = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=70), nullable=False, unique=True)
    password_defense = db.Column(db.String(length=60), nullable=False)
    budge =db.Column (db.Integer(), nullable=False, default=10000)
    items = db.relationship('Item', backref="owned_user", lazy=True)
    
    
    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_defense = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    def check_password_correct(self,  attempted_password):
        if bcrypt.check_password_hash(self.password_hash, attempted_password):
            return True
    
class Item(db.Model):
    number = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=150), nullable=False, unique=True )
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=15), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(),db.ForeignKey('user.number'))
    
    def __repr__(self):
        return f"Item{self.name}"