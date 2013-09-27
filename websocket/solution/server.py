from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
import sqlite3
import time
import json
from flask import Flask, request, g, render_template

app = Flask(__name__)
DATABASE = 'cheeps.db'
counter = 0
websockets = {}

class WSMessage:
    def __init__(self, message):
        self.message = message

    def to_json(self):
        return str(json.dumps(self.message))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def db_read_cheeps():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM cheeps")
    return cur.fetchall()

def db_add_cheep(name, cheep):
    cur = get_db().cursor()
    t = str(time.time())
    cheep_info = (name, t, cheep)
    cur.execute("INSERT INTO cheeps VALUES (?, ?, ?)", cheep_info)
    get_db().commit()

@app.route("/")
def hello():
    cheeps = db_read_cheeps()
    return render_template('index.html', cheeps=cheeps)

def send_message(message):
    msg = WSMessage(message)
    for id, ws in websockets.items():
        ws.send(msg.to_json())

@app.route('/ws')
def api():
    if request.environ.get('wsgi.websocket'):
        global counter
        ws = request.environ['wsgi.websocket']
        websockets[counter] = ws
        counter += 1
        while True:
            message = ws.receive()
            message = json.loads(message)
            db_add_cheep(message['name'], message['cheep'])
            send_message(message)
        del websockets[counter - 1]
        return
    return "No Websocket"

if __name__ == "__main__":
    http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
