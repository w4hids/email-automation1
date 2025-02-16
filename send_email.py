import smtplib
import ssl
import os

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
PORT = 465  # SSL Port

# Credentials from GitHub Secrets
USERNAME = os.environ.get("EMAIL_USER")
PASSWORD = os.environ.get("EMAIL_PASS")

# Email Recipients (Add as many as needed)
recipients = [
    "samaniwahiduddin382@gmail.com",
    "singhshreya9445@gmail.com",
    "singhshreya9445@gmail.com",
    "singhshreya9445@gmail.com",
    "singhshreya9445@gmail.com"
]

# Email Message
subject = "Attendance Reminder"
body = """\
Dear Student,

We have noticed irregular attendance in your classes. Regular attendance is vital for your academic progress and overall success.

If you are facing any challenges, feel free to reach out for support. Please ensure regular attendance moving forward.
"""

message = f"Subject: {subject}\n\n{body}"

# Create SSL context
context = ssl.create_default_context()

# Send email to all recipients
try:
    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        server.login(USERNAME, PASSWORD)
        for recipient in recipients:
            server.sendmail(USERNAME, recipient, message)
            print(f"Email sent to {recipient}")

    print("All emails sent successfully!")
except Exception as e:
    print(f"Error sending emails: {e}")
