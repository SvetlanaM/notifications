import smtplib
from email.mime.text import MIMEText
from smtplib import SMTP
from smtplib import SMTPException
import sys
from sql import *
from sql.aggregate import *
from sql.conditionals import *
from datetime import date, timedelta

EMAIL_SUBJECT = "Notification from povinnosti.com"
EMAIL_FROM = "notification@povinnosti.com"
EMAIL_RECEIVERS = user.select(user.id, user.name) #alebo iba (user.name)
message = pokuta.select(pokuta.message)
notify = datetime.today()-timedelta(days=3)
"""Nastavenie pre gmail
"""
GMAIL_SMTP = "smtp.gmail.com"
GMAIL_SMTP_PORT = 587


def send_email(msg):
    msg_header = "From: " + EMAIL_FROM + "\n" + \
                 "To: " + listToStr(EMAIL_RECEIVERS) + "\n" + \
                 "Subject: " + EMAIL_SUBJECT + "\n"
    msg_body =  message
 
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(EMAIL_FROM, EMAIL_RECEIVERS, msg_body)
        smtpObj.quit()
    except SMTPException as error:
      print "Error: unable to send email :  {err}".format(err=error)
 
def main():
    if notify == True :
        send_email("Email was sent to") + listToStr(EMAIL RECEIVERS) + "\n";
 
if __name__ == "__main__":
    main()