from flask import Flask,json,request,jsonify, render_template
from framework import *
from config import scores

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/groupify-similar',methods=['get'])
def groupify():
    return render_template("groupified.html",groups=exec_similar(),scores=scores)

@app.route('/groupify-dissimilar',methods=['get'])
def groupify_similar():
    return render_template("groupified.html", groups=exec_dissimilar(),scores=scores)

if __name__ == '__main__':
    app.run()