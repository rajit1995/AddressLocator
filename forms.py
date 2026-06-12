from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    submit = SubmitField('Submit')
    

class ReturnToHome(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    submit = SubmitField('Click Here')
    

class OpenMap(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    submit = SubmitField('Map')
    
    
class ReturnToData(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    submit = SubmitField('Back')    
    
    

