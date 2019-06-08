from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Aqui será a tela principal'

@app.route('/slide/')
def download_slide():
    return send_file(os.getcwd() + os.sep + 'slides'+ os.sep + 'Ageu-001.ppt',  as_attachment=True, attachment_filename = 'Ageu-001.ppt')

app.run(debug=True, use_reloader=True)