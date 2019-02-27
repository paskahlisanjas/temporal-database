from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class UpdateForm(FlaskForm):
  update = StringField('UPDATE', validators=[DataRequired()])
  submit = SubmitField('Start')

class DeleteForm(FlaskForm):
  delete = StringField('DELETE', validators=[DataRequired()])
  submit = SubmitField('Start')

  