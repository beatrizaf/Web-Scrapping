#Projeto de MINERAÇÃO DE DADOS - Algoritmos e Lógica de Programação 2019.1
#coding: utf-8
#coding: utf-8
import json
import os
import urllib.request
import requests
from bs4 import BeautifulSoup
import seaborn as sns

def abrir():
    with open('analise.json') as f:    
        data = json.load(f)
    f.close()
    return data 


