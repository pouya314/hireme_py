from wtforms import StringField, SelectField
import mappings


def drop_down(question):
    return SelectField(
        u'Please Select', 
        validators=[mappings.Validations[v] for v in question['validations']],
        choices=[(option, option) for option in question['options']],
        render_kw={'class':'usa-select'}
    )


def text_field(question):
    return StringField(
        u'Your Answer Here',
        validators=[mappings.Validations[v] for v in question['validations']],
        default="",
        render_kw={'class':'usa-input'}
    )
