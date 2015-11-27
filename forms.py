from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class SignupForm(Form):
	first_name = StringField('First name', validators=[DataRequired("Please enter first name!")])
	last_name = StringField('Last name', validators=[DataRequired("Please enter email address")])
	email = StringField('Email', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Sign up') 
