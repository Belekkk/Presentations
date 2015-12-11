import cgi
from flask import render_template, abort, request
from jinja2 import TemplateNotFound
from twilio import twiml
from twilio.rest import TwilioRestClient
from app import app, redis_db, socketio
 
TWILIO_ACCOUNT_SID = app.config['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = app.config['TWILIO_AUTH_TOKEN']
TWILIO_NUMBER = app.config['TWILIO_NUMBER']
 
client = TwilioRestClient(account=TWILIO_ACCOUNT_SID,
						  token=TWILIO_AUTH_TOKEN)
 
@app.route('/<presentation_name>/', methods=['GET'])
def landing(presentation_name):
    try:
        return render_template(presentation_name + '.html', telephone=TWILIO_NUMBER)
    except TemplateNotFound:
        abort(404)
 
@app.route('/presentation/twilio/webhook/', methods=['POST'])
def twilio_callback():
    to = request.form.get('To', '')
    from_ = request.form.get('From', '')
    message = request.form.get('Body', '').lower()
    if to == TWILIO_NUMBER:
        redis_db.incr(cgi.escape(message))
        socketio.emit('msg', {'div': cgi.escape(message),
                              'val': redis_db.get(message)},
                               namespace='/presentation')
    #resp = twiml.Response()
    #resp.message('Merci/Cheers.')
    return str(resp)