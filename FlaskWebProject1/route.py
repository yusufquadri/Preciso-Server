from flask import Flask , url_for
from app import app
from flask import request
from flask import render_template
from flask.templating import render_template
import basic_sentiment_analysis 
@app.route('/')
def temp():
    user = "yusuf"
    print("default")
    return render_template("Home.html",user=user)

@app.route("/register")
def register():
    return render_template("Homepage.html")
    
@app.route("/spell")
def spell():
    return render_template("Spell.html")

@app.route('/spell1/',methods =["POST"] )
def spell1():
    global user
    user = request.values.get('param')
    print(user)
    user = basic_sentiment_analysis.abcd(user)
    #test1(user)
    return render_template("test.html",user = user)
    
@app.route("/test1")
def test1():
    #user = "yeahhhhhh "
    return render_template("test1.html",user=user)
#@app.route('/temp',methods=["POST"])

#def temp():
 #   de=request.form("param")
#    request.args.get('param')
    
#@app.route('/spell/<getting_data>')
#def spell(getting_data):
   # print(getting_data)
   # return getting_data


          
          
