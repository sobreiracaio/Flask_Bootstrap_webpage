from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormCreateAccount(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
    pass_confirm = PasswordField('Password confirmation', validators=[DataRequired(), EqualTo('password')])
    submit_button_create_acc = SubmitField('Create Account')
    

class FormLogin(FlaskForm):
    
    email = StringField('E-mail', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
    remember_me = BooleanField('Remember me')
    submit_button_login = SubmitField('Login')