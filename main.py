from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormLogin, FormCreateAccount


app = Flask(__name__)

users_list = ["Caio", "Ze", "Jão", "Manuel"]

app.config['SECRET_KEY'] = 'a1e4c51b5a440f3fbf1f3e96126a354a'


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
        flash(f"Account created successfully for email: {form_create_acc.email.data}", 'alert-success')
        return redirect(url_for('home'))
        
    return render_template('login.html', form_login=form_login, form_create_acc=form_create_acc)


if __name__ == '__main__':
    app.run(debug = True)