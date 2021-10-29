#Importa as bibliotecas necessárias
from flask import Flask, jsonify, request
import json
import os
from webscraping import execWebScraping

#Invoca a função do arquivo webscraping.py para que o products.json seja criado
execWebScraping()
#Cria a aplicação
app = Flask('WebScrappingNotebooks')
#Verifica o diretório raiz onde a pasta do projeto webscraping está salva
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
#Abre o arquivo products.json localizado dentro da pasta WEBSCRAPING realiza a leitura do mesmo e atribui para products
with open(BASE_DIR + '\\WEBSCRAPING\\products.json') as prod:    
    products = json.load(prod)
#Cria a rota get que irá consultar todos os produtos
@app.route('/products', methods=['GET'])
def home():
    return jsonify(products), 200

#Inicia a api
app.run(debug=True)