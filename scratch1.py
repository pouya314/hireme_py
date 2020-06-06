# QUESTIONS = [
#     {
#         'question_type': 'drop_down',
#         'position': 1,
#         'body': "In which country is this job located?",
#         'option_set': ['Australia (Melbourne)', 'Sweden', 'United States', 'Other'],
#         'acceptance_criterion': 'any',
#         'accepted_answers': ['Australia (Melbourne)', 'Sweden', 'United States'],
#         'message_if_fail': 'Sorry but the location of this job does not suit me.'
#     },
#     {
#         'question_type': 'drop_down',
#         'position': 2,
#         'body': "Heavy JS?",
#         'option_set': ['Yes', 'No'],
#         'acceptance_criterion': 'equal',
#         'accepted_answers': ['No'],
#         'message_if_fail': 'I hate JS.'
#     },
# ]


# class Question(object):
#     BASE_FIELDS = ['position', 'body', 'message_if_fail']

#     def __init__(self, **kwargs):
#         for field in self.BASE_FIELDS:
#             assert field in kwargs, '{} is required but not in the params dict'.format(field)
#             setattr(self, field, kwargs[field])


# class DropDownQuestion(Question):
#     FIELDS = ['option_set', 'acceptance_criterion', 'accepted_answers']
#     AVAILABLE_ACCEPTANCE_CRITERIA = ['any']

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         for field in self.FIELDS:
#             assert field in kwargs, '{} is required but not in the params dict'.format(field)
#             setattr(self, field, kwargs[field])

#     def validate(self, answer):
#         if self.acceptance_criterion == 'any':
#             return answer in self.accepted_answers
#         elif self.acceptance_criterion == 'equal':
#             return answer == self.accepted_answers
#         else:
#             raise Exception('Unknown acceptance_criterion.')

#     def answer_prompt(self):
#         print(self.option_set)
#         return input("Answer: ")


# QUESTION_TYPE_MAPPING = {
#     'drop_down': DropDownQuestion
# }

# for q in QUESTIONS:
#     x = QUESTION_TYPE_MAPPING[q['question_type']](**q)
#     print(x.body)
#     answer = x.answer_prompt()
#     if x.validate(answer):
#         print('Cool, Next question')
#     else:
#         print(x.message_if_fail)
