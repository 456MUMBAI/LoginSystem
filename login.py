# # LOGIN FILE
# import main
# # import reg
# def menu(username):
#     print(f'WELCOME {username}! ')
#     exit()
#
#
# def verify():
#     """ To verify login details of the user."""
#     print('##LOGIN DETAILS##')
#     while True:
#         user_name = input('USERNAME: ')
#         if len(user_name) == 0:
#             print("please enter a valid  username")
#         elif user_name.isspace():
#             print("please enter a valid  username")
#         else:
#             pswd = input('PASSWORD: ')
#             break
#
#     t = (user_name, pswd)
#     if t in main.login_data:
#         menu(user_name)
#     else:
#         print('Either username or password incorrect.')
#         forgot = input('Forgot password? Press 0 to change password. Else press any key to continue. ')
#         if forgot == '0':
#             change_pswd()
#         else:
#             main.menu()
#
#
# def change_pswd():
#     import reg
#     """To change password"""
#     VC = input('Enter your VC number= ')
#     try:
#         if 100000<=int(VC)<=100000000000:
#             for i in main.reg_data:
#                 if VC in i[0]:
#                     user_info = i
#                     print('##CHANGE PASSWORD WINDOW##')
#                     print('hhh')
#                     print('jjj')
#                     ans = reg.otp(user_info[5])
#                     print(ans)
#                     if ans[0] == 'verified':
#
#                         new_pswd = reg.password()
#                         query1 = f"update login_info set password='{new_pswd}' where username='{user_info[2]}'"
#                         main.mycursor.execute(query1)
#                         query2 = f"update reg set passwd='{new_pswd}' where VC='{user_info[0]}'"
#                         main.mycursor.execute(query2)
#                         print('##Updated Password Successfully##')
#                         menu(user_info[2])
#                     else:
#                         print('Invalid OTP!')
#                         break
#             else:
#                 print('No such VC number exists. ')
#                 ch = int(input('Press 1 to re-enter VC number. Else press any key to continue:  '))
#                 if ch == 1:
#                     change_pswd()
#                 else:
#                     main.menu()
#     except ValueError:
#         print('Please enter a Valid VC number.')
#         change_pswd()
#     else:
#         print('Please enter a Valid VC number')
#         change_pswd()
#     main.menu()
#
#
# # k=reg.otp('ritu.kansal456@gmail.com')
