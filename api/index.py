from sanic import Sanic
from sanic.response import json
from utils.scrapper import searchRarbg
app = Sanic()


@app.route('/')
@app.route('/<path:path>')
async def index(request, path=""):
    result = searchRarbg("avengers")
    return json({'hasdsad': result})
