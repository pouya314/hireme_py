from decimal import Decimal


def any(submitted_answer, question):
    accepted = True
    error = None

    if not submitted_answer in question['accepted_answers']:
        accepted = False
        error = question['message_if_fail']

    return (accepted, error)


def equal(submitted_answer, question):
    accepted = True
    error = None

    if submitted_answer != question['accepted_answers'][0]:
        accepted = False
        error = question['message_if_fail']

    return (accepted, error)


def gte(submitted_answer, question):
    accepted = True
    error = None

    if Decimal(submitted_answer) < Decimal(question['accepted_answers'][0]):
        accepted = False
        error = question['message_if_fail']

    return (accepted, error)
