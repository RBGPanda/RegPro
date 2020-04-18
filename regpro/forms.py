from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):

    username = StringField("Username", 
        validators=[DataRequired(), 
                    Length(min=3, max=20, message="Username must be between 3 and 20 characters")
                    ])
    
    password = PasswordField("Password", 
        validators=[DataRequired(), 
                    Length(min=3, max=20, message="Password must be between 3 and 20 characters")
                    ])

    submit = SubmitField("Create user account")


class LoginForm(FlaskForm):

    username = StringField("Username", 
        validators=[DataRequired(), 
                    Length(min=3, max=20, message="Invalid username")
                    ])
    
    password = PasswordField("Password", 
        validators=[DataRequired(), 
                    Length(min=3, max=20, message="Invalid password")
                    ])

    submit = SubmitField("Login")

class AddClass(FlaskForm):
    crn = StringField("CRN", validators=[DataRequired()])

    add = SubmitField("Add")

    drop = SubmitField("Drop")