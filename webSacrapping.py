#coding: utf-8
import json #Usamos o Json para manipulação de arquivos json
import os # Usamos o OS para adiquirir informações a respeito do SO e adequar o funcionamento independentemente do SO em uso 
import urllib.request #Usamos a urllib.request
import requests #Usamos os requests para abrir as URLs em questão
from bs4 import BeautifulSoup #Usamos o Beautiful Soup para fazer a extração dos dados

"""
#Gerar histograma e nuvem de palavra
import seaborn as sns #Usamos para gerar o gráfico
OBSERVAÇÃO: A partir desse trecho de código, importaremos as bibliotecas fundamentais  para a geração da Nuvem de Palavra
import re
from worldcloud import WorldCloud, STOPWORDS, ImageColorGenerator #OBS: 
from os import path
import matplotlib.pyplot as plt
"""

listadearquivos = ["armazena.txt"]
l1 = []
l2 = []

#função criada para abertura do arquivo JSON
def abrir():
    with open('analise.json', "r") as f:    
        dado = json.load(f)
    f.close()
    print (dado)
    return dado

""" Sabendo que essa variável "data" vai me retornar o 
"""
#função criada para a inserção de palavra pelo o usuário e para a validação

def receber_e_validar():
    abrir = True
    while abrir == True:
        palavra = input("Digite a sua pesquisa: ").lower() #Usando o lower par deixar as entradas como minúsculo, por padrão para cada entrada
        if palavra in dado:
            lista = dado[palavra]
            abrir = False
            return palavra
        else:
            print("A expressão procurada é inexistente")
