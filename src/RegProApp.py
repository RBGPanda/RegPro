from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from Forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ef6e3f6a5a0954f0710993da4cd648c6'

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
    return render_template('login.html', page='Login', form=login_form)




if __name__ == "__main__":
    app.run(debug=True)