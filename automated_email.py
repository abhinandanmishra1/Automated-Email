import psycopg2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import date

passe=input("Enter Your password of Email :")
#database ---->>>> email fetching
conn = psycopg2.connect(database="AutoEmail", user = "postgres", password = passe, host = "127.0.0.1", port = "5432")
print("jai hind")


cur = conn.cursor()

cur.execute("SELECT FIRST_NAME,EMAIL,LAST_EMAIL_SENT,ID from Students where year='TH'")
rows = cur.fetchall()
for row in rows:

    fromaddr = "abhinandanmishra360@gmail.com"
    toaddr = row[1]
    name=row[0]

    today = date.today()
   # today = (today.year, today.month, today.day)
    total_days=today-row[2]
    if(total_days.days<30):
        continue
    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Appreciate Your Work"

    # string to store the body of the mail
    body = '''Hello {} 
    I'm sending this Email To you because you're doing great for 
    Exams Notifications.
    We appreciate your work and dedication .
    We're not at any position to give you something but my words are with you.
        
    As soon as we start earning , You will get perks from us.
    BE CONNECTED WITH US
        
    Thanks
    Regards 
    Abhinandan Mihsra
    (YOUR FRIEND)'''.format(name)

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = "CEO_FOUN.jpg"
    attachment = open("C:/Users/lp/Downloads/Screenshots/real_logo.jpg", "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com:587')

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, passe)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    print("Email Sent To ->" + toaddr)
    datetime_current = date.today()
    #datetime_current=( datetime_current.year, datetime_current.month, datetime_current.day)
    #cur.execute("INSERT INTO Students  (LAST_EMAIL_SENT) VALUES (datetime_current) ")
    s.quit()
conn.commit()
print("Records created successfully")

conn.close()

