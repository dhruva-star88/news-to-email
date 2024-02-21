import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    user_id = "workdhruvateja@gmail.com"
    password = os.getenv("news_app_password")
    receiver = "dhruvatej6565@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_id, password)
        server.sendmail(user_id, receiver, message)

