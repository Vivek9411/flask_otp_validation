from email.message import EmailMessage
import smtplib
import random
from random import choice
import time
import ssl
# workd only for gmail
PASSWORD ='googleapppassword'
email_sender = 'gmail@address.com'


#use this or choose each digit of otp 
class generate_otp:
    def __init__(self):
        self.otp = random.randint(110000, 999999)

    def get_otp(self):
        return self.otp



class send_mail:
    def __init__(self,email, body):
        self.email = email

        self.body =  body
        self.sendmail()

    def sendmail(self):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=email_sender, password=PASSWORD)
        connection.sendmail(from_addr=email_sender, to_addrs=self.email, msg=self.body)
        connection.close()

