from flask import render_template, redirect, url_for, request, flash
from community_site import app, database, bcrypt
from community_site.forms import FormLogin, FormCreateAccount
from community_site.models import User



users_list = ["Caio", "Ze", "Jão", "Manuel"]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/users')
def users():
    return render_template('users.html', users_list = users_list)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_create_acc = FormCreateAccount()
    
    if form_login.validate_on_submit() and 'submit_button_login' in request.form:
        flash(f"Login successfully done on email: {form_login.email.data}!", 'alert-success')
        return redirect(url_for('home'))
        
    if form_create_acc.validate_on_submit() and 'submit_button_create_acc' in request.form :
        crypt_pass = bcrypt.generate_password_hash(form_create_acc.password.data)
        user = User(username=form_create_acc.username.data, email=form_create_acc.email.data, password= crypt_pass) #create user
        database.session.add(user) #add a session
        database.session.commit() #commit session
        flash(f"Account created successfully for email: {form_create_acc.email.data}", 'alert-success')
        return redirect(url_for('home'))
        
    return render_template('login.html', form_login=form_login, form_create_acc=form_create_acc)
