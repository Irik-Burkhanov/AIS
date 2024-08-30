import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Ввод логина, пароль и кому направленно письмо
fromaddr = ""
toaddr = ""
password = ""

# Создание сообщения
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Лабараторная работ 3"

body = "Лаба по АИС #3"
msg.attach(MIMEText(body, 'plain'))

# Подключение к серверу mail.ru
server = smtplib.SMTP('smtp.mail.ru', 25)
server.starttls()

# Вход в аккаунт
server.login(fromaddr, password)

# Отправка сообщения
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
print('\nПисьмо доставлено на адрес ' + toaddr + '\n')

# Закрытие соединения
server.quit()