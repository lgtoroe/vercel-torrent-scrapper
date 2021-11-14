from flask import Flask, Response
app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return {'hasdsad': path}


# @app.route('/abc/<path:path>')
# async def index(request, path=""):
#     return json({'hasdsad': path})
