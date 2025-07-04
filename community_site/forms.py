from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from community_site.models import User
from flask_login import current_user


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
    
    
class FormEditProfile(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    profile_image = FileField('Update profile image', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    course1 = BooleanField('Course 1')
    course2 = BooleanField('Course 2')
    course3 = BooleanField('Course 3')
    course4 = BooleanField('Course 4')
    course5 = BooleanField('Course 5')
    course6 = BooleanField('Course 6')
    submit_button_edit_profile = SubmitField('Confirm Edit')
    
    def validate_email(self, email):
        if current_user.email != email.data:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("This email belongs to another account, try a different one.")
            
            
class FormCreatePost(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(2, 140)])
    body = TextAreaField('Contents', validators=[DataRequired()])
    submit_button_create_post = SubmitField ('Create Post')