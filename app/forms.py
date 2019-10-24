'''
class for holding info for the input form on the /index page
'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    '''
    class for holding info for the query form on the /index page
    '''
    expense = StringField('Expense', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    submit = SubmitField('Input')