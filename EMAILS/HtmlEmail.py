import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Piotr Koma"
email["to"] = "magdalenakomaa@gmail.com"
email["subject"] = "Python"

email.set_content(html.substitute({"name":"TinTin"}),"html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("piotrkoma41@gmail.com","mytbbucijsjeyufs")
    smtp.send_message(email)
    print("all good !")

