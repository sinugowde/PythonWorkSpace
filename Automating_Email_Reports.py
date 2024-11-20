import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv, dotenv_values

# loading variables from .env file
load_dotenv()


def send_email(subject, body, to_email):
    sender_email = os.getenv("GMAIL_ID")
    sender_password = os.getenv("GMAIL_APP_PASS")
    receiver_email = to_email

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

subject = 'Monthly Report1'
body = 'Here is the monthly report.'

send_email(subject, body, 'sinu.gowde@gmail.com')