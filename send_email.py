import smtplib, ssl
import os

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('EMAIL_USER')
PASSWORD = os.environ.get('EMAIL_PASS')
message = """\
Subject: Hi there
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME,USERNAME, message)