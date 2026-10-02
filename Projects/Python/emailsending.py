import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("pranjal2008goyal@gmail.com", "pranjalgoyal2008")
server.sendmail("pranjal2008goyal@gmail.com", "amazingpranjal2008@gmail.com", "Hello, how are you? This is a automated message")
server.quit()