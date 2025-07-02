from flask import render_template, redirect, url_for, request, flash
from community_site import app, database, bcrypt
from community_site.forms import FormLogin, FormCreateAccount
from community_site.models import User
from flask_login import login_user, logout_user, current_user, login_required



users_list = ["Caio", "Ze", "Jão", "Manuel"]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/users')
@login_required
def users():
    return render_template('users.html', users_list = users_list)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_create_acc = FormCreateAccount()
    
    if form_login.validate_on_submit() and 'submit_button_login' in request.form:
        user = User.query.filter_by(email=form_login.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form_login.password.data):
            login_user(user, remember= form_login.remember_me)
            flash(f"Login successfully done on email: {form_login.email.data}!", 'alert-success')
            return redirect(url_for('home'))
        else:
            flash(f"Error logging in, check e-mail and password!", 'alert-danger')
            
        
    if form_create_acc.validate_on_submit() and 'submit_button_create_acc' in request.form :
        crypt_pass = bcrypt.generate_password_hash(form_create_acc.password.data)
        user = User(username=form_create_acc.username.data, email=form_create_acc.email.data, password= crypt_pass) #create user
        database.session.add(user) #add a session
        database.session.commit() #commit session
        flash(f"Account created successfully for email: {form_create_acc.email.data}", 'alert-success')
        return redirect(url_for('home'))
        
    return render_template('login.html', form_login=form_login, form_create_acc=form_create_acc)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(f"Logout successfully done!", 'alert-success')
    return redirect (url_for('home'))

@app.route('/profile')
@login_required
def profile():
    return render_template("profile.html")


@app.route('/post/create')
@login_required
def post_create():
    return render_template("post_create.html")