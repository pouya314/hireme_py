import mappings


def validate(submitted_answer, question):
    return mappings.Conditions[question['condition']](submitted_answer, question)