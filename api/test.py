from flask import Flask, Response
from utils.scrapper import searchRarbg


app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return {"message": "hello world"}
