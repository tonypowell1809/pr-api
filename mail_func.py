'''
This is an example of a mail function that could be used for mailing the report.
'''

import smtplib
from email.mime.text import MIMEText



def send_email(recipients, subject, body):
    email_username = 'yourrelayuser@example.com'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = f'no-reply <no-reply@powell.io>'
    msg['To'] = recipients
    msg = msg.as_string()

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(email_username, 'xxxxxxxxx')
    session.sendmail(email_username, recipients, msg)
    session.quit()

to = "tony.powell22@outlook.com"
subj = "Showing an email example"
message  = "Data for the message as an example"

send_email(to,subj,message)






