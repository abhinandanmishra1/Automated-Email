#before importing install pdf-mail  #pip install pdf-mail #only one function email_send()
#email_send():: It will send the pdf document from your Gmail account to another Gmail account .
from pdf_mail import sendpdf
sender_email_address = "allexamsnotifications@gmail.com"
receiver_email_address = "jaihindustanabhi@gmail.com"
sender_email_password = input("Enter Your Password")
subject_of_email = "Sending Pdf"
body_of_email = "You're Awesome"
filename ="abhim"
location_of_file = "C:/Users/lp/Desktop"
# Create an object of sendpdf function
k = sendpdf(sender_email_address,
			receiver_email_address,
			sender_email_password,
			subject_of_email,
			body_of_email,
			filename,
			location_of_file)
k.email_send()    #used to send pdfs
print("Success")
