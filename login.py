print('hello')
print('welcome')
import mysql.connector as ms

mycon = ms.connect(host='db4free.net', user='divergent', passwd='tanya555', charset='utf8', database='dthcon')
if mycon.is_connected():
    print('connected!')
    mycursor = mycon.cursor()
    mycursor.execute('select * from login_info;')
    login_data=mycursor.fetchall()
    def verify():
        ''' to verify login information of the user.'''
        print('##LOGIN DETAILS##')
        user_name=input('USERNAME: ')
        pswd=input('PASSWORD: ')
        t=(user_name,pswd)
        if t in login_data:
            print(f'WELCOME {user_name}! ')
        else:
            print('either username or password incorrect.')
            forgot=int(input('forgot password?? press 0 to change password.Else press any key to continue. '))
            if forgot!=0:
                verify()
            else:
                def change_pswd():
                    def menu():
                        print('##PLEASE ENTER EITHER OF MOBILE NO/VC NO/EMAIL ID##')
                        print('press 1 to enter mobile no. ')
                        print('press 2 to enter vc no. ')
                        print('press 3 to enter email id. ')
                        ch=int(input('enter your choice: '))
                        if ch==1:
                            mb=int(input('MOBILE NUMBER: '))
                        elif ch==2:
                            vc=int(input('VC NUMBER: '))
                        elif ch==3:
                            id=input('EMAIL ID: ')
                        else:
                            print('Please enter valid choice')
                            menu()

