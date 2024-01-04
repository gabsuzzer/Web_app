from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
