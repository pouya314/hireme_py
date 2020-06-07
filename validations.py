from wtforms.validators import ValidationError
from decimal import Decimal


def required(form, field):
    if not field.data:
        raise ValidationError('Required.')


def is_string(form, field):
    try:
        str(field.data)
    except Exception as e:
        raise ValidationError('Must be a String.')


def is_decimal(form, field):
    try:
        Decimal(field.data)
    except Exception as e:
        raise ValidationError('Must be decimal.')
