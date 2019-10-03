#encoding: utf-8
from flask import Flask, send_rom_directory, request, render_template, redirect, Response, send_file, make_response
import gospel
import os,io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/showLyrics.html')
def showLyrics():
    musid = request.args.get('musid') 
    return render_template("showLyrics.html",musid=musid)

@app.route('/slide/')
def download_slide():
    url = request.args.get("url-link")
    caminho_slides = os.getcwd() + os.sep + 'slides'
    for the_file in os.listdir(caminho_slides):
        if (str(the_file) != ".gitkeep"):
            os.unlink(caminho_slides + os.sep + the_file)
    name = gospel.createSlide(url)
    return send_file(caminho_slides + os.sep + name,  as_attachment=True, attachment_filename = name)

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

@app.route('/sendByAPI/<name>',methods=['GET'])
def sendSlide(name):
    print(name)
    caminho_slides = os.getcwd() + os.sep + 'slides'
    try:
        return send_file(caminho_slides + os.sep + name,  as_attachment=True, mimetype="application/vnd.openxmlformats-officedocument.presentationml.presentation")
    except Exception as e:
	    return str(e)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug = True, use_reloader=True)