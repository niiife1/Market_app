from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, SubmitField

class RegisterFrom (FlaskForm):
    username = StringField(label='username')
    email_address = StringField(label='email')
    password1 = PasswordField(label='Password1')
    password2 = PasswordField(label='Password2')
    submit = SubmitField(label='submit')