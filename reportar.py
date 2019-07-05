# -*- coding: utf-8 -*-
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter


def elegirpais(df):
    comprobar=sorted(list(set(df.country_name.values)))
    while True:
        try:
            npais = str(input("Para elegir pais escribe su nombre en inglés: ").title())
            if npais in comprobar: 
                print("....")
                print("generando informe sobre {}...".format(npais))
                print("....")
                break
            else: raise TypeError
        except TypeError:
            print("Escribe bien el pais, parfavar...")
            continue 
    comprobar_anho=sorted(list(set(df.iyear.values)))
    while True:
        try:
            anho_inicio = int(input("elige temporada desde: "))
            anho_fin = int(input("al año: "))
            if anho_inicio and anho_fin in comprobar_anho: 
                print("....")
                print("generando informe con estas fechas...")
                print("....")
                break
            else: raise TypeError
        except TypeError:
            print("año mal escrito o no disponible, por favor, vuelve a ecribir el año correcto...")
            continue         
    bd=df[(df["country_name"]==npais) & (df["iyear"]>=anho_inicio) & (df["iyear"]<=anho_fin)]
    anho=bd.iyear.value_counts().index[0]
    num=bd.iyear.value_counts().values[0]
    ratio_anho=round(8760/num)
    print("¿Sabias que el peor año de {} fue {} donde habia un ataque cada {} horas de media?".format(npais,anho,ratio_anho))            
    print("....")
    print("Recolectando datos...")
    print("....")
    print("Accediendo a la API de New York Times...")
    print("....")
    print("Accediendo a la API de Google...")
    print("....")
    print("Generando Informe...")
    print("....")
    return bd

def verpaises(df):
    print("")
    print("........//////                                             \\\\\.......")
    print("Bienvenido al generador de informes sobre Contraterrorismo.")
    print("........\\\\\\                                             /////.......")
    print("")
    print("Para generar el informe elige un pais del mundo.")
    print("¿quieres saber los paises disponibles?")
    comprobar=sorted(list(set(df.country_name.values)))
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

def pildora_pais(df):
    anho=df.iyear.value_counts().index[0]
    num=df.iyear.value_counts().values[0]
    ratio_anho=round(8760/num)
    return print("¿Sabías que el peor año de {} fue {} donde habia un ataque cada {} horas de media?".format(npais,anho,ratio_anho))
    