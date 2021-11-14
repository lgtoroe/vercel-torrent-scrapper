from sanic import Sanic
from sanic.response import json
from utils.scrapper import searchRarbg, getRarbgTorrentData, searchTPB, getTPBTorrentData, search1337x, get1337xTorrentData
app = Sanic()


@app.route('/')
@app.route('/<path:path>')
async def index(request, path=""):
    if path.startswith("api/rarbg"):
        handle_rarbg_route(path, request)
    if path.startswith("api/piratebay"):
        handle_piratebay_route(path, request)
    if path.startswith("api/threesven"):
        handle_threesven_route(path, request)
    return json({'message': "invalid path"}, status=404)


def handle_rarbg_route(path, request):
    if path.startswith("api/rarbg/search"):
        query = request.args.get("q")
        if not query:
            return json({'message': "empty query"}, status=404)
        result = searchRarbg(query)
        if not result:
            return json({'message': "no results found"}, status=404)
        return json({"result": result})
    if path.startswith("api/rarbg/get"):
        link = request.args.get("link")
        if not link:
            return json({'message': "no link provided"}, status=404)
        result = getRarbgTorrentData(link)
        if not result:
            return json({'message': "no results found"}, status=404)
        return json({"result": result})


def handle_piratebay_route(path, request):
    if path.startswith("api/piratebay/search"):
        query = request.args.get("q")
        if not query:
            return json({'message': "empty query"}, status=404)
        result = searchTPB(query)
        if not result:
            return json({'message': "no results found"}, status=404)
        return json({"result": result})
    if path.startswith("api/piratebay/get"):
        link = request.args.get("link")
        if not link:
            return json({'message': "no link provided"}, status=404)
        result = getTPBTorrentData(link)
        if not result:
            return json({'message': "no results found"}, status=404)
        return json({"result": result})


def handle_threesven_route(path, request):
    if path.startswith("api/threesven/search"):
        query = request.args.get("q")
        if not query:
            return json({'message': "empty query"}, status=404)
        result = search1337x(query)
        if not result:
            return json({'message': "no results found"}, status=404)
        return json({"result": result})
    if path.startswith("api/threesven/get"):
        link = request.args.get("link")
        if not link:
            return json({'message': "no link provided"}, status=404)
        result = get1337xTorrentData(link)
        if not result:
            return json({'message': "no results found"}, status=404)
        return json({"result": result})
