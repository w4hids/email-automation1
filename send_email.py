import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
PORT = 465  # SSL Port

# Credentials from GitHub Secrets
USERNAME = os.environ.get("EMAIL_USER")
PASSWORD = os.environ.get("EMAIL_PASS")

# Email Recipients (Unique)
recipients = list(set([
    "samaniwahiduddin382@gmail.com",
    "singhshreya9445@gmail.com"
]))

# Email Subject
subject = "Daily Expense Reminder: Log Your Spending Today"

# Email Body (HTML)
body = """\
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            background: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            margin: auto;
        }
        h2 {
            color: #2c3e50;
            text-align: center;
        }
        p {
            font-size: 16px;
            color: #555;
            line-height: 1.6;
        }
        .footer {
            margin-top: 20px;
            font-size: 14px;
            color: #777;
            text-align: center;
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            margin: 20px 0;
            font-size: 16px;
            color: #ffffff;
            background-color: #007bff;
            text-decoration: none;
            border-radius: 5px;
            text-align: center;
        }
        .button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>📌 Daily Expense Reminder</h2>
    <p>Dear User,</p>
    <p>This is a friendly reminder to log your daily expenses to keep track of your financial health.</p>
    <p>Regularly updating your expenses will help you stay within budget and make informed financial decisions.</p>
    
    <p style="text-align: center;">
        <a href="YOUR_WEBSITE_LINK" class="button">Log Your Expenses</a>
    </p>
    
    <div class="footer">
        <p>Best Regards,</p>
        <p>FinCascade Team</p>
    </div>
</div>

</body>
</html>
"""

# Create SSL context
context = ssl.create_default_context()

# Sending email
try:
    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        server.login(USERNAME, PASSWORD)

        for recipient in recipients:
            msg = MIMEMultipart()
            msg["From"] = USERNAME
            msg["To"] = recipient
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "html"))

            server.sendmail(USERNAME, recipient, msg.as_string())
            print(f"✅ Email sent to {recipient}")

    print("✅✅✅ All emails sent successfully!")
except Exception as e:
    print(f"❌ Error sending emails: {e}")
    
