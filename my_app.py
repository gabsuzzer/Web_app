from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c1403fbf4154af61385992b20752e790'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

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
    if form.validate_on_submit():
        flash(f'Acount created for { form.username.data}!', 'sucess')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)

if __name__ == "__main__":
    app.run(debug=True)
