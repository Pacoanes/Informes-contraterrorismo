import requests as req
from bs4 import BeautifulSoup

def scrapear(url, css):
    res = req.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    ss = soup.select(css)
    lista=list(map(lambda x : x.text.strip(),ss))
    return lista

def seleccionar(lista, desde, cada_cuanto):
    return lista[desde::cada_cuanto]

def limitar(lista, fin):
    return lista[:fin]
