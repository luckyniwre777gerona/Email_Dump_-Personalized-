import os
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


smtp_ssl_host = 'smtp.gmail.com'         # mail server host e.g smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'lucky777pogi@gmail.com'      # email address / usename of account
password = '*********'                   # password enables log-in
sender = 'lucky777pogi@gmail.com'        # same as email adress / usename. used in sending
targets = ['geronaerwinray@gmail.com', 'lucky.gerona@eee.upd.edu.ph'] # list all receipients. Can be as long as you want
target_company_name = ['BADING KA', 'GWAPO AKO']                      # These are company names for each item in recepient. This makes emails seem more personalized    


# enable email protocol
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)

# start sending
for i in range(len(targets)):

	msg = MIMEMultipart()

	#This is written in the subject header. The personalized company name can be used here
	msg['Subject'] = 'Partnership Deal for ' + target_company_name[i] + 'for kabaklaan ng music circle the talented org'
	
	#This is written in the sender (which is you)
	msg['From'] = sender

	#This is written in the target recepient. Goes through the list and sends the email
	msg['To'] = targets[i]

	#This is additional info. This will be the ssasme for all copanies.
	txt = MIMEText('Common txt for all')
	msg.attach(txt)


	#If you need attachments. GOING.pdf is an example.
	filepath = 'GOING.pdf'

	with open(filepath, "rb") as f:
	    PDF = MIMEApplication(f.read(), _subtype = "pdf")

	PDF.add_header('Content-Disposition',
	               'attachment',
	               filename=os.path.basename(filepath))
	msg.attach(PDF)
	# end of pdf example

	# This sends the mail
	server.sendmail(sender, targets[i], msg.as_string())


# Quits after sending all
server.quit()