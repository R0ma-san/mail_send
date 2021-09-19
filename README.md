1)Создайте файл config.py и введите туба email = 'Ваш почтовый адрес' и password = 'Пароль от почтового адреса'
В файле send_email.py :
2)В строке to_email  введите почтовый адрес получателя
3)В строке massage  введите сообщение
4)Если у вас почта gmail поменяйте server = smtplib.SMTP('smtp.mail.ru: 25') на server = smtplib.SMTP('smtp.gmail.com: 587')