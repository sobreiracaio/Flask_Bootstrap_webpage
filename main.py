from flask import Flask, render_template, url_for
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

@app.route('/login')
def login():
    form_login = FormLogin()
    form_create_acc = FormCreateAccount()
    return render_template('login.html', form_login=form_login, form_create_acc=form_create_acc)


if __name__ == '__main__':
    app.run(debug = True)