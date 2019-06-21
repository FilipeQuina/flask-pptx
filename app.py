from flask import Flask, send_file
import gospel
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Aqui será a tela principal'

@app.route('/slide/')
def download_slide():
    name = gospel.createSlide()
    return send_file(os.getcwd() + os.sep + 'slides'+ os.sep + name,  as_attachment=True, attachment_filename = name)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug =True)