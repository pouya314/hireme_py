from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, SelectField
import mappings



class BaseForm(FlaskForm):
    uuid = HiddenField('UUID')
    submit = SubmitField('Submit')


def answer_field_for(question):
    return mappings.FieldTypes[question['question_type']](question)


def form_for(question):
    setattr(BaseForm, 'answer', answer_field_for(question))
    return BaseForm()
