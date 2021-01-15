from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class LoveLetter(FlaskForm):
    sender = StringField('Sender', validators=[DataRequired()])
    to = StringField('Recipient', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField("Ship It!")
    cancel = SubmitField("Cancel")
