import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import email, password

msg = MIMEMultipart()

#Email получателя
to_email = '#'
#Cообщение
massage = 'Какое-то сообщение'

msg.attach(MIMEText(massage, 'plain'))

server = smtplib.SMTP('smtp.mail.ru: 25')
server.starttls()
server.login(email, password)
server.sendmail(email, to_email, msg.as_string())
server.quit()