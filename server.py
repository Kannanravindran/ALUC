from flask import Flask,json,request,jsonify
from framework import *

app = Flask(__name__)

@app.route('/')
def index():
    return '<b>Welcome to AULC</b>'

@app.route('/groupify',methods=['get'])
def groupify():
    return jsonify({"result":exec_schur(request.args['n'],request.args['k'])})

if __name__ == '__main__':
    app.run()
