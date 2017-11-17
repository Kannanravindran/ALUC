from flask import Flask,json,request,jsonify, render_template
from framework import *
from flask_sse import sse
from config import scores

# Redis - Server sent events config
app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(sse, url_prefix='/stream')
app.static_url_path = '/scripts'
users=['john','david','peter']

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/groupify-similar',methods=['get'])
def groupify():
    return render_template("groupified.html",groups=exec_similar(),students=student_dict)

@app.route('/groupify-dissimilar',methods=['get'])
def groupify_similar():
    return render_template("groupified.html", groups=exec_dissimilar(),students=student_dict)

@app.route('/collab',methods=['get'])
def collab():
    test_users = []
    for user in users:
        if user != request.args.get('user'):
            test_users.append(user)
    return render_template("collab.html",users=test_users)


if __name__ == '__main__':
    app.run(host="0.0.0.0")