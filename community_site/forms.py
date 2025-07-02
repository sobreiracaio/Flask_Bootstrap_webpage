from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from community_site.models import User


class FormCreateAccount(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
    pass_confirm = PasswordField('Password confirmation', validators=[DataRequired(), EqualTo('password')])
    submit_button_create_acc = SubmitField('Create Account')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("This email belongs to another account, try a different one or login.")
            
    

class FormLogin(FlaskForm):
    
    email = StringField('E-mail', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
    remember_me = BooleanField('Remember me')
    submit_button_login = SubmitField('Login')