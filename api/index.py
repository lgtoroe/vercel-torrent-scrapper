from sanic import Sanic
from sanic.response import json
from utils.scrapper import searchRarbg
app = Sanic()


@app.route('/')
@app.route('/<path:path>')
async def search(request, path=""):
    result = searchRarbg("avengers")
    return json({'results': result})


@app.route('/test/<path:path>')
async def search2(request, path=""):
    result = searchRarbg("game of thrones")
    return json({'results': result})
