# registration file

import mysql.connector as ms
import random

mycon = ms.connect(host="db4free.net", user="clairie", passwd="education", charset="utf8", database="skytouch")
if mycon.is_connected():
    print("connected")
    mycursor = mycon.cursor()
    mycursor.execute("select * from reg")
    data = mycursor.fetchall()


    def mobile():
        """to input mobile no. of user."""
        loop1 = "y"
        while loop1 == "y":
            mb = input("Enter your mobile number= ")
            if len(mb) == 10:
                if mb.isdigit():
                    mobile = mb
                    loop1 = "n"

                    return mobile
            else:
                print("Invalid mobile number")
                loop1 = "y"


    def username():
        """to input username of user"""
        loop2 = "y"
        while loop2 == "y":
            uname = input("Enter your username= ")
            length = len(uname)

            for i in data:
                if uname == i[2]:
                    print("This username already exists")
                    loop2 = "y"
            if length == 0:
                print("Enter a valid username")

            elif uname.isspace():
                print("please enter a valid username ")

            else:
                user = uname
                loop2 = "n"
                return user




    def password():

        loop3 = "y"
        while loop3 == "y":
            pswd = input("Enter a password= ")
            length = len(pswd)
            if length >= 8:
                if pswd.isalnum():
                    passwd = pswd
                    loop3 = "n"
                    return passwd
                elif length > 20:
                    print("Password should be less than 20 characters")
                    loop3 = "y"
                else:
                    print("Password should consist of only digits and alphabets")
                    loop3 = "y"

            else:
                print("Password should not be less than 8 characters")
                loop3 = "y"


    def vc():
        """To generate unique vc number for every new customer."""
        vt = random.randrange(100000, 100000000000)
        for i in data:
            if vt == i[0]:
                vc = random.randrange(100000, 1000000000)
                return vc
            else:
                vc = vt
                return vc


    def name():
        """To input name of the user"""
        loop = "y"
        while loop == "y":
            name = input("Enter your fullname=")
            if len(name) == 0:
                print("Please enter a valid name")
                loop = "y"
            elif name.isspace():
                print("Please enter a valid name")
                loop = "y"
            else:
                loop = "n"
                return name


    def place():
        """to input place"""
        while True:
            fav_place = input('Enter your favourite place: ')
            if len(fav_place) == 0:
                print('Please enter valid favourite place.')
            elif fav_place.isspace():
                print('Please enter a valid favourite place.')
            else:
                break
        return fav_place


    def color():
        """to input color"""
        while True:
            fav_color = input('Enter your favourite color: ')
            if len(fav_color) == 0:
                print('Please enter valid favourite color.')
            elif fav_color.isspace():
                print('Please enter a valid favourite color.')
            else:
                break
        return fav_color


    def pet():
        """to input pet"""
        while True:
            fav_pet = input('Enter your favourite pet: ')
            if len(fav_pet) == 0:
                print('Please enter valid favourite pet.')
            elif fav_pet.isspace():
                print('Please enter a valid favourite pet.')
            else:
                break
        return fav_pet


    choice = "y"
    while choice == "y":
        cc = int(input("Enter your country code= "))
        if cc == 91:
            name = name()
            mobile = mobile()
            user = username()
            fav_place = place()
            fav_color = color()
            fav_pet = pet()

            print("Password should not be less than 8 characters and more than 20 characters")
            print("Password should consist of only digits and alphabets")
            print("No special characters allowed")
            passwd = password()

            vc = vc()
            mail = input("Enter email= ")

            query = f"insert into reg values('{vc}','{name}','{user}','{mobile}','{passwd}','{mail}', '{fav_place}','{fav_color}','{fav_pet}')"
            mycursor.execute(query)
            mycon.commit()

            choice = input("Do you want to register another user(y/n): ").lower()


        else:
            print("DTH service available only in india")
