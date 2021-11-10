# #menu
# import login
# import register
# import mysql.connector as ms
# mycon = ms.connect(host='db4free.net', user='clairie', passwd='education', charset='utf8', database='skytouch')
#
# print('connected!')
# mycursor = mycon.cursor()
# mycursor.execute('select * from login_info;')
# login_data = mycursor.fetchall()
# mycursor.execute("select * from reg;")
# reg_data = mycursor.fetchall()
# print('WELCOME TO SKYTOUCH!!')
# ch=input('> ')
# if ch=='1' :
#     login.verify()
# elif ch=='2':
#     register.fun()
#
#
# print('hi')
#
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
#     user_name = input('USERNAME: ')
#     pswd = input('PASSWORD: ')
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
# print('hi')
#
#
#
#
#
#
#
# # registration file
# # import login
# import main
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
#
#         for i in main.reg_data:
#             if uname == i[2]:
#                 print("This username already exists")
#                 loop2 = "y"
#
#             else:
#                 if length == 0:
#                     print("Enter a valid username")
#                     loop2 = "y"
#                 else:
#                     user = uname
#                     loop2 = "n"
#                     return user
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
# def fun():
#     print('##REGISTRATION WINDOW##')
#     print('Dear Customer, please note our DTH service is only available in INDIA.')
#     nm = name()
#     uname = username()
#     passwd = password()
#     mb = mobile()
#     mail = input("Enter email= ")
#     print(
#         'Please provide the following details that will be required to change your password if you forget it in future.')
#     fav_place = place()
#     fav_color = color()
#     fav_pet = pet()
#     VC = vc()
#
#     query = f"insert into reg values('{VC}','{nm}','{uname}','{mb}','{passwd}','{mail}', '{fav_place}','{fav_color}','{fav_pet}')"
#     main.mycursor.execute(query)
#     main.mycon.commit()
#     print('##THANK YOU FOR REGISTERING WITH US!!##')
# print('hi')
#
#


def email():
    """to input email and verify it."""
    mail = input("enter your e-mail: ")
    if len(mail)==0:
        print('Invalid Email.')
        email()
    elif mail.isspace():
        print('Invalid Email.')
        email()
    else:
        ans= otp(mail)
        print(ans)
        if ans[0] == 'verified':
            print('inside loop')
            print(ans[1])
            return ans[1]
        else:
            print('Please input your email again.')
            email()

def otp(email):
    import smtplib
    import random
    # create smtp session
    s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
    # start TLS for E-mail security
    s.starttls()
    # Log in to your gmail account
    s.login("skytouch.clairie@gmail.com", "ceilotocco")
    OTP = random.randint(1000, 9999)
    OTP = str(OTP)
    # return otp
    try:
        s.sendmail("skytouch.clairie@gmail.com", email, OTP)
        print("OTP sent successfully to registered mail id...")
    except:
        print('Invalid Email')
        return 'invalid'
    # OTP verification program
    iOTP = input('Enter the OTP to verify your email: ')
    if iOTP == OTP:
        print('##OTP VERIFIED##')
        # close smtp session
        s.quit()
        return ('verified', email)
    else:
        print('Invalid OTP!!!')
        # close smtp session
        s.quit()
        return 'invalid'
mail=email()
print(mail)