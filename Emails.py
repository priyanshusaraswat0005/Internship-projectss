import smtplib
import ssl
from email.message import EmailMessage
EMAIL = "..."
APP_PASSWORD = "**** **** **** ****"
RECEIVER = "..."
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "or bta bete ky chal rha hai ....."
msg.set_content("ky re bete ky haal hai re......")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)