from flask import Flask, Response, jsonify
from utils.scrapper import searchRarbg
app = Flask(__name__)


@app.route('/gw/<path:path>')
def catch_all(path):
    result = searchRarbg("avengers")
    return jsonify({'results': result})
    # else:
    #     result = "gg"
    #     return jsonify({'results': result})


@app.route('/gg/<path:path>')
def catch_all2(path):
    result = searchRarbg("game of thrones")
    return jsonify({'results': result})


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
