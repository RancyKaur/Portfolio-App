import smtplib
import ssl,os

def send_email(message):
    useremail="iamrancy@gmail.com"
    password = "goyynobxosacaasu" #os.getenv("MYAPPPWD")
    host = "smtp.gmail.com"
    port = 465
    receiver1 = "iamrancy@gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(useremail, password)
        server.sendmail(useremail, receiver1, message)
