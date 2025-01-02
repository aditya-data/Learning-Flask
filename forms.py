from flask_wtf import FlaskForm #functionality of forms in Flask
from wtforms import (
    StringField,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField
)
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Optional,
    EqualTo
)

class SignupForm(FlaskForm):
    username = StringField(
        label="UserName",
        validators=[DataRequired(), Length(3, 30)]
    )
    email = StringField(
        label="Email",
        validators=[DataRequired(), Email()]
    )
    gender = SelectField(
        label="Gender",
        validators=[Optional()],
        choices=["Male", "Female", "Not Applicable"]
    )
    dob = DateField(
        label="Date of Birth",
        validators=[Optional()]
    )
    password = PasswordField(
        label="Password",
        validators=[DataRequired(), Length(2, 50)]

    )
    confirm_password = PasswordField(
        label="Confirm Password",
        validators=[DataRequired(), Length(2, 50), EqualTo("password")]
        
    )
    submit = SubmitField("Sign Up")




class LoginForm(FlaskForm): 
    email = StringField(
        label="Email",
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        label="Password",
        validators=[DataRequired(), Length(2, 50)]

    )
    remember_me = BooleanField(
        label="Remember Me"
    )
    submit = SubmitField("Login")