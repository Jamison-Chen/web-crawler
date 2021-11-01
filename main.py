from flask import Flask, url_for, redirect, Response
from flask import request as flaskRq
import requests
from pyquery import PyQuery as pq
import json
app = Flask(__name__)


def fetchWiki(url):
    resp = requests.get(url)
    doc = pq(resp.text)
    return json.dumps({"body": doc.find("body").html()})


@app.route("/")
def home():
    try:
        resp = Response(response={"Hello"}, headers={
                        'Access-Control-Allow-Origin': "*"})
    except Exception as e:
        resp = "Helloooo"
    return resp


@app.route("/fetchContent", methods=['GET'])
def fetchContent():
    url = str(flaskRq.args.get("url"))
    try:
        resp = Response(response=fetchWiki(url), headers={
                        'Access-Control-Allow-Origin': "*"})
    except Exception as e:
        resp = "Helloooo"
    return resp


if __name__ == "__main__":
    app.run()
