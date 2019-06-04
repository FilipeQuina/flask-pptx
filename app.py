import os
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World</h1>"

@app.route("/api")
def ret():
    result = [{"id":37823,"name":"J\u00e9ssica Reis"},{"id":37822,"name":"Tadeu Francisco"},{"id":37821,"name":"Matheus Pado"},{"id":37720,"name":"Palloma"},{"id":37191,"name":"Peter Parker"},{"id":37186,"name":"Peter Parker"},{"id":37185,"name":"Flavio Almeida"},{"id":37182,"name":"Filipe Pacheco"},{"id":36985,"name":"Sebasti\u00e3o Jos\u00e9 Almeida Barbosa J\u00fanior"},{"id":36972,"name":"Sucesso do Cliente"},{"id":35976,"name":"\u00cdtalo N\u00f3brega"},{"id":35962,"name":"Paulo Tinoco"},{"id":22341,"name":"Vin\u00edcius Melo"}]
    return result

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)