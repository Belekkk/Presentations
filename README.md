# Presentations

## List

- [CMI - 14/03/2016](presentations/static/content/cmi/slides.md)

## Required

- `pip install -r requirements.txt`
- Add a `presentations/config.py` script and fill in the blanks:

    # General Flask app settings
    DEBUG = True
    SECRET_KEY = ...

    # Redis connection
    REDIS_SERVER = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0

    # Twilio API credentials
    TWILIO_ACCOUNT_SID = ...
    TWILIO_AUTH_TOKEN = ...
    TWILIO_NUMBER = ...

## Twilio

[Inspiration](https://www.twilio.com/blog/2014/11/choose-your-own-adventure-presentations-with-reveal-js-python-and-websockets.html)

1. `python manage.py runserver`
2. `ngrok http 5000`
3. Open `localhost:5000`
4. Note the `ngrok` URL with `/presentation/twilio/webhook/` at the end [here](https://www.twilio.com/user/account/phone-numbers/incoming)
5. Profit
