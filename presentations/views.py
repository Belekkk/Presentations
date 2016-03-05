import cgi
from flask import render_template, abort, request
from jinja2 import TemplateNotFound
from twilio.rest import TwilioRestClient

from . import app, redis_db, socketio

TWILIO_ACCOUNT_SID = app.config['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = app.config['TWILIO_AUTH_TOKEN']
TWILIO_NUMBER = app.config['TWILIO_NUMBER']

client = TwilioRestClient(account=TWILIO_ACCOUNT_SID, token=TWILIO_AUTH_TOKEN)


@app.route('/<presentation_name>/', methods=['GET'])
def landing(presentation_name):
    try:
        return render_template(presentation_name + '.html',
                               telephone=TWILIO_NUMBER)
    except TemplateNotFound:
        abort(404)


@app.route('/presentation/twilio/webhook/', methods=['POST'])
def twilio_callback():
    to = request.form.get('To', '')
    from_ = request.form.get('From', '')
    message = request.form.get('Body', '').lower()
    print('{0} received from {1}'.format(message, from_))
    count = redis_db.incr(cgi.escape(message))
    print('{0} : {1}'.format(message, count))
    socketio.emit('msg', {'div': message,
                          'val': count},
                  namespace='/presentation')
    return 'Message received'
