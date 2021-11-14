from sanic import Sanic
from sanic.response import json
from utils.scrapper import searchRarbg, getRarbgTorrentData
app = Sanic()


@app.route('/')
@app.route('/<path:path>')
async def index(request, path=""):
    if path.startswith("api/search"):
        query = request.args.get("q")
        if not query:
            return json({'message': "empty query"}, status=404)
        result = searchRarbg(query)
        if not result:
            return json({'message': "no results found"}, status=404)
        return json({"result": result})
    if path.startswith("api/get"):
        link = request.args.get("link")
        if not link:
            return json({'message': "no link provided"}, status=404)
        result = getRarbgTorrentData(link)
        if not result:
            return json({'message': "no results found"}, status=404)
        return json({"result": result})
    return json({'message': "invalid path"}, status=404)
