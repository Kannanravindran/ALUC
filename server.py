from flask import Flask,json,request,jsonify
from framework import *

app = Flask(__name__)

@app.route('/')
def index():
    return '<b>Welcome to AULC</b>'

@app.route('/groupify',methods=['get'])
def groupify():
    if len(request.args) > 0:
        response = {"result":exec_schur(request.args['n'],request.args['k'])}
    else:
        response = {"result":exec_schur()}
    return jsonify(response)

if __name__ == '__main__':
    app.run()