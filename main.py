from flask import Flask, request, url_for, redirect, Response
# import random
# import csv
# import time
# import re
app = Flask(__name__)


@app.route("/")
def home():
    try:
        resp = Response(response="{\"ABC\": \"abc\"}", headers={
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
    app.run()


# git add .
# git commit -m "..."
# git push heroku master
