from gevent import monkey
monkey.patch_all()

import os
import redis

from presentations import app, redis_db, socketio
from flask.ext.script import Manager, Shell

manager = Manager(app)

def make_shell_context():
    return dict(app=app, redis_db=redis_db)

manager.add_command('shell', Shell(make_context=make_shell_context))

@manager.command
def runserver():
    socketio.run(app, '0.0.0.0', port=5005)

@manager.command
def redis_clear(key):
    redis_cli = redis.StrictRedis(host='localhost', port='6379', db='0')
    redis_cli.delete(key)

if __name__ == '__main__':
    manager.run()
