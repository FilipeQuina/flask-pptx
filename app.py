import os
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World</h1>"

@app.route("/api")
def ret():
    result = '{"id":"37182","name":"Filipe P","email":"aa@aa.com","login":"aa@aa.com","type":2,"phone":"32988776655"}'
    return result

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)