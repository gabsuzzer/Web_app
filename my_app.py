from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c1403fbf4154af61385992b20752e790'

posts = [
    {
        'name': 'Victor Jalmar',
        'title': 'Updates for thursday',
        'content' : 'I have finally, taken breakfast and woken up',
        'date_posted': 'Jan 4 2024'
    },

    {
        'name': 'Tina Amisa',
        'title': 'Yaaay',
        'content' : "I'm here too",
        'date_posted': 'Apr 29 2017'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', main_posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'about')

@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.is_submitted():
        flash(f'Acount created for { form.username.data}!', 'sucess')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)

if __name__ == "__main__":
    app.run(debug=True)
