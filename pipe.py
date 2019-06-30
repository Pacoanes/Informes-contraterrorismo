import adquirir
import enriquecer
import limpiar
import reportar
import analisis
import generar_pdf
import gmail

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

def graficos(bd):
    gra=analisis.grafico_barras("gname",bd.gname.value_counts()[:15].index,'bandas.png','Actos cometidos por cada organización en {}'.format(npais))
    gra=analisis.grafico_barras("attacktype1_txt",bd['attacktype1_txt'].value_counts().index, 'metodos.png', 'Metodo preferido por los terroristas en {}'.format(npais))
    gra=analisis.grafico_vs
    return 

def pdf(pdf):
    x=generar_pdf.crearpdf
    return pdf

def enviaremail(mail):
    mail=gmail.conectar_mail
    return mail

miscrap=scrapeo()
midata = leer("gtd.csv")
dd = (limpiarcositas(midata))
merge=adquirir.mergear(miscrap,dd,'paises','country_name')
entra=report(merge)
gr=graficos(entra)


