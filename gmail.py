import smtplib
import getpass
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
from dotenv import load_dotenv
load_dotenv()

email = os.environ["correo"]
contraseña = os.environ["password"]

def conectar_mail():
    gmail_user = email
    gmail_password = contraseña
    #conectando
    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        print("Conectando al servidor SMTP")
    except:  
        print("Algo malo esta pasando...")
        
    #crear mensaje
    message = MIMEMultipart('alternative')
    message['Subject'] = 'informe de Contraterrorismo'
    message['From'] = 'Servicio de inteligencia Ironhack'
    message.attach(MIMEText('Buenos dias, tal y como ha pedido, le enviamos el informe generado de Contraterrorismo'))

    # añadiendo pdf
    filename='informe.pdf'
    fo=open(filename,'rb')
    attach = email.mime.application.MIMEApplication(fo.read(),_subtype="pdf")
    fo.close()
    attach.add_header('Content-Disposition','attachment',filename=filename) 
    message.attach(attach)
    to = input("¿Quieres recibirlo por mail? Escribe tu correo electrónico --> ")
    server.sendmail(gmail_user, to, message.as_string())
    # Close connection
    server.close()
    return