import os
from flask import (Flask, flash, redirect, render_template, request, send_from_directory, url_for)
from Controller.Requests import busca_cep

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/cep', methods=['GET'])
def index():

    cep = request.args.get('cep')
    if cep:
        dados= busca_cep(cep)
        if "erro" in dados.keys():
            return redirect(url_for('erro'))
        else:
            return render_template('main.html', dados=dados) 
            
@app.route('/erro', methods=["GET"])
def erro():

    flash('CEP não encontrado!')
    return redirect(url_for('main'))


@app.route('/', methods=['GET'])
def main():

    return render_template('index.html')





@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host= "0.0.0.0" ,debug=True)