import smtplib
sender_email="rithiksharma27@gmail.com"
rec_email="rithiksharma27@gmail.com"
password="password"
message="hey ,Accuracy greater than 80 percent has been acheived "
server=smtplib.SMTP("smtp.gmail.com",587) 
server.starttls()
server.login(sender_email,password)
print("Login success")
server.sendmail(sender_email,rec_email,message)
print("Email  has been sent")
