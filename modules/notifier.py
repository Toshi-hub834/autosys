import smtplib
from email.message import EmailMessage

def send_email(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = "autosys@localhost"
    msg['To'] = to

    with smtplib.SMTP('localhost') as s:
        s.send_message(msg)
