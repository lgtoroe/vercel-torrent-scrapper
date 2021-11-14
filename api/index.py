from flask import Flask, Response
app = Flask(__name__)


@app.route('/',)
@app.route('/<path:path>')
def index(path):
    return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")


@app.route("/gg")
def other():
    return {"hello": "world"}
