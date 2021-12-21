# # REGISTRATION FILE
#
# import main
# import userinfo
#
#
# def fun():
#     """main function to store user data in the reg table"""
#     print('##REGISTRATION WINDOW##')
#     print('Dear Customer, please note our DTH service is only available in INDIA.')
#     query = f"insert into reg values('{details.VC}','{details.nm}','{details.uname}','{details.mb}','{details.passwd}','{details.mail}')"
#     main.mycursor.execute(query)
#     main.mycon.commit()
#     userinfo.select()
#     return details.uname
#
#
# def otp(email):
#     """otp generation and verification program"""
#     import smtplib
#     import random
#     # create smtp session
#     s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
#     # start TLS for E-mail security
#     s.starttls()
#     # Log in to your gmail account
#     s.login("skytouch.clairie@gmail.com", "ceilotocco")
#     OTP = random.randint(1000, 9999)
#     msg = '''Dear User,
#
#     Thank you for registering at SKYTOUCH. We have received your request for registration.
#     Your OTP for validation is= ''' + str(OTP)
#
#     try:
#         s.sendmail("skytouch.clairie@gmail.com", email, msg)
#         print("OTP sent successfully to registered mail id...")
#     except:
#         print('Invalid Email')
#         return 'invalid'
#
#     # OTP verification program
#     iOTP = int(input('Enter the OTP to verify your email: '))
#     if iOTP == OTP:
#         print('##OTP VERIFIED##')
#         # close smtp session
#         s.quit()
#         return 'verified', email
#     else:
#         print('Invalid OTP!!!')
#         # close smtp session
#         s.quit()
#         return 'invalid'
#
#
# def mobile():
#     """To input mobile no. of user."""
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
#     """To input username of user"""
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
# def password():
#     """To change / add password"""
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
#     for i in main.reg_data:
#         if str(vt) == i[0]:
#             vt = random.randrange(100000, 1000000000)
#     else:
#         return str(vt)
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
#             return name
#
#
# def email():
#     """to input email and verify it."""
#     mail = input("enter your e-mail: ")
#     if len(mail) == 0:
#         print('Invalid Email.')
#         email()
#     elif mail.isspace():
#         print('Invalid Email.')
#         email()
#     else:
#         ans = otp(mail)
#         if ans[0] == 'verified':
#
#             return ans[1]
#         else:
#             print('Please input your email again.')
#             email()
#
#
# class details:
#     nm = name()
#     n = nm
#     uname = username()
#     u = uname
#     passwd = password()
#     p = passwd
#     mb = mobile()
#     m = mb
#     mail = email()
#     ml = mail
#     VC = vc()
#     v = VC
