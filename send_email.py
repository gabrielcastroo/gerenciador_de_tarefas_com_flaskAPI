import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(email_to_send, text_to_send):
    host = "smtp.gmail.com"
    port = "587"
    login = "gerenciadordetarefasdev@gmail.com"
    password = "flaskapi55"

    server = smtplib.SMTP(host, port)
    server.starttls()
    server.login(login, password)

    subject = "Olá, você tem uma tarefa - Enviado de Gerenciador de Tarefas "

    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_to_send
    email_msg['Subject'] = subject
    email_msg.attach(MIMEText(text_to_send,'plain'))

    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

    server.quit()
