#menu
import login
import rconnector as ms
mycon = ms.connect(host='db4free.net', user='clairie', passwd='education', charset='utf8', database='skytouch')

print('connected!')
mycursor = mycon.cursor()
mycursor.execute('select * from login_info;')
login_data = mycursor.fetchall()
mycursor.execute("select * from reg;")
reg_data = mycursor.fetchall()
print('WELCOME TO SKYTOUCH!!')
print('See the Unseen!!')
print("Press 1 to login")
print("New User? Register Now. Press 2")
ch=input('>>> ')

if ch=='1':
    login.verify()
elif ch=='2':
    register.fun()





# import smtplib
# import random
#
# # create smtp session
# s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
# # start TLS for E-mail security
# s.starttls()
# # Log in to your gmail account
# s.login("hanumimassey222@gmail.com", "lauramassey")
# otp = random.randint(1000, 9999)
# otp = str(otp)
#
# s.sendmail("hanumimassey222@gmail.com", 'ritu.kansal456@gmail.com', otp)
# print("OTP sent succesfully..")
# # close smtp session
# s.quit()