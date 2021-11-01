# registration file

import main
#import login


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

        for i in main.reg_data:
            if uname == i[2]:
                print("This username already exists")
                loop2 = "y"

            else:
                if length == 0:
                    print("Enter a valid username")
                    loop2 = "y"
                else:
                    user = uname
                    loop2 = "n"
                    return user


def password():
    """to change / add password"""
    print("Password should not be less than 8 characters and more than 20 characters")
    print("Password should consist of only digits and alphabets")
    print("No special characters allowed")
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
    import random
    vt = random.randrange(100000, 100000000000)
    for i in main.login_data:
        if vt == i[0]:
            vt = random.randrange(100000, 1000000000)
    else:
        return vt


def name():
    """To input name of the user"""
    loop = "y"
    while loop == "y":
        name = input("Enter your fullname= ")
        if len(name) == 0:
            print("Please enter a valid name.")
            loop = "y"
        elif name == " ":
            print("Please enter a valid name.")
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

# def mail():
#      while True:
#          print("please note that for the registration process you are required to enter your G-mail")
#          import os
#          import math
#          import random
#          import smtplib
#
#          digits = "0123456789"
#          OTP = ""
#          for i in range(6):
#              OTP += digits[math.floor(random.random() * 10)]
#          otp = OTP + " is your OTP"
#          msg = otp
#          s = smtplib.SMTP('smtp.gmail.com', 587)
#          s.starttls()
#          s.login("Your Gmail Account", "You app password")
#          mail = input("Enter your email: ")
#          s.sendmail('&&&&&&&&&&&', mail, msg)
#          a = input("Enter Your OTP >>: ")
#          if a == OTP:
#              print("Verified")
#              return mail
#              break
#          else:
#              print("Please Check your OTP again")


def fun():
    print('##REGISTRATION WINDOW##')
    print('Dear Customer, please note our DTH service is only available in INDIA.')
    nm = name()
    uname = username()
    passwd = password()
    mb = mobile()
    mail=input("enter your e-maiL")
    #mail=mail()

    print(
        'Please provide the following details that will be required to change your password if you forget it in future.')
    fav_place = place()
    fav_color = color()
    fav_pet = pet()
    VC = vc()

    query = f"insert into reg values('{VC}','{nm}','{uname}','{mb}','{passwd}','{mail}', '{fav_place}','{fav_color}','{fav_pet}')"
    main.mycursor.execute(query)
    main.mycon.commit()
    print('##THANK YOU FOR REGISTERING WITH US!!##')

