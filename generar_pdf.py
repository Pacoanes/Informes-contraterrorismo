import pandas as pd
import time
import requests as req 
from fpdf import *  
import reportar
import os
from dotenv import load_dotenv
load_dotenv()

api_key_nyt = os.environ["api_nyt"]   
ap1 = os.environ["api_g"] 
ap2 = os.environ["cse_id"]  

def crearpdf(df):
    npais=df.country_name.value_counts().index[0]
    nciudad=df.provstate.value_counts().index[0]
    tiempo=time.asctime(time.localtime(time.time()))
    cel=df.gname.value_counts().index[0]
    anho=df.iyear.value_counts().index[0]
    num=df.iyear.value_counts().values[0]
    ratio_anho=round(8760/num)
    afecta = df.gname.value_counts().sum()
    pob =int(df.poblacion.value_counts().index[0].replace(",",""))
    ratio=round(afecta/pob, 6)
    ratio
    if cel=="Unknown":
        cel=df.gname.value_counts().index[1]

    #conectar con la api de NYT
    key = api_key_nyt
    res = req.get("https://api.nytimes.com/svc/search/v2/articlesearch.json?q={} {}&sort=newest&api-key={}".format(npais,cel,key))
    nyt=res.json()
    url=nyt["response"]["docs"][0]["web_url"]
    title=nyt["response"]["docs"][0]["headline"]["main"]
    date=nyt["response"]["docs"][0]["pub_date"].strip(" ")[:10]

    #conectar api google 

    rest = req.get("https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}&searchType=image".format(ap1,ap2,cel))
    goo=rest.json()
    ima=goo["items"][0]["link"]
  
    
    ext= ima[-3:] 
    if ext=="jpg":
        picture = req.get(ima)
        if picture.status_code == 200:
            with open("image.jpg", 'wb') as f:
                f.write(picture.content)
    elif ext=="png":
        picture = req.get(ima)
        if picture.status_code == 200:
            with open("image.png", 'wb') as f:
                f.write(picture.content)

    #empieza pdf
    pdf=FPDF()                   
    pdf.add_page()                         
    pdf.set_font('Arial', 'B', 16)
    pdf.image('logo.png', x=20, y=20, w=25, h=25, type = '', link = '')
    pdf.cell(60) 
    pdf.cell(70, 80, 'Informe de Contraterrorismo')       
    pdf.line(5, 55, 200, 55)
    pdf.set_font('Arial', '', 12)
    pdf.cell(-20)  
    pdf.cell(20, 100, 'pais: {}'.format(npais))
    pdf.cell(-120)
    pdf.cell(20, 110, 'fecha: {}'.format(tiempo))
    pdf.cell(60)  
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(-80)
    pdf.cell(10, 125, 'Puntos clave del informe')
    pdf.set_font('Arial', '', 12)
    pdf.cell(-10)
    pdf.cell(10, 140,"· Peor año de {} fue {}. Año donde había un atentado cada {} horas de media.".format(npais,anho,ratio_anho))
    pdf.cell(-10)
    pdf.cell(10, 150,"· Principal grupo organizado: {}.".format(cel))
    pdf.cell(-10)
    pdf.cell(10, 160,"· Estado/provincia con mayor más atentados: {}.".format(nciudad))
    pdf.cell(-10)
    pdf.cell(10, 170,"· La probabilidad media de sufrir un atentado en {} es de: {}.".format(npais,ratio))
    pdf.cell(-10)
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(10, 190,"Nota al lector:")
    pdf.set_font('Arial', '', 12)
    pdf.cell(-10)
    pdf.cell(10, 205,"Los actos violentos perpetrados por organizaciones no estatales contra la población general")
    pdf.cell(-10)
    pdf.cell(10, 215,"con fines políticos son delitos aberrantes que, cuando tienen carácter generalizado") 
    pdf.cell(-10)
    pdf.cell(10, 225,"o sistemático, pueden constituir crímenes contra la humanidad")
    pdf.image('bandas.png', x=10, y=130, w=200, h=70, type = '', link = '')
    pdf.image('metodos.png', x=10, y=210, w=200, h=70, type = '', link = '')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.image('logo.png', x=20, y=20, w=25, h=25, type = '', link = '')
    pdf.cell(60) 
    pdf.cell(70, 80, 'Informe de Contraterrorismo')       
    pdf.line(5, 55, 200, 55)
    pdf.set_font('Arial', '', 12) 
    pdf.cell(60)  
    pdf.set_font('Arial', '', 12)
    pdf.image('ataques.png', x=10, y=60, w=200, h=70, type = '', link = '')
    #pdf.image('metodos.png', x=10, y=130, w=200, h=70, type = '', link = '')
    pdf.image('meses.png', x=10, y=200, w=200, h=70, type = '', link = '')
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    pdf.image('logo.png', x=20, y=20, w=25, h=25, type = '', link = '')
    pdf.cell(60) 
    pdf.set_font('Arial', '', 16)
    pdf.cell(70, 80, 'Informe de Contraterrorismo')       
    pdf.line(5, 55, 200, 55)
    pdf.set_font('Arial', '', 12)
    pdf.image('años.png', x=10, y=60, w=200, h=70, type = '', link = '') 
    pdf.image('paises.png', x=10, y=140, w=200, h=70, type = '', link = '') 
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    pdf.image('logo.png', x=20, y=20, w=25, h=25, type = '', link = '')
    pdf.cell(60) 
    pdf.set_font('Arial', '', 16)
    pdf.cell(70, 80, 'Informe de Contraterrorismo')       
    pdf.line(5, 55, 200, 55)
    pdf.set_font('Arial', '', 12)
    pdf.cell(-110)
    pdf.cell(10, 110, 'Enlace a última noticia en New York Times publicado el {}'.format(date)) 
    pdf.cell(-20)
    pdf.cell(-100, 125,"Título: {}".format(title)) 
    pdf.cell(90)
    pdf.cell(70, 140,"Enlace: {}".format(url), link = url) 
    pdf.cell(10)
    pdf.image('image.{}'.format(ext), x=40, y=120, w=100, h=100, type = '', link = ima)
    pdf.output('informe.pdf', 'F')
    return  