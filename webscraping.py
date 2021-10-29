#Bibliotecas importadas
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os


#Função para consultar os dados da página por meio do webscraping e criar o json dos dados
def execWebScraping():
    #Consulta o diretorio raiz onde o arquivo webscrapinp.py se encontra ex : C:
    DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #Seta na var PATH o caminho do chrome driver
    PATH = DIR + "\WEBSCRAPING\chromedriver.exe"

    #Atribui o valor da url e consulta por meio do webdriver
    url_laptops = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    driver = webdriver.Chrome(PATH)
    driver.get(url_laptops)
    sleep(5)

    #Consulta o conteudo do html e insere na variável content
    element_page = driver.find_element_by_xpath("//html")
    content = element_page.get_attribute('outerHTML')

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

    driver.quit()
