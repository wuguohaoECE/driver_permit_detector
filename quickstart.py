import requests
import time
import json
from datetime import datetime
url = "https://skiptheline.ncdot.gov/Webapp/WizardAppt/DateandTime"


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

cities_list = [
  {'Cookie': '_ga=GA1.2.1679529248.1634670435; _ga_PJ9DRVJT4V=GS1.1.1635951113.2.1.1635951131.0; ASP.NET_SessionId=ryiggp4livsic0vr2nowxnzw'}
]


import smtplib
from email.header import Header
from email.mime.text import MIMEText

mail_host = "smtp.163.com"
mail_user = "wqgy74"
mail_pass = "your_password"
sender = "wqgy74@163.com"
receivers = ["receiver1@gmail.edu","receiver2@gmail.com"]

content = "content"
title = "permit update"

def sendEmail(content):
    message  = MIMEText(content, 'plain', 'utf-8')
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("mail has beed sent")
    except smtplib.SMTPException as e:
        print(e)

while(1):
    time.sleep(20)
    for city in cities_list:
        headers.update(city)
        response = requests.request("GET", url, headers=headers)
        content = response.text
        startIndex = content.index('arrayAvailableDates.push([')
        content = content[startIndex:]
        endIndex = content.index(']')
        date_time_str = content[len('arrayAvailableDates.push([')+1:endIndex-1]
        date_time_obj = datetime.strptime(date_time_str, '%m/%d/%Y')
        if(date_time_obj.month != 1):
            content = "new vacancy on " + str(date_time_obj.month) + "/" + str(date_time_obj.day) + " on " + response.text.split('\n')[120]
            print(content)
            sendEmail(content)
    print("update")