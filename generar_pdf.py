import pandas as pd
import time
from fpdf import *  
import reportar

def crearpdf(df):
    npais=df.country_name.value_counts().index[0]
    tiempo=time.asctime(time.localtime(time.time()))
    cel=df.gname.value_counts().index[0]
    anho=df.iyear.value_counts().index[0]
    num=df.iyear.value_counts().values[0]
    ratio_anho=round(8760/num)
    if cel=="Unknown":
        cel=df.gname.value_counts().index[1]
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
    pdf.cell(10, 140,"· Peor año de {} fue {}. Año donde había un atentado cada {} horas.".format(npais,anho,ratio_anho))
    pdf.cell(-10)
    pdf.cell(10, 150,"· Principal grupo organizado: {}.".format(cel))
    pdf.cell(-10)
    pdf.cell(10, 160,"· Probabilidad x cada 100k habitantes de sufrir un atentado: {}.".format(npais))
    pdf.cell(-10)
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(10, 180,"Nota al lector:")
    pdf.set_font('Arial', '', 12)
    pdf.cell(-10)
    pdf.cell(10, 195,"Los actos violentos perpetrados por organizaciones no estatales contra la población general")
    pdf.cell(-10)
    pdf.cell(10, 205,"con fines políticos son delitos aberrantes que, cuando tienen carácter generalizado") 
    pdf.cell(-10)
    pdf.cell(10, 215,"o sistemático, pueden constituir crímenes contra la humanidad")
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
    pdf.image('metodos.png', x=10, y=130, w=200, h=70, type = '', link = '')
    pdf.output('informe.pdf', 'F')
    return  