from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.form import RegistrationForm, LoginForm
from flaskblog.models import User, Post

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'test@gmail.com' and form.password.data == 'password':
            flash('You have been logged in.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', title='Register', form = form)
