from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class UpdateForm(FlaskForm):
  update = StringField('UPDATE', validators=[DataRequired()])
  submit = SubmitField('Start')

class UnionForm(FlaskForm):
  select1 = StringField('Select 1', validators=[DataRequired()])
  table1 = StringField('Table 1', validators=[DataRequired()])
  select2 = StringField('Select 2', validators=[DataRequired()])
  table2 = StringField('Table 2', validators=[DataRequired()])
  submit = SubmitField('Start')