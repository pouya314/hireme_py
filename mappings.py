import constants
import validations
import conditions
import form_fields

Validations = {
    constants.VALIDATIONS_REQUIRED: validations.required,
    constants.VALIDATIONS_IS_STRING: validations.is_string,
    constants.VALIDATIONS_IS_DECIMAL: validations.is_decimal
}

Conditions = {
    constants.CONDITIONS_ANY: conditions.any,
    constants.CONDITIONS_EQUAL: conditions.equal,
    constants.CONDITIONS_GTE: conditions.gte
}

FieldTypes = {
    constants.QUESTION_TYPES_DROP_DOWN: form_fields.drop_down,
    constants.QUESTION_TYPES_TEXT_FIELD: form_fields.text_field,
    constants.QUESTION_TYPES_TEXT_AREA: form_fields.text_area,
}
