from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class UpdateForm(FlaskForm):
  table = StringField('TABLE', validators=[DataRequired()])
  values = StringField('SET', validators=[DataRequired()])
  condition = StringField('WHERE', validators=[DataRequired()])
  submit = SubmitField('Start')
