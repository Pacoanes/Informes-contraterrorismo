import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests as req
from bs4 import BeautifulSoup

import adquirir
import enriquecer
import limpiar
import reportar

def leer(file):
    midata = adquirir.cargardatos(file)
    return midata

def limpiarcositas(midata):
    midata=limpiar.eliminar_columnas(midata,'Unnamed: 0')
    midata=limpiar.eliminar_columnas(midata,'vicinity')
    midata=limpiar.renombrar(midata,'country_txt','country_name')
    midata=limpiar.renombrar(midata,'nkill','muertos')
    midata=limpiar.renombrar(midata,'nwound','heridos')
    midata=limpiar.columna_de_sumar_dos(midata,"afectados","muertos","heridos")
    return midata

def scrapeo():
    pais=enriquecer.scrapear('https://countrycode.org','tr td a')
    poblacion=enriquecer.scrapear('https://countrycode.org','tr td')
    pib=enriquecer.scrapear('https://countrycode.org','tr td')
    pob1=enriquecer.seleccionar(poblacion,3,6)
    pib1=enriquecer.seleccionar(pib,5,6)
    pob1=enriquecer.limitar(pob1,240)
    pib1=enriquecer.limitar(pib1,240)
    pais=enriquecer.limitar(pais,240)
    miscrap=adquirir.nuevodf()
    miscrap=adquirir.rellenar_nuevodf(miscrap,"paises",pais)
    miscrap=adquirir.rellenar_nuevodf(miscrap,"poblacion",pob1)
    miscrap=adquirir.rellenar_nuevodf(miscrap,"pib",pib1)
    return miscrap

def reportar(repo):
    repo=reportar.verpaises
    repo=reportar.elegirpais
    mensaje=reportar.pildora_pais
    


miscrap=scrapeo()
midata = leer("gtd.csv")
dd = (limpiarcositas(midata))
merge=adquirir.mergear(miscrap,dd,'paises','country_name')
print(merge.shape)




