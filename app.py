import os

from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message

import acceptance_check
from forms import form_for, form_for_application
from questions_controller import (
    question_with_uuid, first_question,
    question_after, all_application_questions)
from utils import str_to_bool

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['MAIL_SERVER'] = os.environ['MAIL_SERVER']
app.config['MAIL_PORT'] = int(os.environ['MAIL_PORT'])
app.config['MAIL_USE_TLS'] = str_to_bool(os.environ['MAIL_USE_TLS'])
app.config['MAIL_USE_SSL'] = str_to_bool(os.environ['MAIL_USE_SSL'])
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']

mail = Mail(app)


@app.route('/hireme', methods=['GET'])
def landing_page():
    return render_template('landing_page.html')


@app.route('/hireme/eligibility_test', methods=['GET'])
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


@app.route('/hireme/submit_answer', methods=['POST'])
def submit_answer():
    """
    Respond to ajax form submission.
    """
    resp = {}

    curr_q = question_with_uuid(request.form['uuid'])

    # Check for form validation errors
    form = form_for(curr_q)
    if not form.validate_on_submit():
        resp['status'] = 'error'
        resp['payload'] = form.errors
        return jsonify(resp)

    # Check if acceptance condition is met
    supplied_answer = form.answer.data
    accepted, err = acceptance_check.validate(supplied_answer, curr_q)
    if not accepted:
        resp['status'] = 'fail'
        resp['payload'] = render_template('fail.html',
                                          val=question_answer_str(curr_q, supplied_answer), msg=err)
        return jsonify(resp)

    next_question = question_after(curr_q)
    if next_question:
        # All good, go to next question
        next_form = form_for(next_question)
        resp['status'] = 'success'
        resp['accepted'] = render_template('success.html',
                                           val=question_answer_str(curr_q, supplied_answer))
        resp['payload'] = render_template('form.html', form=next_form,
                                          question=next_question['body'], uuid=next_question['uuid'])
        return jsonify(resp)

    # End of eligibility, now serve the application form
    application_questions = all_application_questions()
    application_form = form_for_application(application_questions)
    resp['status'] = 'success'
    resp['accepted'] = render_template('success.html',
                                       val=question_answer_str(curr_q, supplied_answer))
    resp['payload'] = render_template('application_form.html', form=application_form,
                                      fields=['q{}'.format(i + 1) for i in range(len(application_questions))])
    return jsonify(resp)


@app.route('/hireme/submit_application', methods=['POST'])
def submit_application():
    resp = {}

    application_form = form_for_application(all_application_questions())
    if not application_form.validate_on_submit():
        resp['status'] = 'error'
        resp['payload'] = application_form.errors
        return jsonify(resp)

    # Send email to self
    msg = Message('New Job Opportunity Alert',
                  sender=os.environ['MAIL_SENDER'],
                  recipients=[os.environ['MAIL_RECEIVER']])

    eligibility_lines = application_form.accepted_bits.data
    msg_body = eligibility_lines + '\n'

    for idx, q in enumerate(all_application_questions()):
        msg_body += q['body']
        msg_body += '\n'
        msg_body += getattr(application_form, 'q{}'.format(idx + 1)).data
        msg_body += '\n'

    msg.body = msg_body

    with app.app_context():
        mail.send(msg)

    resp['status'] = 'success'
    resp['accepted'] = None
    resp['payload'] = render_template('success.html',
                                      val='Your application has been submitted successfuly. Thank you!')
    return jsonify(resp)

# if __name__ == '__main__':
#     app.run()
