import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()

email['from'] = 'Kuba Walczak'
email['to'] = 'jakubwalczak8@gmail.com'
email['subject'] = 'Wygrales pythona' # tytuł maila

email.set_content(html.substitute(name = 'Tintin'),'html') # treść maila

with smtplib.SMTP(host= 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('kubapython8@gmail.com', 'gigabyte0')
    smtp.send_message(email)
    print('all good')