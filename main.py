from flask import Flask, request, jsonify, send_from_directory, render_template
from Controller.Requests import busca_cep


app = Flask(__name__)

@app.route('/cep', methods=['GET'])
def index():
        cep = request.args.get('cep')
        if cep:
            dados= busca_cep(cep)
            return render_template('main.html', dados=dados)
        return render_template('main.html')
        
         
@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host= "0.0.0.0" ,debug=True, ssl_context=('cert.pem', 'key.pem'))