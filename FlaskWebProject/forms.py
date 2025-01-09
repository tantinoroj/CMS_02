from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=150)])
    author = StringField('Author', validators=[DataRequired(), Length(min=1, max=75)])
    body = TextAreaField('Content', validators=[DataRequired(), Length(min=1, max=800)])
    image_path = FileField('Image', validators=[FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
    submit = SubmitField('Save')

