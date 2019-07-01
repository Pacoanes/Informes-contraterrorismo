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
    print("Informe generado.")
    t = input("¿Quieres recibirlo por mail? [Y/n] ")
    if t == "no" or t=="No" or t=="N" or t=="n":
        print("Informe no enviado, gracias.")
        return
    else:
        to = input("Escribe tu correo electrónico --> ")
    #conectando
        try:  
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)

            print("Conectando al servidor SMTP")
        except:  
            print("Algo no esta funcionando bien...")
            
        #crear mensaje
        message = MIMEMultipart('alternative')
        message['Subject'] = 'informe de Contraterrorismo'
        message['From'] = 'Servicio de inteligencia Ironhack'
        message.attach(MIMEText('Buenos dias, tal y como ha pedido, le enviamos el informe generado de Contraterrorismo'))

        filename='informe.pdf'
        fo=open(filename,'rb')
        attach = MIMEApplication(fo.read(),_subtype="pdf")
        fo.close()
        attach.add_header('Content-Disposition','attachment',filename=filename)
        
        # Attachment and HTML to body message.
        message.attach(attach)
        print("Email enviado, gracias.")
        server.sendmail(gmail_user, to, message.as_string())
        # Close connection
        server.close()
        return