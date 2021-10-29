# Projeto WebScraping com API Flask

Projeto de Web Scrapping com Python para busca de modelos de notebook Lenovo do site [webscraper.io](https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops) 

## Primeiros passos

Baixar os arquivos pelo [Link](https://github.com/gabrielsuper/webscraping/archive/refs/heads/main.zip) e depois extrair o arquivo ```webscraping-main``` dentro de uma pasta local em seu computador, é importante salientar que os arquivos devem estar dentro de uma pasta com o exato nome webscraping, caso baixe o arquivo rar e ao descompactar a pasta esteja como nome webscraping-main renomeie a pasta para ```webscraping```. É necessário realizar o download do [Python](https://www.python.org/) e instalar para executar o projeto.

## Instalação dos módulos

Para execução correta do arquivo é importando instalar os módulos, acessando o terminal e executando o comando ```pip install "nome do modulo"```.
Exemplo:
```
pip install json
pip install flask
pip install os
pip install pandas
pip install bs4
pip install selenium
pip install time
```
Após a instalação de todos os módulos execute seu terminal python o arquivo api.py, exemplo: python api.py
Pode ser executado também no terminal do linux, windows ou vscode.

## Acessando os dados na api

Para acessar os dados da api abra o browser de sua preferência (Mozilla,Chrome,etc) e digite http://127.0.0.1:5000/products
Ele irá listar os produtos Lenovo por ordem de preço como na imagem abaixo.

![image](https://user-images.githubusercontent.com/79488507/139363245-81de49ff-c7c5-412e-98b2-9fd824ecf4e0.png)
