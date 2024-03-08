from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, TextAreaField
from wtforms.validators import Email, InputRequired


class SendMailForm(FlaskForm):
    recipient = StringField("Email", validators=[InputRequired(), Email()])
    subject = StringField("Subject", validators=[InputRequired()])
    content = TextAreaField("Content", validators=[InputRequired()])
    save_to_sent_items = BooleanField(
        "Save this email to Sent folder on the server?", default=False
    )
    submit = SubmitField("Send")


class SendTaskForm(FlaskForm):
    title = StringField("title", validators=[InputRequired()])
    submit = SubmitField("Send")
