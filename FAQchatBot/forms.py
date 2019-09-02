from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FAQform(FlaskForm):
    Question = StringField('Question', validators=[DataRequired()])
    Answer = StringField('Answer', validators=[DataRequired()])
    submit = SubmitField('Add')