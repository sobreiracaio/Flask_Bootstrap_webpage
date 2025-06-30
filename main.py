from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug = True)