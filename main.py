import json

import requests
from flask import Flask, Response
from flask import request as flask_request
from pyquery import PyQuery

app = Flask(__name__)


@app.route("/")
def index():
    try:
        return Response(
            response={"Hello"}, headers={"Access-Control-Allow-Origin": "*"}
        )
    except Exception:
        return "Failed"


@app.route("/fetchContent", methods=["GET"])
def fetchContent():
    try:
        url = str(flask_request.args.get("url"))
        response = PyQuery(requests.get(url).text)
        return Response(
            response=json.dumps({"body": response.find("body").html()}),
            headers={"Access-Control-Allow-Origin": "*"},
        )
    except Exception:
        return "Failed To Fetch"


if __name__ == "__main__":
    app.run()
