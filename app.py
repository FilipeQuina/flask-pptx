from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Aqui será a tela principal'

@app.route('/slide/')
def download_slide():
    return send_file(os.getcwd() + os.sep + 'slides'+ os.sep + 'Ageu-001.ppt',  as_attachment=True, attachment_filename = 'Ageu-001.ppt')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)