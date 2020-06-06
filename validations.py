from wtforms.validators import ValidationError
from decimal import Decimal


def required(form, field):
    if not field.data:
        raise ValidationError('Field is required.')


def is_string(form, field):
    try:
        str(field.data)
    except Exception as e:
        raise ValidationError('Field must be a String.')


def is_decimal(form, field):
    try:
        Decimal(field.data)
    except Exception as e:
        raise ValidationError('Field must be a decimal.')
