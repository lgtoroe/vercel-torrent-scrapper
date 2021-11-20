from flask import Flask, request
from flask_cors import CORS
from utils.scrapper import searchRarbg, getRarbgTorrentData, searchTPB, getTPBTorrentData, search1337x, get1337xTorrentData, searchNyaa
app = Flask(__name__)
CORS(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path.startswith("api/rarbg"):

        # handle_rarbg_route(path, request)
        if path.startswith("api/rarbg/search"):
            query = request.args.get("q")
            if not query:
                return {'message': "empty query"}, 404
            result = searchRarbg(query)
            if not result:
                return {'message': "no results found"}, 404
            return {"result": result}
        if path.startswith("api/rarbg/get"):
            link = request.args.get("link")
            if not link:
                return {'message': "no link provided"}, 404
            result = getRarbgTorrentData(link)
            if not result:
                return {'message': "no results found"}, 404
            return {"result": result}
    elif path.startswith("api/piratebay"):
        # handle_piratebay_route(path, request)
        if path.startswith("api/piratebay/search"):
            query = request.args.get("q")
            if not query:
                return {'message': "empty query"}, 404
            result = searchTPB(query)
            if not result:
                return {'message': "no results found"}, 404
            return {"result": result}
        if path.startswith("api/piratebay/get"):
            link = request.args.get("link")
            if not link:
                return {'message': "no link provided"}, 404
            result = getTPBTorrentData(link)
            if not result:
                return {'message': "no results found"}, 404
            return {"result": result}
    elif path.startswith("api/1337"):
        # handle_threesven_route(path, request)
        if path.startswith("api/1337/search"):
            query = request.args.get("q")
            if not query:
                return {'message': "empty query"}, 404
            result = search1337x(query)
            if not result:
                return {'message': "no results found"}, 404
            return {"result": result}
        if path.startswith("api/1337/get"):
            link = request.args.get("link")
            if not link:
                return {'message': "no link provided"}, 404
            result = get1337xTorrentData(link)
            if not result:
                return {'message': "no results found"}, 404
            return {"result": result}
    elif path.startswith("api/nyaa"):
        # handle_threesven_route(path, request)
        if path.startswith("api/nyaa/search"):
            query = request.args.get("q")
            if not query:
                return {'message': "empty query"}, 404
            result = searchNyaa(query)
            if not result:
                return {'message': "no results found"}, 404
            return {"result": result}
    else:
        return {'message': "invalid path"}
