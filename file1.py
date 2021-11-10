# # # import os
# # import math
# # import random
# # import smtplib
# #
# # digits = "0123456789"
# # OTP = ""
# # for i in range(6):
# #     OTP += digits[math.floor(random.random() * 10)]
# # otp = OTP + " is your OTP"
# # msg = otp
# # s = smtplib.SMTP('smtp.gmail.com', 587)
# # s.starttls()
# # s.login("hanumimassey222@gmail.com", "lauramassey")
# # emailid = input("Enter your email: ")
# # s.sendmail('hanumimassey222@gmail.com', emailid, msg)
# # a = input("Enter Your OTP >>: ")
# # if a == OTP:
# #     print("Verified")
# #     s.quit()
# # else:
# #     print("Please Check your OTP again")
# #     s.quit()
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
#
#
#
#
#
# # registration file
#
# import main
# #import login
#
#
# def mobile():
#     """to input mobile no. of user."""
#     loop1 = "y"
#     while loop1 == "y":
#         mb = input("Enter your mobile number= ")
#         if len(mb) == 10:
#             if mb.isdigit():
#                 mobile = mb
#                 loop1 = "n"
#
#                 return mobile
#         else:
#             print("Invalid mobile number")
#             loop1 = "y"
#
#
# def username():
#     """to input username of user"""
#     loop2 = "y"
#     while loop2 == "y":
#         uname = input("Enter your username= ")
#         length = len(uname)
#         if length == 0:
#             print("Enter a valid username")
#             loop2 = "y"
#
#         else:
#             for i in main.reg_data:
#                 if uname == i[2]:
#                     print("This username already exists")
#                     loop2 = "y"
#                     break
#             else:
#                 user = uname
#                 loop2 = "n"
#                 return user
#
#
#
#
#
#
# def password():
#     """to change / add password"""
#     print("Password should not be less than 8 characters and more than 20 characters")
#     print("Password should consist of only digits and alphabets")
#     print("No special characters allowed")
#     loop3 = "y"
#     while loop3 == "y":
#         pswd = input("Enter a password= ")
#         length = len(pswd)
#         if length >= 8:
#             if pswd.isalnum():
#                 passwd = pswd
#                 loop3 = "n"
#                 return passwd
#             elif length > 20:
#                 print("Password should be less than 20 characters")
#                 loop3 = "y"
#             else:
#                 print("Password should consist of only digits and alphabets")
#                 loop3 = "y"
#
#         else:
#             print("Password should not be less than 8 characters")
#             loop3 = "y"
#
#
# def vc():
#     """To generate unique vc number for every new customer."""
#     import random
#     vt = random.randrange(100000, 100000000000)
#     for i in main.login_data:
#         if vt == i[0]:
#             vt = random.randrange(100000, 1000000000)
#     else:
#         return vt
#
#
# def name():
#     """To input name of the user"""
#     loop = "y"
#     while loop == "y":
#         name = input("Enter your fullname= ")
#         if len(name) == 0:
#             print("Please enter a valid name.")
#             loop = "y"
#         elif name == " ":
#             print("Please enter a valid name.")
#             loop = "y"
#         else:
#             loop = "n"
#             return name
#
#
# def place():
#     """to input place"""
#     while True:
#         fav_place = input('Enter your favourite place: ')
#         if len(fav_place) == 0:
#             print('Please enter valid favourite place.')
#         elif fav_place.isspace():
#             print('Please enter a valid favourite place.')
#         else:
#             break
#     return fav_place
#
#
# def color():
#     """to input color"""
#     while True:
#         fav_color = input('Enter your favourite color: ')
#         if len(fav_color) == 0:
#             print('Please enter valid favourite color.')
#         elif fav_color.isspace():
#             print('Please enter a valid favourite color.')
#         else:
#             break
#     return fav_color
#
#
# def pet():
#     """to input pet"""
#     while True:
#         fav_pet = input('Enter your favourite pet: ')
#         if len(fav_pet) == 0:
#             print('Please enter valid favourite pet.')
#         elif fav_pet.isspace():
#             print('Please enter a valid favourite pet.')
#         else:
#             break
#     return fav_pet
#
#
#
# def fun():
#     print('##REGISTRATION WINDOW##')
#     print('Dear Customer, please note our DTH service is only available in INDIA.')
#     nm = name()
#     uname = username()
#     passwd = password()
#     mb = mobile()
#     mail=input("enter your e-mail: ")
#
#
#     print('Please provide the following details that will be required to change your password if you forget it in future.')
#     fav_place = place()
#     fav_color = color()
#     fav_pet = pet()
#     VC = vc()
#
#     query = f"insert into reg values('{VC}','{nm}','{uname}','{mb}','{passwd}','{mail}', '{fav_place}','{fav_color}','{fav_pet}')"
#     main.mycursor.execute(query)
#     main.mycon.commit()
#     print('##THANK YOU FOR REGISTERING WITH US!!##')
#     ch=input('Do you want to register another user?(y/n)= ').lower()
#     if ch=='y':
#         fun()
#     else:
#         pass
# # print('hiii')
#
#
#
#
#
# #menu
# import login
# import rconnector as ms
# mycon = ms.connect(host='db4free.net', user='clairie', passwd='education', charset='utf8', database='skytouch')
#
# print('connected!')
# mycursor = mycon.cursor()
# mycursor.execute('select * from login_info;')
# login_data = mycursor.fetchall()
# mycursor.execute("select * from reg;")
# reg_data = mycursor.fetchall()
# print('WELCOME TO SKYTOUCH!!')
# print('See the Unseen!!')
# print("Press 1 to login")
# print("New User? Register Now. Press 2")
# ch=input('>>> ')
#
# if ch=='1':
#     login.verify()
# elif ch=='2':
#     register.fun()
#
#
#
#
#
# # import smtplib
# # import random
# #
# # # create smtp session
# # s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
# # # start TLS for E-mail security
# # s.starttls()
# # # Log in to your gmail account
# # s.login("hanumimassey222@gmail.com", "lauramassey")
# # otp = random.randint(1000, 9999)
# # otp = str(otp)
# #
# # s.sendmail("hanumimassey222@gmail.com", 'ritu.kansal456@gmail.com', otp)
# # print("OTP sent succesfully..")
# # # close smtp session
# # s.quit()
# print('hi')
#
#
#
#
# import main
#
#
# def change_pswd():
#     VC = input('Enter your VC number= ')
#     for i in main.reg_data:
#         if VC in i[0]:
#             user_info = i
#             print('##CHANGE PASSWORD WINDOW##')
#             place = input('Enter your favourite place: ')
#             color = input('Enter your favourite color: ')
#             pet = input('Enter your favourite pet: ')
#             if place == user_info[6] and color == user_info[7] and pet == user_info[8]:
#                 print('##All Details Verfied!##')
#                 import register
#                 new_pswd = register.password()
#                 query1 = f"update login_info set password='{new_pswd}' where username='{user_info[2]}'"
#                 main.mycursor.execute(query1)
#                 query2 = f"update reg set passwd='{new_pswd}' where VC='{user_info[0]}'"
#                 main.mycursor.execute(query2)
#                 print('##Updated Password Successfully##')
#             break
#     else:
#         print('No such VC number exists. ')
#         ch = int(input('Press 1 to re-enter VC number. Else press any key to continue:  '))
#         if ch == 1:
#             change_pswd()
#         else:
#             verify()
#
#
# def verify():
#     ''' to verify login information of the user.'''
#     print('##LOGIN DETAILS##')
#     while True:
#         user_name = input('USERNAME: ')
#         if len(user_name)==0:
#             print("please enter a valid  username")
#         else:
#             pswd = input('PASSWORD: ')
#             break
#
#
#     t = (user_name, pswd)
#     if t in main.login_data:
#         print(f'WELCOME {user_name}! ')
#     else:
#         print('Either username or password incorrect.')
#         forgot = input('Forgot password? Press 0 to change password. Else press any key to continue. ')
#         if forgot == '0':
#             change_pswd()
#         else:
#             verify()
# #print('hhhii')

# #CSV file                   9
#program to insert  recprds in a file
import csv
ch="y"
f=open("comma.csv","a",newline="")
data=["name","rollnumber","marks"]
a=csv.writer(f)
a.writerow(data)
while ch=="y" or ch=="Y":
    name=input("please enter your name")
    roll=int(input("enter you roll number"))
    marks=int(input("enter your marks in maths"))
    rec=[name,roll,marks]
    a.writerow(rec)
    ch=input("would you like to enter another record")
f.close()

