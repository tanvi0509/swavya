from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__, template_folder='__/templates')
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('login.html')

@socketio.on('message')
def handle_message(message):
    print('Message received:', message)
    socketio.emit('notification', message)

if __name__ == '__main__':
    socketio.run(app, debug=True,port=500)
