from sanic import Sanic
from sanic.response import json
app = Sanic()


@app.route('/abc')
# @app.route('/abc/<path:path>')
async def index(request, path=""):
    return json({'hello': path})


# @app.route('/other_route')
# @app.route('/<path:path>')
# async def other_route(request, path=""):
#     return json({'whatever': path})

# @app.route("/gg")
# def other():
#     return {"hello": "world"}
