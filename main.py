import json

import requests
from flask import Flask, Response
from flask import request as flaskRq
from pyquery import PyQuery as pq

app = Flask(__name__)


def fetchWiki(url):
    resp = requests.get(url)
    doc = pq(resp.text)
    return json.dumps({"body": doc.find("body").html()})


@app.route("/")
def index():
    try:
        resp = Response(
            response={"Hello"}, headers={"Access-Control-Allow-Origin": "*"}
        )
    except Exception:
        resp = "Failed To Fetch"
    return resp


@app.route("/fetchContent", methods=["GET"])
def fetchContent():
    url = str(flaskRq.args.get("url"))
    try:
        resp = Response(
            response=fetchWiki(url), headers={"Access-Control-Allow-Origin": "*"}
        )
    except Exception:
        resp = "Failed To Fetch"
    return resp


if __name__ == "__main__":
    app.run()
