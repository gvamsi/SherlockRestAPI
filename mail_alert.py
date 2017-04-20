#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sbhar
#
# Created:     14/12/2016
# Copyright:   (c) sbhar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import smtplib,getpass
from email.mime.multipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders

def sendMail(toMailId, name,latitude, longitude, cityName):
    mailTo=toMailId

    sender="vamsiholmes@gmail.com"
    s=smtplib.SMTP("smtp.gmail.com",587)
    s.ehlo()
    s.starttls()
    pwd='vamsirocks'
    s.login(sender,pwd)


    msg=MIMEMultipart()
    msg["From"]=sender
    msg["To"] = mailTo
    msg['Subject']="Is your phone safe?"

    bodyText='''Hi '''+name+''',

         I detected some suspicious activity in your phone. In case it is lost, it is at Latitude '''+str(latitude)+''', Longitude '''+str(longitude)+''', City Name'''+cityName+'''.

Regards,
Sherlock'''

    body=MIMEText(bodyText)
    msg.attach(body)
    s.sendmail(msg["From"],msg["To"],msg.as_string())
    s.close()
    #s.quit()

def main():
    sendMail('sbharathkumar92@gmail.com','Bharath', '111.23', '-37.45', 'Tempe')

if __name__ == '__main__':
    main()
