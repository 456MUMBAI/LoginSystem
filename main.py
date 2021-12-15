# MAIN FILE
import temp1
import register
import mysql.connector as ms
import login

mycon = ms.connect(host='db4free.net', user='clairie', passwd='education', charset='utf8', database='skytouch')

# print('connected!')
mycursor = mycon.cursor()
mycursor.execute('select * from login_info;')
login_data = mycursor.fetchall()
print(login_data)
mycursor.execute("select * from reg;")
reg_data = mycursor.fetchall()
print(reg_data)


def menu():
    """Home Page"""
    print('WELCOME TO SKYTOUCH!!')
    print('Learn with Entertainment')
    print("Press 1 to login")
    print("New User? Register Now. Press 2")
    print('Press 0 to EXIT')
    ch = input('>>> ')
    if ch == '1':
        login.verify()
    elif ch == '2':
        register.fun()
    elif ch == '0':
        Exit()
    else:
        print("Please enter a valid input.")
        menu()


def Exit():
    """To terminate the program"""
    print("##THANK YOU FOR VISITING OUR WEBSITE. NEVER STOP LEARNING AND HAVING ENTERTAINMENT##")
    mycon.close()
    exit()


menu()

# OTP sending program
# import smtplib
# import random
#
# # create smtp session
# s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
# # start TLS for E-mail security
# s.starttls()
# # Log in to your gmail account
# s.login("skytouch.clairie@gmail.com", "ceilotocco")
# otp = random.randint(1000, 9999)
# otp = str(otp)
# # user_mail=reg_data[5]
# s.sendmail("skytouch.clairie@gmail.com", 'ritu.kansal456@gmail.com', otp)
# print("OTP sent succesfully to registered mail id..")
# # OTP verification program
# OTP = input('Enter the OTP: ')
# if OTP == otp:
#     print('##ALL DETAILS VERIFIED##')
# else:
#     print('Invalid OTP!!!')
# # close smtp session
# s.quit()
