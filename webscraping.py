#Bibliotecas importadas
import requests
from bs4 import BeautifulSoup
import pandas as pd


#Função para consultar os dados da página por meio do webscraping e criar o json dos dados
def execWebScraping():
    
    #Consulta por meio da biblioteca requests as informações da url
    response = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')

    #Atribui o contéudo html da página na variável content
    content = response.content
    #Formata os dados da variável content em html e atribui para a variável page
    page = BeautifulSoup(content, 'html.parser')
    #Procura na page todas as div's que possuem a class caption
    products = page.findAll('div', attrs={'class': 'caption'})
    #Array de produtos a serem normalizados (Será extraida as informações necessárias e amazedanas neste array)
    normalizeProducts = []
    #Looping para extrair do array de products o preço de cada item e seu respectivo titulo
    for p in products:
        price = p.find('h4', attrs={'class': 'pull-right price'})
        title = p.find('p', attrs={'class': 'description'})

        targetProduct = 'Lenovo'
        #Validação para verificar se o produto em questão é um lenovo, caso verdadeiro é atribuido para o array normalizeProducts
        if targetProduct in title.text:

            product = {
                "price": price.text,
                "title": title.text,
            }

            normalizeProducts.append(product)

    #Os passos abaixo criam um Json dos dados e exportam um arquivo no formato .jsonS
    dataFrame = pd.DataFrame(normalizeProducts)
    dados = dataFrame.to_json(orient= 'records')
    doc = open('products.json', 'w')
    doc.write(dados)
    doc.close()