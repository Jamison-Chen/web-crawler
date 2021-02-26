from flask import Flask, url_for, redirect, Response
# from flask import request as flaskRq
import requests
from pyquery import PyQuery as pq
import json
# import random
# import csv
# import time
# import re
app = Flask(__name__)


def fetchWiki(url):
    resp = requests.get(url)
    doc = pq(resp.text)
    # return json.dumps({"body": doc.children("body")})
    return json.dumps({"body": "hi"})


# fetchWiki("https://en.wikipedia.org/wiki/NP-completeness")


@app.route("/")
def home():
    try:
        resp = Response(response={"DEF"}, headers={
                        'Access-Control-Allow-Origin': "*"})
    except Exception as e:
        resp = "Helloooo"
    return resp


# @app.route("/getUserInfo", methods=['GET'])
# def getUserInfo():
#     # resp = "Hello"
#     try:
#         resp = Response(response="{\"ABC\": \"abc\"}", headers={
#                         'Access-Control-Allow-Origin': "*"})
#         # resp.headers['Access-Control-Allow-Origin'] = '*'
#     except Exception as e:
#         resp = "Helloooo"
#     return resp


if __name__ == "__main__":
    # app.run()
    pass


# git add .
# git commit -m "..."
# git push heroku master
