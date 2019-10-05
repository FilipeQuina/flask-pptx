#encoding: utf-8
from flask import Flask, request, render_template, make_response
import gospel
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/showLyrics/')
def showLyrics():
    musid = request.args.get('musid') 
    return render_template("showLyrics.html",musid=musid)

@app.route('/sendByAPI',methods=['POST'])
def sendByAPI():
    title = request.form["title"]
    band = request.form["band"]
    text = request.form["text"]
    slideObj = gospel.createSlideAPI(title,band,text)
    name = title+"-"+band+".pptx"
    response = make_response(slideObj)
    response.headers['Content-Type'] = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    response.headers['Content-Description'] = 'attachment; filename={}'.format(name)
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug = True, use_reloader=True)