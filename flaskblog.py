from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author':'abc',
        'title': 'blog 1',
        'content':'this is first blog',
        'date_posted':'May 20,2018'
    },
    {
        'author':'xyz',
        'title': 'blog 2',
        'content':'this is second blog',
        'date_posted':'May 21,2018'
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)