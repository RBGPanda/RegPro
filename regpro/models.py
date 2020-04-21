from regpro import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

courses = db.Table('courses',
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
    permissions = db.Column(db.String(), unique=False, nullable=False)
    courses = db.relationship('Course', secondary=courses, backref='users')

    def __repr__(self):
        return f"User('{self.permissions}' : {self.username}' : '{self.password}')"


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    crn = db.Column(db.String(5), unique=True, nullable=False)
    days = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(100), nullable=False)
    instructor = db.Column(db.String(100), unique=False, nullable=False)

    def __repr__(self):
        return f"User('{self.crn}' | {self.title}' : '{self.days}' '{self.time}')"