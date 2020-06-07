from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, SelectField

import mappings



class BaseForm(FlaskForm):
    uuid = HiddenField('UUID')
    submit = SubmitField('Submit')


def field_for(question, with_label=False):
    field = mappings.FieldTypes[question['question_type']]
    return field(question, question['body']) if with_label else field(question)


def form_for(question):
    setattr(BaseForm, 'answer', field_for(question))
    return BaseForm()


def form_for_application(questions):
    for idx, question in enumerate(questions):
        setattr(BaseForm, 'q{}'.format(idx+1), field_for(question, with_label=True))
    setattr(BaseForm, 'accepted_bits', HiddenField())
    return BaseForm()
