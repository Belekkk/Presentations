from flask.ext.socketio import emit

from . import socketio


@socketio.on('connect', namespace='/presentation')
def test_connect():
    pass

@socketio.on('disconnect', namespace='/presentation')
def test_disconnect():
    pass
