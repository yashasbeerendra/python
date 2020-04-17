import smtplib
from email.message import EmailMessage
email = EmailMessage()
email['from'] = 'Your lover'
email['to'] = 'k.adarshsonu2000@gmail.com'
email['subject'] = 'INTROduction'
email.set_content(
    'hello adarsh i just sent you this mail without logging into my account .STAY HOME STAY SAFE')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('yashasbeerendra2001@gmail.com', 'yashas2001')
    smtp.send_message(email)
    print('all good')
