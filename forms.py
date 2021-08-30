from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField

class AddFilterForm(FlaskForm):
    fsymbol = StringField('Symbol')
    charttype = StringField('Chart_Type')
    submit = SubmitField('Proceed')