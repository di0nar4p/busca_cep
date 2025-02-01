from flask import Flask, request, jsonify, send_from_directory
from Controller.Requests import busca_cep


app = Flask(__name__)

@app.route('/<int:cep>', methods=['GET'])
def index(cep):
    if request.method == 'GET':
        return busca_cep(cep)



@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host= "0.0.0.0" ,debug=True, ssl_context=('cert.pem', 'key.pem'))