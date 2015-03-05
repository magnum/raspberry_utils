import os
import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
# Change to your own account information
to = os.environ['SMTP_RECIPIENT']
gmail_user = os.environ['SMTP_USERNAME']
gmail_password = os.environ['SMTP_PASSWORD']
smtpserver = smtplib.SMTP(os.environ['SMTP_HOST'], os.environ['SMTP_PORT'])
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()
# Very Linux Specific
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src')+1]

#my_ip = 'Your ip is %s' %  ipaddr
my_ip = data[0]

msg = MIMEText(my_ip)
msg['Subject'] = 'IP For RaspberryPi on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
