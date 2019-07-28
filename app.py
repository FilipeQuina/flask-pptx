from flask import Flask, send_file, request, render_template
import gospel
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/slide/')
def download_slide():
    url = request.args.get("url-link")
    caminho_slides = os.getcwd() + os.sep + 'slides'
    for the_file in os.listdir(caminho_slides):
        if (str(the_file) != ".gitkeep"):
            os.unlink(caminho_slides + os.sep + the_file)
  
    name = gospel.createSlide(url)
    return send_file(caminho_slides + os.sep + name,  as_attachment=True, attachment_filename = name)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug = True, use_reloader=True)