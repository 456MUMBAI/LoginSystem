import main


def change_pswd():
    VC = input('Enter your VC number= ')
    for i in main.reg_data:
        if VC in i[0]:
            user_info = i
            print('##CHANGE PASSWORD WINDOW##')
            place = input('Enter your favourite place: ')
            color = input('Enter your favourite color: ')
            pet = input('Enter your favourite pet: ')
            if place == user_info[6] and color == user_info[7] and pet == user_info[8]:
                print('##All Details Verfied!##')
                import register
                new_pswd = register.password()
                query1 = f"update login_info set password='{new_pswd}' where username='{user_info[2]}'"
                main.mycursor.execute(query1)
                query2 = f"update reg set passwd='{new_pswd}' where VC='{user_info[0]}'"
                main.mycursor.execute(query2)
                print('##Updated Password Successfully##')
            break
    else:
        print('No such VC number exists. ')
        ch = int(input('Press 1 to re-enter VC number. Else press any key to continue:  '))
        if ch == 1:
            change_pswd()
        else:
            verify()


def verify():
    ''' to verify login information of the user.'''
    print('##LOGIN DETAILS##')
    user_name = input('USERNAME: ')
    pswd = input('PASSWORD: ')
    t = (user_name, pswd)
    if t in main.login_data:
        print(f'WELCOME {user_name}! ')
    else:
        print('Either username or password incorrect.')
        forgot = input('Forgot password? Press 0 to change password. Else press any key to continue. ')
        if forgot == '0':
            change_pswd()
        else:

            print('either username or password incorrect.')
            forgot = int(input('Forgot password? Press 0 to change password. Else press any key to continue. '))
            if forgot != 0:
                verify()
            else:
                change_pswd()

print('hi there')
verify()

            verify()
print('hi')