from flask import Flask,json,request,jsonify
from framework import *

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file("index.html")

@app.route('/groupify-similar',methods=['get'])
def groupify():
    if len(request.args) > 0:
        response = {"result":exec_similar(request.args['n'],request.args['k'])}
    else:
        response = {"result":exec_similar()}
    return jsonify(response)

@app.route('/groupify-dissimilar',methods=['get'])
def groupify_similar():
    if len(request.args) > 0:
        response = {"result":exec_dissimilar(request.args['n'],request.args['k'])}
    else:
        response = {"result":exec_dissimilar()}
    return jsonify(response)

if __name__ == '__main__':
    app.run()