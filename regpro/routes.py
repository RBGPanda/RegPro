from flask import render_template, url_for, flash, redirect
from regpro import app
from regpro.forms import RegistrationForm, LoginForm
from regpro.models import User


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    registration_form = RegistrationForm()

    if registration_form.validate_on_submit():
        flash(f'Account created for {registration_form.username.data}', 'success')
        return redirect(url_for('home'))

    return render_template('signup.html', page='Sign-up', form=registration_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        return redirect(url_for('home'))

    return render_template('login.html', page='Login', form=login_form)