# -*- coding: utf-8 -*-
import adquirir
import enriquecer
import limpiar
import reportar
import analisis
import generar_pdf
from gmail import *

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

def report(x):
    repo=reportar.verpaises(x)
    bd=reportar.elegirpais(x)
    return bd

def graficos(df,df1):
    gra=analisis.grafico_barras(df,"gname",df.gname.value_counts()[:15].index,'bandas.png','Actos cometidos por cada organización en {}')
    gra=analisis.grafico_barras(df,"attacktype1_txt",df['attacktype1_txt'].value_counts().index, 'metodos.png', 'Metodo preferido por los terroristas en {}')
    gra=analisis.grafico_barras(df,"iyear", None, 'años.png', 'Acciones terroristas en {} por años')
    gra=analisis.grafico_vs(df)
    gra=analisis.nograf(df1)
    gra=analisis.ppalbandaxmes(df)
    return 

def pdf(df):
    x=generar_pdf.crearpdf(df)
    return

def enviaremail():
    mail=conectar_mail()
    return 

def exe():
    miscrap=scrapeo()
    midata = leer("gtd.csv")
    dd = (limpiarcositas(midata))
    merge=adquirir.mergear(miscrap,dd,'paises','country_name')
    entra=report(merge)
    gr=graficos(entra, merge)
    pun=pdf(entra)
    em=enviaremail()

