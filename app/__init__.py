from flask import Flask
from flask.ext.socketio import SocketIO
import redis
 
app = Flask(__name__)

app.config.from_object('config')

REDIS_SERVER = app.config['REDIS_SERVER']
REDIS_PORT = app.config['REDIS_PORT']
REDIS_DB = app.config['REDIS_DB']
 
redis_db = redis.StrictRedis(host=REDIS_SERVER, port=REDIS_PORT, db=REDIS_DB)
 
socketio = SocketIO(app)
 
from app import views
from app import websockets