# ! -*- encoding:utf-8 -*-
# !/usr/bin/python
import json  # Importa um arquivo com um formato de intercâmbio de dados leve inspirado por JavaScript
import os  # Dentre tantas funcionalidades, este módulo fornece também uma maneira portátil de usar a funcionalidade dependente do sistema operacional
import io # Módulo fornece as interfaces do Python para o gerenciamento de fluxo
import urllib2 # Auxilia na extração das tags
from pylab import *  # Dentre suas funcionalidades, assumirá a função de gerar os gráficos
import requests # Assumirá a função de definir funções e classes que ajudam na abertura de URLs
from bs4 import BeautifulSoup  # Essa biblioteca possibilita fazer a extração dos dados de uma forma mais prática


# LISTAS CRIADAS PARA ARMAZENAR A EXTRAÇÃO DAS URL's
arquivos = ["armazena_extracao.txt"]
lista1 = []  # NO DECORRER DO CÓDIGO, MOSTRAREI A UTILIDADE DESSA LISTA
lista2 = []  # NO DECORRER DO CÓDIGO, MOSTRAREI A UTILIDADE DESSA LISTA

# ABERTURA DO ARQUIVO JSON
def abertura():
    with io.open("analise.json", "r", encoding= 'utf-8') as data_file:
        data = json.load(data_file)
    data_file.close()
    return data

# ANÁLISE DE INSERÇÃO DO USUÁRIO
def analise(data):
    try:
        abrir = True

        while abrir == True:
            letter = input("Informe a palavra:").lower()  # RECEBE A PALAVRA DA ENTRADA PADRÃO E PÕES EM MINUSCULO PARA PADRONIZAR A LEITURA

            if letter in data:
                lista = data[letter]
                print(lista)
                abrir = False
                return letter
            else:
                print('Palavra inválida')

    except NameError:
        print('Identificador não é encontrado no namespace local ou global')
    except TypeError:
        print('Fatorial não é suportado para determinado tipo de entrada.')


# PROCURA NO ARQUIVO JSON AS NOTÍCIAS
def procura_armazenamento(data, letter):
    # VARIÁVEL "STRINGS" ARMAZENA A LISTA REFERENTE A CHAVE DIGITADA PELO USUÁRIO
    # Ex.: "nome" : ["Martin", "Luther", "King", "Malcolm"] -> ESSA LISTA SERÁ ARMANEZADA EM "STRINGS"
    try:
        strings = data[letter]

        # VARIÁVEL CRIARÁ UMA LISTA E ORDENARÁ A POSIÇÃO DE CADA UM
        # Ex.: ["Martin", "Luther", "King", "Malcolm"], NESSA SITUAÇÃO TEMOS 4 ELEMENTOS
        pos = arange(len(data[letter]))

        # ABRIRÁ O DIRETÓRIO E ANALISARÁ TODOS OS ARQUIVOS INSERIDOS NELE.
        files = [f for f in os.listdir(".") if f.startswith("armazena_extracao.txt") and f.endswith('.txt')] #Listcomprehesion
        # 1º FOR TERÁ UTILIDADE DE PERCORRER TODOS OS TXT'S ALOCADOS NO DIRETÓRIO
        for filename in files:
            # ESSAS VARIÁVEIS AQUI, ASSUMIRAM O PAPEL DE ZERAR QUANDO FOR FEITA UMA ITERAÇÃO
            lista1 = []
            lista2 = []
            with io.open(filename, encoding='utf-8', mode='r') as f:
                arquivo = f.read()

                # 2º FARÁ A COMPARAÇÃO DE CADA ELEMENTO DA VARIÁVEL "STRINGS" COM CADA ELEMENTO DO ARQUIVO TXT
                for s in strings:
                    print (filename, s, arquivo.count(s))
                    # LISTA1 ARMANEZA OS ELEMENTOS EM COMUM
                    lista1.append(s)
                    # LISTA2 ARMAZENA A INCIDÊNCIA DAS PALAVRAS NO TXT
                    lista2.append(arquivo.count(s))
            f.close()
        return lista1, lista2, pos
    except KeyError:
        print('Chave não encontrada no dicionário!')

def grafico(lista1, lista2, pos):
    # APÓS A PROCURA DO JSON NO ARQUIVO GERAREMOS O GRÁFICO(HISTOGRAMA)
    bar(pos, lista2, align='center', color='orange')
    xticks(pos, lista1)
    plt.title("WebScrapping")

    show()
    print(len(lista1))
    print(lista2)


# FUNÇÃO COM O PROPÓSITO DE FAZER O SCRAPINGWEB
def url_search():

    try:
        # ABRE O ARQUIVO ONDE HÁ AS URL's PRÉ DEFENIDAS E AS DECODIFICA PARA A LEITURA DO PYTHON
        with io.open("Exemplo.txt", encoding='utf-8', mode='r') as data_file:
            # INICIALIZA A VARIAVEL PARA INSERÇÃO DOS TEXTOS LIDOS NAS URL's
            soup_text = ""
            for line in data_file:
                html_content = urllib2.urlopen(line)
                soup = BeautifulSoup(html_content, "lxml")
                soup_text += soup.get_text()

        data_file.close()

        # ABRE ARQUIVO ONDE FORAM ARMAZENADOS OS TEXTOS DAS URL's
        with io.open("armazena_extracao.txt", mode='a+') as out:
            out.write(soup_text)
            # print(out.write)

        out.close()

    except NameError:
        print('Identificador não é encontrado no namespace local ou global')
    except KeyError:
        print('Chave especificada não é encontrada no Dicionário')


url_search()
# FOR UTILIZADO PARA LER 3  VEZES O ARQUIVO "armazena_extracao.txt" COM  INSERÇÕES DIFERENTE DO USUÁRIO
for i in range(6):
    retorno = abertura()
    palavra = analise(retorno)
    try:
        lista1, lista2, pos = procura_armazenamento(retorno, palavra)
        grafico(lista1, lista2, pos)
    except TypeError:
        print('Objeto não é iterável')
