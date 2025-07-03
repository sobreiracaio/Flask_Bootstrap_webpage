from flask import render_template, redirect, url_for, request, flash
from community_site import app, database, bcrypt
from community_site.forms import FormLogin, FormCreateAccount, FormEditProfile
from community_site.models import User
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image


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
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
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
    profile_image = url_for('static', filename = 'images/{}'.format(current_user.profile_photo))
    return render_template("profile.html", profile_photo = profile_image)


@app.route('/post/create')
@login_required
def post_create():
    return render_template("post_create.html")


def save_img(image):
    code = secrets.token_hex(8)
    file_name, extension = os.path.splitext(image.filename)
    new_file_name = file_name + code + extension
    full_path = os.path.join(app.root_path, 'static/images/' + new_file_name)
    img_size = (200, 200)
    resized_img = Image.open(image)
    resized_img.thumbnail(img_size)
    resized_img.save(full_path)
        
    return new_file_name

@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def profile_edit():
    form_edit_profile = FormEditProfile()
    if form_edit_profile.validate_on_submit():
        current_user.email = form_edit_profile.email.data
        current_user.username = form_edit_profile.username.data
        if form_edit_profile.profile_image:
            image_name = save_img(form_edit_profile.profile_image.data)
            current_user.profile_photo = image_name
        database.session.commit()
        flash(f"Profile successfully updated!", 'alert-success')
        return (redirect(url_for('profile')))
    elif request.method == 'GET':
        form_edit_profile.email.data = current_user.email
        form_edit_profile.username.data = current_user.username
        
    
    profile_image = url_for('static', filename = 'images/{}'.format(current_user.profile_photo))
    return render_template('profile_edit.html', profile_photo = profile_image, form_edit_profile = form_edit_profile)