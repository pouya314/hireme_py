import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper



def all_application_questions():
    return sorted(yaml.load(open("application.yml", "r").read(), Loader=Loader), 
        key=lambda question: question['position'])


def all_questions():
    return sorted(yaml.load(open("questions.yml", "r").read(), Loader=Loader), 
        key=lambda question: question['position'])


def idx_question_by_uuid(uuid):
    found = [
        (idx, question_dict) 
        for idx, question_dict in enumerate(all_questions()) 
        if str(uuid) == question_dict['uuid']
    ]
    assert len(found) == 1, "Error: Could not find the question by the UUID given."
    return found.pop()


def question_with_uuid(uuid):
    _, q = idx_question_by_uuid(uuid)
    return q


def first_question():
    return all_questions()[0]


def question_after(curr_q):
    idx, q = idx_question_by_uuid(curr_q['uuid'])
    try:
        return all_questions()[idx+1]
    except Exception as e:
        return None
