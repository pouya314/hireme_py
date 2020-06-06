from flask import Flask, render_template, request, jsonify

from forms import form_for
from questions_controller import all_questions, question_with_uuid, first_question, question_after
import acceptance_check



app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'



@app.route('/', methods=['GET'])
def landing_page():
    return render_template('landing_page.html')


@app.route('/start_eligibility_test', methods=['GET'])
def start_eligibility_test():
    fq = first_question()

    form = form_for(fq)

    return render_template(
        'eligibility_test.html', 
        form=form, 
        question=fq['body'],
        uuid=fq['uuid']
    )


def question_answer_str(q, a):
    return '{} -> {}'.format(q['body'], a)


@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    """
    Respond to ajax form submission.
    """
    import time; time.sleep(2)  # TODO: REMOVE ME!

    resp = {}

    curr_q = question_with_uuid(request.form['uuid'])

    # Check for form validation errors
    form = form_for(curr_q)
    if not form.validate_on_submit():
        resp['status'] = 'error'
        resp['payload'] = render_template('validation_error.html', msg=', '.join(form.answer.errors))
        return jsonify(resp)

    # Check if acceptance condition is met
    supplied_answer = form.answer.data
    accepted, err = acceptance_check.validate(supplied_answer, curr_q)
    if not accepted:
        resp['status'] = 'fail'
        resp['payload'] = render_template('condition_error.html', val=question_answer_str(curr_q, supplied_answer), msg=err)
        return jsonify(resp)

    next_question = question_after(curr_q)
    if not next_question:
        return 'You have reached the last question'

    # All good, go to next question
    next_form = form_for(next_question)
    resp['status'] = 'success'
    resp['accepted'] = render_template('success.html', val=question_answer_str(curr_q, supplied_answer))
    resp['payload'] = render_template('form.html', form=next_form, question=next_question['body'], uuid=next_question['uuid'])
    return jsonify(resp)




if __name__ == '__main__':
    app.run()


