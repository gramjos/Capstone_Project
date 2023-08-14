import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pandas as pd

# add logfile path
logs = '../logfile.txt'
with open(logs, 'r') as fd :
    files = fd.readlines()[-14:]

html = f'''
    <html>
        <body>
            <h1>How we serving ?</h1>
            <p>:(</p>
            <p>{files}</p> </body>
    </html>
    '''

def attach_file_to_email(email_message, filename):
    with open(filename, "rb") as f:
        file_attachment = MIMEApplication(f.read())
    file_attachment.add_header( "Content-Disposition", f"attachment; filename= {filename}",)
    email_message.attach(file_attachment)

email_from = 'weather.or.not.its.hot@gmail.com'
password = 'wckkwodjrmajbuuz'
email_to = ['graham.joss@gmail.com', 'bhalala300@gmail.com', 'jpember97@gmail.com', 'kylecstest@gmail.com']

date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = f'Report email - {date_str}'

email_message.attach(MIMEText(html, "html"))

attach_file_to_email(email_message, 'sun.png')
email_string = email_message.as_string()

# Connect to the Gmail SMTP server and Send Email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email_from, password)
    server.sendmail(email_from, email_to, email_string)
