import subprocess
from distutils.log import debug
import os
import sys

# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def hello():
#     return 'Hello, World!'


# @app.route('/automate')
# def automate():
#     # steps
#     print(sys.platform)
#     return sys.platform
#     # get os
# pass


# app.run(debug=True)

# Basic blask server to catch events
from flask import Flask, request
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


# @socketio.on('connect')
# def run():
#     process = subprocess.Popen()
# Decorator to catch an event called "my event":


@socketio.on('my_event')
# test_message() is the event callback function.
def test_message(message):
    print(message)
    # Trigger a new event called "my response"
    if message == 'automate':
        platform = sys.platform
        emit('message', 'platform detected' + platform)
        if platform.startswith('win'):
            # windows code

            pass
        elif platform.startswith('linux'):
            # linux code
            pass
        else:
            emit('message', 'bruh we are sorry scripts havent developed for this purpose')

            # that can be caught by another callback later in the program.


if __name__ == '__main__':
    socketio.run(app, debug=True)
