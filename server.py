from flask import Flask,json,request,jsonify, render_template
from framework import *
from config import scores

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/groupify-similar',methods=['get'])
def groupify():
    return render_template("groupified.html",groups=exec_similar(),scores=[1,2,3,4,5,6,7,8,9,10])

@app.route('/groupify-dissimilar',methods=['get'])
def groupify_similar():
    return render_template("groupified.html", groups=exec_dissimilar(),scores=scores)

@app.route('/collab',methods=['get'])
def collab():
    return render_template("collab.html")


if __name__ == '__main__':
    app.run()