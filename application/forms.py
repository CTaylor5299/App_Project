from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PlayersForm(FlaskForm):
    name = StringField('Name of Player', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    team = StringField('Team', validators=[DataRequired()])
    submit = SubmitField('Add player')

class TeamForm(FlaskForm):
    team_name = StringField('Name of Team', validators=[DataRequired()])
    owner = StringField('Name of Owner', validators=[DataRequired()])
    submit = SubmitField('Done') 