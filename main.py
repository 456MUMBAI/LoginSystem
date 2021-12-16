# MAIN FILE
from prettytable import PrettyTable
# import reg
# import mysql.connector as ms
# import login
from colorama import Fore, Back, Style

# mycon = ms.connect(host='db4free.net', user='clairie', passwd='education', charset='utf8', database='skytouch')

# print('connected!')
# mycursor = mycon.cursor()
# mycursor.execute('select * from login_info;')
# login_data = mycursor.fetchall()
# print(login_data)
# mycursor.execute("select * from reg;")
# reg_data = mycursor.fetchall()
# print(reg_data)


def menu():
    """Home Page"""
    print('WELCOME TO SKYTOUCH!!')
    print('Learn with Entertainment')
    print("Press 1 to login")
    print("New User? Register Now. Press 2")
    print('Press 0 to EXIT')
    ch = input('>>> ')
    if ch == '1':
        login.verify()
    elif ch == '2':
        reg.fun()
    elif ch == '0':
        Exit()
    else:
        print("Please enter a valid input.")
        menu()


def Exit():
    """To terminate the program"""
    print("##THANK YOU FOR VISITING OUR WEBSITE. NEVER STOP LEARNING AND HAVING ENTERTAINMENT##")
    mycon.close()
    exit()

#menu()









#home()
def vision():
    print(Style.BRIGHT + Fore.RED + "VISSION AND MISSION".center(90), Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.LIGHTYELLOW_EX + "Everything is rapidly changing so to keep pace with these changes, one has to make modifications in how things work, so they can be taken to the advanced level. ",
        Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.LIGHTYELLOW_EX + "With this mindset we have built our DTH which is not only  user-friendly  but affordable.",
        Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.LIGHTYELLOW_EX + "We are keen on providing the best service to our customers. With SKYTOUCH cable connection one can ensure their security.",
        Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.LIGHTYELLOW_EX + "Entertainment in one's life is something that can't be ignored, but due to high cost of tv packages and a busy schedule of people, many people are drained out of this joy.",
        Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.LIGHTYELLOW_EX + "Therefore, our DTH service has come up with low cost packages and 24/7 services",
        Style.RESET_ALL)

def core_values():
    print(Style.BRIGHT + Fore.GREEN + "OUR CORE VALUES".center(90), Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.LIGHTYELLOW_EX + "To work together effectively and efficiently realizing organisational objectives with a sense of shared accomplishment.",
        Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.LIGHTYELLOW_EX + "To act rapidly and deliver on responsibilities while anticipating and responding to the dynamic environment.",
        Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.LIGHTYELLOW_EX + "To embrace each individual’s unique talents, diverse life choices and work styles. To be fair, humble, honest, transparent and ethical in conduct.",
        Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.LIGHTYELLOW_EX + "To generate, encourage and implement unconventional & novel ideas/technology continuously which fuel business growth.",
        Style.RESET_ALL)
    print(Style.NORMAL + Fore.LIGHTYELLOW_EX + "Some core values that makes us different",Style.RESET_ALL)

def techandinfs():
    print(Style.BRIGHT + Fore.CYAN + "Technology and Infrastructure".center(90), Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.LIGHTYELLOW_EX + " SKYTOUCH serves its customers with a passion, always endeavours to offer its customers with exceptional picture quality, stereophonic sound along with unmatched services.",
        Style.RESET_ALL)
    print(Style.NORMAL + Fore.LIGHTYELLOW_EX + "Believing in the quote",
          Style.BRIGHT + Fore.LIGHTRED_EX + "Best choices come with best rewards",
          Style.NORMAL + Fore.LIGHTYELLOW_EX + " the brand offers the finest to its customers with its best-in-class technology and infrastructure",
          Style.RESET_ALL)
    print(Style.NORMAL + Fore.LIGHTCYAN_EX + "Digital Picture Quality and Stereophonic Sound".center(50),
          Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.LIGHTBLACK_EX + "Delivering maximum entertainment right in their homes, SKYTOUCH offers its customers with unmatched picture quality and superb sound experience.",
        Style.RESET_ALL)
    print(Style.NORMAL + Fore.LIGHTCYAN_EX + "Geographic Mobility".center(30), Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.LIGHTBLACK_EX + "The full-fledged all India coverage of SKYTOUCH ensures that entertainment is reached in every nook and corner of the country along with uninterrupted services and nonstop access to all channels.",
        Style.RESET_ALL)
    print(Style.NORMAL + Fore.LIGHTCYAN_EX + "Flexible Recharge Option".center(30), Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.LIGHTBLACK_EX + "SKYTOUCH offers you a range of recharge offers that are designed to provide maximum value for money where you can select and pay for channels of your choice",
        Style.RESET_ALL)


def whyus():
    print(Style.BRIGHT + Fore.RED + "WHY US?".center(90), Style.RESET_ALL)
    print(Style.NORMAL + Fore.LIGHTGREEN_EX + "Largest DTH service provider. Trusted by over 21 million subscribers ",
          Style.RESET_ALL)
    print(Style.NORMAL + Fore.LIGHTGREEN_EX + "At your service 24*7. Call ,e-mail or chat with us", Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.LIGHTGREEN_EX + "Non stop entertainement with easy recharge options. Availability of wallets , dealers etc.",
        Style.RESET_ALL)
    print(Style.NORMAL+Fore.LIGHTGREEN_EX+"We provide our cutomers with refund if they do not like your service",Style.RESET_ALL)
    print(Style.NORMAL+Fore.LIGHTGREEN_EX+"Our customers can cancel their plan anytime and modify it without any troubles",Style.RESET_ALL)


def home():
    print(Style.BRIGHT+Fore.RED+"ABOUT US".center(85),Style.RESET_ALL)
    print("To know more about our vission and mission. Press 1")
    print("To know more about our core values. Press 2")
    print("To know more about our technology and infrastructure. Press 3")
    print("To know why you should select us as your DTH service provider. Press 4")
    ch=int(input("please enter your choice="))
    if ch==1:
        vision()
    if ch==2:
        core_values()
    if ch==3:
        techandinfs()
    if ch==4:
        whyus()
    else:
        print("please enter a valid choice")
    print("Do you want to know more about us.If yes press 0 else press any key to skip")
    i=input("please enter")
    if i=="0":
        home()
    else:
        print("THANK YOU FOR SHOWING INTEREST TO KNOW MORE ABOUT US")
        print("HAVE A NICE DAY")
home()


# OTP sending program
# import smtplib
# import random
#
# # create smtp session
# s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
# # start TLS for E-mail security
# s.starttls()
# # Log in to your gmail account
# s.login("skytouch.clairie@gmail.com", "ceilotocco")
# otp = random.randint(1000, 9999)
# otp = str(otp)
# # user_mail=reg_data[5]
# s.sendmail("skytouch.clairie@gmail.com", 'ritu.kansal456@gmail.com', otp)
# print("OTP sent succesfully to registered mail id..")
# # OTP verification program
# OTP = input('Enter the OTP: ')
# if OTP == otp:
#     print('##ALL DETAILS VERIFIED##')
# else:
#     print('Invalid OTP!!!')
# # close smtp session
# s.quit()
