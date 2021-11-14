from flask import Flask, Response
app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")


# @app.route('/api')
# def api():
#     with open('data.json', mode='r') as my_file:
#         text = my_file.read()
#         return text


# from sanic import Sanic
# from sanic.response import json
# from utils.scrapper import searchRarbg
# app = Sanic()


# @app.route('/<path:path>')
# # @app.route('/main')
# async def index(request, path=""):
#     return json({'hello': path})


# @app.route('/other_route')
# async def other_route(request, path="other_route"):
#     return json({'whatever': path})

# @app.route('/')
# @app.route('/<path:path>')
# async def search(request, path=""):
#     result = searchRarbg("avengers")
#     return json({'results': result})


# @app.route('/test')
# async def search2(request, path="test"):
#     result = searchRarbg("game of thrones")
#     return json({'results': result})
