import pandas as import pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter

def elegirpais():
    print("Bienvenido al generador de informes sobre Contraterrorismo")
    while True:
        try:
            npais = str(input("elige el pais en inglés: ").capitalize())
            if npais in comprobar: 
                print("generando informe sobre {}...".format(npais))
                break
            else: raise TypeError
        except TypeError:
            print("Escribe bien el pais.")
            continue 
    bd=merge[merge["country_name"]==npais]            
    return bd

def verpaises():
    print("quieres saber los paises disponibles?")
    comprobar=list(set(merged.country_name.values))
    while True:
        try:
            
            x = str(input("[Y/n]: ").lower())
            if x=="y" or x=="yes" or x=="s" or x=="si": 
                print(', '.join(comprobar))
                break
            elif x=="n" or x=="no":
                break
            else: raise TypeError
        except TypeError:
            print("Escribe bien si o no.")
            continue 
    return

def pildora_pais():
    anho=bd.iyear.value_counts().index[0]
    num=bd.iyear.value_counts().values[0]
    ratio_anho=round(8760/num)
    return print("¿Sabias que el peor año de {} fue {} donde habia un ataque cada {} horas de media?".format(npais,anho,ratio_anho))

def generar_pdf():
    