import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
sender = input("your email")
s.login(sender, input("Enter Password"))
message = "sup man hows it going in bangalore. its hot over here in hyd"
s.sendmail(sender, sender,message)
s.quit()
