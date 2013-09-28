Cheeper in Realtime
================================

This tutorial is a follow up to the beginner hack. This tutorial will be more about you exploring different technologies and experimenting with them and will involve less sample code than the previous guide.

Let's add realtime functionality to Cheeper. When anyone makes a Cheep, we want it to appear *instantly* on everyone else's page.

This is actually super tricky. Realtime functionality has been prevalent in the web for a very long time, but only recently have technologies come out that have made it practical.

Websockets are a persistent connection between a client and the server that allows bi-directional communication. Before, with old HTTP, we only had the request-response model, where a client had to initiate a connection with server and only expect one response back. With websockets, we can have the server send the client any new information whenever it's ready and the client doesn't have to send a request for it.

There are two portions to websockets: a client and a server. Let's work on the server. 

Adding websocket functionality to the server is annoying due to a Flask limitation, but it's still possible using the `gevent` library and the `gevent-websocket` library. Install these with `pip`. (You may be missing some operating system dependencies, such as `libevent` s you'll need to figure out how to install these). Once you have these installed, you'll need to integrate it with your Flask server.

To add websocket functionality to our server, add this to the beginning of your `server.py` file.
```python
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
```

Now replace the end of your file with this:
```python
if __name__ == "__main__":
    http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
```

This code imports the websockets library and injects the websocket library into Flask.

Here's a quick overview on how to use websockets with your server now.
```python
@app.route('/ws')
def ws():
    if request.environ.get('wsgi.websocket'):
        websocket = request.environ['wsgi.websocket']
        return
    return "No Websocket"
```
This route creates a websocket to the client who made the request to `/ws`. Websockets support several important methods.

* `ws.send(message)` - Sends a string message to the other end of the websocket
* `ws.receive()` - Waits until a string message arrives on the websocket and returns it

With these methods, you can send information back and forth between the client and the server whenever you want to.

Now with this in mind, you have to design a protocol to let everyone on the site know when a cheep is sent, and send the cheep down to all of them.

Things to consider:
* When a websocket route returns, the websocket is terminated, meaning you have to keep the request alive forever. Consider using a `while True:`.
* You have to maintain a list of everyone's websockets so that you can broadcast the latest cheep to everyone via their websocket
* You have to devise some sort of protocol for the client and server to communicate to each other. Websockets support sending strings, so you'll need to organize how you send down information. Consider using `json`.
