#Projeto de MINERAÇÃO DE DADOS - Algoritmos e Lógica de Programação 2019.1
#coding: utf-8
#coding: utf-8
import json
import os
import urllib.request
import requests
from bs4 import BeautifulSoup
import seaborn as sns

busca = input("Digite o que deseja pesquisar na web:")
json.dumps(busca) #converte para json

def abrir():
    with open('analise.json') as f: #abertura do arquivo json
        data = json.load(f) #convertendo para um objeto Python
        
    f.close()
    return data 


