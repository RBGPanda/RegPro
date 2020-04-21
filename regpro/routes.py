from flask import render_template, url_for, flash, redirect
from regpro import app, db
from regpro.forms import RegistrationForm, LoginForm, CourseRegistrationForm, ChangePermissions
from regpro.models import User, Course, courses
from flask_login import login_user, current_user, logout_user


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/changePermissions', methods=['GET', 'POST'])
def changePermissions():
    users = User.query.all()
    form = ChangePermissions()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        user.permissions = form.permissions.data
        db.session.commit()
        return redirect(url_for('administrator'))
    return render_template('changePermissions.html', page='change-permissions', form=form, users=users)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data, permissions=form.permissions.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('administrator'))

    return render_template('signup.html', page='Sign-up', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        password = form.password.data
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                login_user(user)
                return redirect(url_for(user.permissions))
            else:
                flash(f'Incorrect password', 'danger')
                form.password.data = ''
        else:
            flash(f'Invalid username', 'danger')
            form.username.data = ''

    return render_template('login.html', page='Login', form=form)


@app.route('/student')
def student():
    courses = current_user.username
    return render_template('student.html', page='Student', courses=courses)


@app.route('/administrator')
def administrator():
    return render_template('administrator.html', page='Administrator')


@app.route('/coursemanager', methods=['GET', 'POST'])
def coursemanager():
    form = CourseRegistrationForm()
    courses = Course.query.all()
    if form.validate_on_submit():
        current_courses = current_user.courses
        if form.add.data:
            course_added = Course.query.filter_by(crn=form.crn.data).first()
            if course_added:
                current_user.courses.append(course_added)
                db.session.commit()
        elif form.drop.data:
            course_dropped = Course.query.filter_by(crn=form.crn.data).first()
            if course_dropped:
                current_user.courses.remove(course_dropped)
                db.session.commit()
        form.crn.data = ''
    return render_template('coursemanager.html',  page='Course Manager', form=form, courses=courses)


@app.route('/logout')
def logout():
    logout_user()
    return render_template('home.html')




@app.route('/Instructor')
def Instructor():
    user = currUser
    return render_template('Instructor.html', stu = user)

@app.route('/InstructorClass')
def InstructorClass():
    user = currUser
    return render_template('InstructorClass.html', stu = user)


@app.route('/Advisor')
def Advisor():
    user = currUser
    return render_template('Advisor.html', stu = user)

@app.route('/AdvisorStudent')
def AdvisorStudent():
    user = currUser
    return render_template('AdvisorStudent.html', stu = user)

@app.route('/Admin')
def Admin():
    user = currUser
    return render_template('Admin.html', stu = user)