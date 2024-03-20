import smtplib, ssl
import sys

smtp_address = "smtp.gmail.com"
smtp_port = 465

sender_email = "burenarthur@gmail.com"
sender_password = "qpea hnfu voqt htsx"

email_receiver = "burenarthur@gmail.com"



with open("mail/mail.txt", "r") as file:
    message = file.read()


if "cpu" in sys.argv :
    message += """\
    - The CPU usage is above 90%"""
    
if "ram" in sys.argv :
    message += """\
    - The RAM usage is above 90%"""
    
if "disk" in sys.argv :
    message += """\
    - The disk usage is above 90%"""

if "number_of_users" in sys.argv :
    message += """\
    - The number of users connected is above 5"""

if "nbr_process" in sys.argv :
    message += """\
    - The number of processes is above 100"""







context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, email_receiver, message)