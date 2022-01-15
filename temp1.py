# # REGISTRATION FILE
#
# import home
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
#             for i in home.reg_data:
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
#     for i in home.reg_data:
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
# # def place():
# #     """to input place"""
# #     while True:
# #         fav_place = input('Enter your favourite place: ')
# #         if len(fav_place) == 0:
# #             print('Please enter valid favourite place.')
# #         elif fav_place.isspace():
# #             print('Please enter a valid favourite place.')
# #         else:
# #             break
# #     return fav_place
#
#
# # def color():
# #     """to input color"""
# #     while True:
# #         fav_color = input('Enter your favourite color: ')
# #         if len(fav_color) == 0:
# #             print('Please enter valid favourite color.')
# #         elif fav_color.isspace():
# #             print('Please enter a valid favourite color.')
# #         else:
# #             break
# #     return fav_color
#
#
# # def pet():
# #     """to input pet"""
# #     while True:
# #         fav_pet = input('Enter your favourite pet: ')
# #         if len(fav_pet) == 0:
# #             print('Please enter valid favourite pet.')
# #         elif fav_pet.isspace():
# #             print('Please enter a valid favourite pet.')
# #         else:
# #             break
# #     return fav_p
#
#
# def fun():
#     """main function to store user data in the reg table"""
#     print('##REGISTRATION WINDOW##')
#     print('Dear Customer, please note our DTH service is only available in INDIA.')
#     nm = name()
#     uname = username()
#     passwd = password()
#     mb = mobile()
#     mail = email()
#     print(mail)
#     VC = vc()
#
#     query = f"insert into reg values('{VC}','{nm}','{uname}','{mb}','{passwd}','{mail}')"
#     home.mycursor.execute(query)
#     home.mycon.commit()
#     print('##THANK YOU FOR REGISTERING!!##')
#     ch = input('Do you want to register another user?(y/n)= ').lower()
#     if ch == 'y':
#         fun()
#     else:
#         home.menu()
#
#
# import temp
# def fun1():
#     print('in file 1: temp1')
# fun1()
# temp.fun2()


print("Now accepting: @upi, @paytm, @ibl, @axl, @ybl, @apl")
upi = input("enter you UPI Id".capitalize())
if len(upi) == 14 or len(upi) == 16:
    if upi[10] == "@":
        print("press 1 to confirm your payment.")
        print('press any key to skip payment. You can pay later on by logging into your account.')
        ans = input("enter your choice= ")

        if ans == "1":
            print(f'Your total amount is= Rs. {total_amount}')
            print(f'Press 1 to pay Rs. {total_amount}')
            print('Press any key to skip the transaction, you can pay later by logging into your account')
            Ans = input('Enter your choice here: ')
            if Ans == '1':
                pay_date = date.today().isoformat()
                query = f"update user_info set paid={total_amount} ,pay_date='{pay_date}' where username='{User}';"
                mycursor.execute(query)
                mycon.commit()
                print('Please Wait, your payment is in process...')
                print("...Do not refresh the page... ")
                print('Payment made successfully!!')
                payment_confirmation(total_amount, User)
            else:
                query = f"update user_info set paid=0;"
                mycursor.execute(query)
                mycon.commit()

                menu()
        else:
            query = f"update user_info set paid=0;"
            mycursor.execute(query)
            mycon.commit()
            menu()
    else:
        print('Please enter a valid choice!!')
        transaction(total_amount, User)
else:
    print('Please enter a valid choice!!')
    transaction(total_amount, User)
