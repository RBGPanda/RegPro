from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from regpro.models import User

class ChangePermissions(FlaskForm):

    permissions = SelectField("Permissions", 
        choices=[("student", "Student"), ("instructor", "Instructor"), ("advisor", "Advisor"), ("administrator", "Administrator")],
        default=1,
        coerce=str)

    username = StringField("Username", 
        validators=[DataRequired(), 
                    Length(min=1, max=20, message="Username must be between 3 and 20 characters")
                    ])

    submit = SubmitField("Change Permission")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user:
            raise ValidationError("Username does not exist")


class RegistrationForm(FlaskForm):

    permissions = SelectField("Permissions", 
        choices=[("student", "Student"), ("instructor", "Instructor"), ("advisor", "Advisor"), ("administrator", "Administrator")],
        default=1,
        coerce=str)

    username = StringField("Username", 
        validators=[DataRequired(), 
                    Length(min=1, max=20, message="Username must be between 3 and 20 characters")
                    ])
    
    password = StringField("Password",
        validators=[DataRequired(),        
                    Length(min=1, max=20, message="Password must be between 3 and 20 characters")
                    ])

    submit = SubmitField("Create user account")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already exists")


class LoginForm(FlaskForm):

    username = StringField("Username", 
        validators=[DataRequired(), 
                    Length(min=3, max=20, message="Invalid username")
                    ])
    
    password = StringField("Password", 
        validators=[DataRequired(), 
                    Length(min=3, max=20, message="Invalid password")
                    ])

    submit = SubmitField("Login")


class CourseRegistrationForm(FlaskForm):

    crn = StringField("CRN", validators=[DataRequired()])

    add = SubmitField("Add")

    drop = SubmitField("Drop")


class editCourseTime(FlaskForm):
    
    coursename = StringField("Course Name", validators=[DataRequired()])

    newday = StringField("Days", validators=[DataRequired()])

    newtime = StringField("Times", validators=[DataRequired()])

    submit = SubmitField("Submit")




