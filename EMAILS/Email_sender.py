import smtplib
from email.message import EmailMessage




email = EmailMessage()
email["from"] = "Piotr Koma"
email["to"] = "magdalenakomaa@gmail.com"
email["subject"] = "Python"

email.set_content("Hi i m writing to you to say that you suck at python")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("piotrkoma41@gmail.com","mytbbucijsjeyufs")
    smtp.send_message(email)
    print("all good !")

