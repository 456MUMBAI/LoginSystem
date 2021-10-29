
#registration file
import mysql.connector as ms

mycon = ms.connect(host='db4free.net', user='clairie', passwd='education', charset='utf8', database='skytouch')
if mycon.is_connected():
    print('connected!')

import mysql.connector as ms
import random
mycon=ms.connect(host="db4free.net",user="clairie",passwd="education",charset="utf8",database="skytouch")
if mycon.is_connected():
    print("connected")
    mycursor=mycon.cursor()
    mycursor.execute("select * from reg")
    data=mycursor.fetchall()
    def mobile():
        #global mobile
        loop1 = "y"
        while loop1 == "y":
            mb = input("enter your mobile number=")
            if len(mb) == 10:
                if mb.isdigit():
                    mobile = mb
                    loop1 = "n"

                    return mobile
            else:
                print("invalid number")
                loop1 = "y"
    def username():
        #global user
        loop2 = "y"
        while loop2 == "y":
            uname = input("enter your username=")
            length=len(uname)

            for i in data:
                if uname == i[2]:
                    print("this username already exist")
                    loop2 = "y"

                else:
                    if length == 0:
                        print("enter a valid username")
                        loop2 = "y"
                    else:
                        user = uname
                        loop2 = "n"
                        return user






    def password():
        #global passwd
        loop3 = "y"
        while loop3 == "y":
            pswd = input("enter a password=")
            length = len(pswd)
            if length >= 8:
                if pswd.isalnum():
                    passwd = pswd
                    loop3 = "n"
                    return passwd
                elif length>20:
                    print("enter a password less than 20 characters")
                    loop3="y"
                else:
                    print("password should consist of only digits and alphabets")
                    loop3 = "y"

            else:
                print("password should not be less than 8 characters")
                loop3 = "y"
    def vc():
        #global vc
        vt = random.randrange(100000, 100000000000)
        for i in data:
            if vt == i[0]:
                vc = random.randrange(100000, 1000000000)
                return vc
            else:
                vc = vt
                return vc
    def name():
        loop = "y"
        while loop == "y":
            name = input("enter your fullname=")
            if len(name) == 0:
                print("please enter a valid name")
                loop = "y"
            elif name == " ":
                print("please enter a valid name")
                loop = "y"
            else:
                loop = "n"
                return name




    choice = "y"
    while choice=="y":
         cc=int(input("enter your country code"))
         if cc==91:
             name=name()

             mobile=mobile()
             user=username()


             print("password should not be less than 8 characters and more than 20 characters")
             print("password should consist of only digits and alphabets")
             print("no special characters allowed")
             passwd=password()
             vc=vc()


             mail=input("enter email=")


             query="insert into reg values('{0}','{1}','{2}','{3}','{4}','{5}')".format(vc,name,user,mobile,passwd,mail)
             mycursor.execute(query)
             mycon.commit()

             print("do you want to add another user(y/n)")
             choice=input("enter=")


         else:
             print("DTH service available only in india")
