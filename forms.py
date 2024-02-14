from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class WelcomeForm(FlaskForm):
    """A form for user greeting"""

    name = StringField("Name", validators=[InputRequired()])
    submit = SubmitField("Send")


class TodoForm(FlaskForm):
    """A form for creating todo item"""

    title = StringField("Title", validators=[InputRequired()])
    submit = SubmitField("Add")
