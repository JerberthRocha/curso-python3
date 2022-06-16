from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='Maria', data=data_atual)

mensagem_email = MIMEMultipart()
mensagem_email['from'] = 'Jerberth Rocha Silva'
mensagem_email['to'] = meu_email # email(s) destinatário(s)
mensagem_email['subject'] = 'Atenção: este é um e-mail de teste.'

corpo = MIMEText(corpo_msg, 'html')
mensagem_email.attach(corpo)

with open('imagem.jpg', 'rb') as imagem:
    imagem = MIMEImage(imagem.read())
    mensagem_email.attach(imagem)


with smtplib.SMTP(host='smtp.google.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha) # e-mail e senha do remetente
        smtp.send_message(mensagem_email)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('Não foi possível enviar o e-mail.')
        print('Erro:', e)