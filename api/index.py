# from sanic import Sanic
# from sanic.response import json
# from sanic_cors import CORS, cross_origin

# from utils.scrapper import searchRarbg, getRarbgTorrentData, searchTPB, getTPBTorrentData, search1337x, get1337xTorrentData
# app = Sanic(__name__)
# CORS(app, resources={r"/api/*": {"origins": "*"}})


# @app.route('/')
# @app.route('/<path:path>')
# @cross_origin(app)
# async def index(request, path=""):
#     if path.startswith("api/rarbg"):
#         # handle_rarbg_route(path, request)
#         if path.startswith("api/rarbg/search"):
#             query = request.args.get("q")
#             if not query:
#                 return json({'message': "empty query"}, status=404)
#             result = searchRarbg(query)
#             if not result:
#                 return json({'message': "no results found"}, status=404)
#             return json({"result": result})
#         if path.startswith("api/rarbg/get"):
#             link = request.args.get("link")
#             if not link:
#                 return json({'message': "no link provided"}, status=404)
#             result = getRarbgTorrentData(link)
#             if not result:
#                 return json({'message': "no results found"}, status=404)
#             return json({"result": result})
#     elif path.startswith("api/piratebay"):
#         # handle_piratebay_route(path, request)
#         if path.startswith("api/piratebay/search"):
#             query = request.args.get("q")
#             if not query:
#                 return json({'message': "empty query"}, status=404)
#             result = searchTPB(query)
#             if not result:
#                 return json({'message': "no results found"}, status=404)
#             return json({"result": result})
#         if path.startswith("api/piratebay/get"):
#             link = request.args.get("link")
#             if not link:
#                 return json({'message': "no link provided"}, status=404)
#             result = getTPBTorrentData(link)
#             if not result:
#                 return json({'message': "no results found"}, status=404)
#             return json({"result": result})
#     elif path.startswith("api/threesven"):
#         # handle_threesven_route(path, request)
#         if path.startswith("api/threesven/search"):
#             query = request.args.get("q")
#             if not query:
#                 return json({'message': "empty query"}, status=404)
#             result = search1337x(query)
#             if not result:
#                 return json({'message': "no results found"}, status=404)
#             return json({"result": result})
#         if path.startswith("api/threesven/get"):
#             link = request.args.get("link")
#             if not link:
#                 return json({'message': "no link provided"}, status=404)
#             result = get1337xTorrentData(link)
#             if not result:
#                 return json({'message': "no results found"}, status=404)
#             return json({"result": result})
#     else:
#         return json({'message': "invalid path"}, status=404)


# def handle_rarbg_route(path, request):
#     if path.startswith("api/rarbg/search"):
#         query = request.args.get("q")
#         if not query:
#             return json({'message': "empty query"}, status=404)
#         result = searchRarbg(query)
#         if not result:
#             return json({'message': "no results found"}, status=404)
#         return json({"result": result})
#     if path.startswith("api/rarbg/get"):
#         link = request.args.get("link")
#         if not link:
#             return json({'message': "no link provided"}, status=404)
#         result = getRarbgTorrentData(link)
#         if not result:
#             return json({'message': "no results found"}, status=404)
#         return json({"result": result})


# def handle_piratebay_route(path, request):
#     if path.startswith("api/piratebay/search"):
#         query = request.args.get("q")
#         if not query:
#             return json({'message': "empty query"}, status=404)
#         result = searchTPB(query)
#         if not result:
#             return json({'message': "no results found"}, status=404)
#         return json({"result": result})
#     if path.startswith("api/piratebay/get"):
#         link = request.args.get("link")
#         if not link:
#             return json({'message': "no link provided"}, status=404)
#         result = getTPBTorrentData(link)
#         if not result:
#             return json({'message': "no results found"}, status=404)
#         return json({"result": result})


# def handle_threesven_route(path, request):
#     if path.startswith("api/threesven/search"):
#         query = request.args.get("q")
#         if not query:
#             return json({'message': "empty query"}, status=404)
#         result = search1337x(query)
#         if not result:
#             return json({'message': "no results found"}, status=404)
#         return json({"result": result})
#     if path.startswith("api/threesven/get"):
#         link = request.args.get("link")
#         if not link:
#             return json({'message': "no link provided"}, status=404)
#         result = get1337xTorrentData(link)
#         if not result:
#             return json({'message': "no results found"}, status=404)
#         return json({"result": result})

from flask import Flask, Response
app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path == "api/search":
        return {'message': "asdasd"}
    return {'message': "empty query"}
