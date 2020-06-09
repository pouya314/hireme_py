from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, SelectField

from questions_controller import all_application_questions
import mappings


class BaseForm(FlaskForm):
    uuid = HiddenField('UUID')
    submit = SubmitField('Submit')


def field_for(question, with_label=False):
    field = mappings.FieldTypes[question['question_type']]
    return field(question, question['body']) if with_label else field(question)


def form_for(question):
    setattr(BaseForm, 'answer', field_for(question))

    f = BaseForm()

    # Shitfuckery to get around the weird behavior of WTforms.
    # For some reason, it keeps fields from previous submitted form!
    for idx, q in enumerate(all_application_questions()):
        att = 'q{}'.format(idx+1)
        if hasattr(f, att):
            delattr(f, att)
    if hasattr(f, 'accepted_bits'):
        delattr(f, 'accepted_bits')

    return f


def form_for_application(questions):
    for idx, question in enumerate(questions):
        setattr(BaseForm, 'q{}'.format(idx+1),
                field_for(question, with_label=True))
    setattr(BaseForm, 'accepted_bits', HiddenField())

    a_form = BaseForm()

    # Shitfuckery to get around the weird behavior of WTforms.
    # For some reason, it keeps fields from previous submitted form!
    if hasattr(a_form, 'answer'):
        delattr(a_form, 'answer')

    return a_form
