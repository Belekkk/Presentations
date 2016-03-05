from flask import Flask
from flask.ext.socketio import SocketIO
import redis

app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')

redis_db = redis.StrictRedis(host=app.config['REDIS_SERVER'],
                             port=app.config['REDIS_PORT'],
                             db=app.config['REDIS_DB'])

socketio = SocketIO(app)

from . import views
from . import websockets
