from wtforms import StringField, SelectField, TextAreaField
import mappings


def drop_down(question, label=None):
    return SelectField(
        label if label else u'Please Select',
        validators=[mappings.Validations[v] for v in question['validations']],
        choices=[(option, option) for option in question['options']],
        render_kw={'class': 'usa-select'}
    )


def text_field(question, label=None):
    return StringField(
        label if label else u'Your Answer Here',
        validators=[mappings.Validations[v] for v in question['validations']],
        default="",
        render_kw={'class': 'usa-input'}
    )


def text_area(question, label=None):
    return TextAreaField(
        label if label else u'Your Answer Here',
        validators=[mappings.Validations[v] for v in question['validations']],
        default="",
        render_kw={'class': 'usa-textarea'}
    )
