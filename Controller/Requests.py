import requests
from flask import render_template
import json
def busca_cep(cep):

    url =f'https://viacep.com.br/ws/{cep}/json/'
    
    headers= {
        'content-type':'application/json'
    }

    try:
        
        dados= requests.get(url,headers).json()
        return render_template('index.html', dados=dados)

    except Exception as e:
        
        return {'message': f'Bad Request: {e}'}, 400

