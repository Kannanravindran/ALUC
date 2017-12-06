from flask import Flask,json,request,jsonify, render_template
from framework import *
from flask_sse import sse
from config import scores
import random

# Redis - Server sent events config
app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(sse, url_prefix='/stream')
app.static_url_path = '/scripts'
# users=['john','david','peter']
mode=None

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/groupify-similar',methods=['get'])
def groupify_similar():
    global mode
    mode="sim"
    return render_template("groupified.html",groups=exec_similar(),students=student_dict)

@app.route('/groupify-dissimilar',methods=['get'])
def groupify_dissimilar():
    global mode
    mode="dissimilar"
    return render_template("groupified.html", groups=exec_dissimilar(),students=student_dict)

@app.route('/student',methods=['get'])
def student():
    return render_template("student.html")

@app.route('/collab',methods=['get'])
def collab():
    global mode
    groupified = {}
    users =[]
    if mode is None:
        return "<center><b><h1>Please wait for the instructor group the students.<br>Try refreshing in sometime.</h1></b></center>"
    if mode == "sim":
        groupified = get_sim()
        groupified_score = exec_similar()
    elif mode == "dis":
        groupified = get_dis()
        groupified_score = exec_dissimilar()
    print groupified
    for group in groupified:
        if inv_student_dict[request.args.get('user').title()] in groupified[group]:
            for _ in groupified[group]:
                print _
                users.append(student_dict[_]['name'])
            break
    avg = 0
    for candi in groupified_score[group]:
        avg = avg + candi[1]
    avg = avg/3
    ques = question[avg/10]
    ques = ques[(avg%10)/3]
    test_users = []
    for user in users:
        if user.lower() != request.args.get('user'):
            test_users.append(user.lower())
    print test_users
    return render_template("collab.html",users=test_users,ques=ques)

@app.route('/overview',methods=['get'])
def overview():
    print request.args.get('group')
    if request.args.get('group') is None:
        group = 1
    else:
        group = request.args.get('group')
    return render_template("overview.html",group=group,roomId=str(gitter_id[int(group)]))

@app.route('/thankyou',methods=['get'])
def thankyou():
    return render_template("thankyou.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4001)