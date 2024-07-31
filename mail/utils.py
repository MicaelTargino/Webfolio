import smtplib
from typing import Literal
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from portfolio.settings import SENDER_MAIL, MAIL_PASSWORD
def send_email(name, email, subject, body):  

    print(SENDER_MAIL, MAIL_PASSWORD)

    RECEIVER_MAIL = 'micaelgomestargino@gmail.com' # need to come from logged user information

    message = MIMEMultipart()
    message["From"] = SENDER_MAIL
    message["To"] = RECEIVER_MAIL
    message["Subject"] = subject if subject else f'Email from {name}'

    body = f'{body} \n\n {name} - {email}'

    message.attach(MIMEText(body, "plain"))
    server = smtplib.SMTP("smtp.gmail.com", 587) 
    server.starttls()
    server.login(SENDER_MAIL, MAIL_PASSWORD)
    text = message.as_string()
    server.sendmail(SENDER_MAIL, RECEIVER_MAIL, text)
    server.quit()