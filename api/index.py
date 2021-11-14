from sanic import Sanic
from sanic.response import json
from utils.scrapper import searchRarbg
app = Sanic()


@app.route('/')
@app.route('/<path:path>')
async def index(request, path=""):
    if path == "api/search":
        query = request.args.get("q")
        if not query:
            return json({'message': "empty query"}, status=404)
        result = searchRarbg(query)
        return json({"result": result})
    return json({'message': "invalid path"}, status=404)
