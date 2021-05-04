import smtplib
from email.mime.text import MIMEText

def send_welcome_email(to, firstName, lastName):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '8ef70ac989fce3'
    password = 'ca7b9a9a1490f5'
    message = f"<h3>Welcome {firstName} {lastName}!</h3><div>You have successfully registered!</div>"
    sender_email = "admin@rizwanminhas.com"
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Welcome email.'
    msg['From'] = sender_email
    msg['to'] = to

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, to, msg.as_string())