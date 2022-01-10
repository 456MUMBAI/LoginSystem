import mysql.connector as ms
from prettytable import PrettyTable
from datetime import date, timedelta, datetime
from colorama import Fore, Style, Back

# DATA
mycon = ms.connect(host='db4free.net', user='clairie', passwd='education', charset='utf8', database='skytouch')
print('connected!')
mycursor = mycon.cursor()
mycursor.execute("select * from reg;")
reg_data1 = mycursor.fetchall()

# print(login_data)




def menu():
    print('WELCOME TO SKYTOUCH!!')
    print('Learn with Entertainment')
    print("Press 1 to login")
    print("New User? Register Now. Press 2")
    print('Press 3 to explore our website!')
    print('Press 4 to view our SKYTOUCH Channel Guide')
    print('Press 5 to contact us ')
    print('Press 0 to EXIT')
    ch = input('>>> ')
    if ch == '1':
        verify()
    elif ch == '2':
        fun()
    elif ch == '0':
        Exit()
    elif ch == '3':
        home()
    elif ch == '4':
        guide()
    elif ch=="5":
        contact()

    else:
        print("Please enter a valid input.")
        menu()


def Exit():
    """To terminate the program"""
    print("##THANK YOU FOR VISITING OUR WEBSITE. NEVER STOP LEARNING AND HAVING FUN##")
    mycon.close()
    exit()


# ABOUT US
def home():
    """Home Page"""
    print(Style.BRIGHT + Fore.RED + "ABOUT US".center(85), Style.RESET_ALL)
    print("To know more about our vission and mission. Press 1")
    print("To know more about our core values. Press 2")
    print("To know more about our technology and infrastructure. Press 3")
    print("To know why you should select us as your DTH service provider. Press 4")
    ch = int(input("Enter your choice here= "))
    if ch == 1:
        vision()
    if ch == 2:
        core_values()
    if ch == 3:
        techandinfs()
    if ch == 4:
        whyus()

    else:
        print("Please enter a valid choice!!")
    print("To know more about us press 0, else press any key to skip.")
    i = input("Enter your choice here= ")
    if i == "0":
        home()
    else:
        print("THANK YOU FOR SHOWING INTEREST TO KNOW MORE ABOUT US")
        print("HAVE A NICE DAY")


def vision():
    print(Style.BRIGHT + Fore.RED + "VISION AND MISSION".center(90), Style.RESET_ALL)
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
    print(Style.NORMAL + Fore.LIGHTYELLOW_EX + "Some core values that makes us different", Style.RESET_ALL)


def techandinfs():
    print(Style.BRIGHT + Fore.CYAN + "Technology and Infrastructure".center(90), Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.LIGHTYELLOW_EX + " SKYTOUCH serves its customers with a passion, always endeavours to offer its customers with exceptional picture quality, stereophonic sound along with unmatched services.",
        Style.RESET_ALL)
    print(Style.NORMAL + Fore.LIGHTYELLOW_EX + "Believing in the quote",
          Style.BRIGHT + Fore.LIGHTRED_EX + "Best choices come with best rewards",
          Style.NORMAL + Fore.LIGHTYELLOW_EX + " the brand offers the finest to its customers with its best-in-class technology and infrastructure",
          Style.RESET_ALL)
    print(Style.NORMAL + Fore.LIGHTCYAN_EX + "* Digital Picture Quality and Stereophonic Sound" +
          Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.MAGENTA + "Delivering maximum entertainment right in their homes, SKYTOUCH offers its customers with unmatched picture quality and superb sound experience." +
        Style.RESET_ALL)
    print(Style.NORMAL + Fore.LIGHTCYAN_EX + "* Geographic Mobility" + Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.MAGENTA + "The full-fledged all India coverage of SKYTOUCH ensures that entertainment is reached in every nook and corner of the country along with uninterrupted services and nonstop access to all channels." +
        Style.RESET_ALL)
    print(Style.NORMAL + Fore.LIGHTCYAN_EX + "* Flexible Recharge Option" + Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.MAGENTA + "SKYTOUCH offers you a range of recharge offers that are designed to provide maximum value for money where you can select and pay for channels of your choice",
        Style.RESET_ALL)


def whyus():
    print(Style.BRIGHT + Fore.RED + "WHY US?".center(90), Style.RESET_ALL)
    print(Style.NORMAL + Fore.LIGHTGREEN_EX + "Largest DTH service provider. Trusted by over 21 million subscribers ",
          Style.RESET_ALL)
    print(Style.NORMAL + Fore.LIGHTGREEN_EX + "At your service 24*7. Call ,e-mail or chat with us", Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.LIGHTGREEN_EX + "Non stop entertainement with easy recharge options. Availability of wallets , dealers etc.",
        Style.RESET_ALL)
    print(Style.NORMAL + Fore.LIGHTGREEN_EX + "We provide our cutomers with refund if they do not like your service",
          Style.RESET_ALL)
    print(
        Style.NORMAL + Fore.LIGHTGREEN_EX + "Our customers can cancel their plan anytime and modify it without any troubles",
        Style.RESET_ALL)


# LOGIN FILE

def welcome(username):
    mycursor.execute(f"select price,paid,pay_date,pack from user_info where username = '{username}';")
    recharge_Data=mycursor.fetchall()[0] #price,paid
    balance = recharge_Data[1]
    price = recharge_Data[0]
    tenure=int((balance/price)*30)
    pack=recharge_Data[3]

    try:
        pay_date= recharge_Data[2]
        next_recharge_date = (pay_date + timedelta(days=tenure)).isoformat()
    except:
        pay_date='0000-00-00'
        next_recharge_date='0000-00-00'
    print(f'WELCOME {username}! ')
    print()
    while True:
        print("PRESS 0 TO MODIFY YOUR PACKAGE")
        print('PRESS 1 TO RECHARGE YOUR ACCOUNT')
        print('PRESS 2 TO VIEW YOUR PROFILE')
        print('PRESS 3 TO LOG OUT')
        ans = input("enter your choice here= ")
        if ans == "0":
            modify(username)
        elif ans=='1':
            print(f'Your account  balance is = Rs. {balance} ')
            if balance!=0:
                print('Your account is already recharged. Thank You!')
                welcome(username)
            else:
                time_period(price,username)
        elif ans=='2':
            ' View Profile'
            query = f"select vc,mail, mobile from reg where username='{username}';"
            mycursor.execute(query)
            vc, mail, mobile_no = mycursor.fetchall()[0]
            mycon.commit()
            print(Fore.BLACK+Style.BRIGHT+'ACCOUNT DETAILS'.center(60)+Style.RESET_ALL)
            print(f'VC number= {vc} ')
            print(f'Registered mobile number= {mobile_no}')
            print(f'Registered mail id={mail}')
            print(f'Your current pack is= {pack}')
            print(f'Total Recharge Amount= Rs. {price} per month')
            print(f'Amount paid= Rs. {balance}')
            print(f'Last Payment= Rs.{balance} on {pay_date}')
            print(f'Next recharge date= {next_recharge_date}')
            print()

        elif ans=='3':
            print('Logging Out...')
            print()
            break

        else:
            print('Please enter a valid choice!')
            welcome(username)
    menu()


def verify():
    """ To verify login details of the user."""
    print()
    print(Style.BRIGHT+ '##LOGIN DETAILS##'.center(60)+Style.RESET_ALL)
    print()
    mycursor.execute('select * from login_info;')
    login_data = mycursor.fetchall()
    while True:
        user_name = input('USERNAME: ')
        if len(user_name) == 0:
            print("please enter a valid  username")
        elif user_name.isspace():
            print("please enter a valid  username")
        else:
            pswd = input('PASSWORD: ')
            break

    t = (user_name, pswd)
    if t in login_data:
        welcome(user_name)
    else:
        print('Either username or password is incorrect...')
        forgot = input('Forgot password? Press 0 to change password. Else press any key to continue. ')
        if forgot == '0':
            change_pswd()
        else:
            menu()


def change_pswd():
    """To change password"""

    VC = input('Enter your VC number= ')
    mycursor.execute("select * from reg;")
    reg_data = mycursor.fetchall()
    try:
        if 100000 <= int(VC) <= 100000000000:
            for i in reg_data:
                if VC in i[0]:
                    user_info = i
                    print(Style.BRIGHT+'## CHANGE PASSWORD WINDOW ##'+Style.RESET_ALL)
                    msg='Dear User,' \
                        'We have received your request to change your SKYTOUCH account password.'
                    ans = otp(user_info[5],msg)
                    if ans[0] == 'verified':
                        new_pswd = password()
                        query1 = f"update login_info set password='{new_pswd}' where username='{user_info[2]}'"
                        mycursor.execute(query1)
                        query2 = f"update reg set passwd='{new_pswd}' where VC='{user_info[0]}'"
                        mycursor.execute(query2)
                        mycon.commit()
                        print('Updated Password Successfully!!!'.upper())
                        welcome(user_info[2])
                    else:
                        print('Invalid OTP!')
                        break

            else:
                print('No such VC number exists. ')
                ch = int(input('Press 1 to re-enter VC number. Else press any key to continue:  '))
                if ch == 1:
                    change_pswd()
                else:
                    menu()
    except ValueError:
        print('Please enter a Valid VC number.')
        change_pswd()
    else:
        print('Please enter a Valid VC number')
        change_pswd()
    # menu()


# REGISTRATION FILE

def fun():
    """main function to store user data in the reg table"""
    print(Style.BRIGHT+'## REGISTRATION WINDOW ##'.center(60)+Style.RESET_ALL)
    print('Dear Customer, please note our DTH service is only available in INDIA.')
    nm = name()
    uname = username()
    passwd = password()
    mb = mobile()
    mail = email()
    print(mail)
    VC = vc()

    query = f"insert into reg values('{VC}','{nm}','{uname}','{mb}','{passwd}','{mail}')"
    query1 = f"insert into login_info values('{uname}','{passwd}')"
    mycursor.execute(query)
    mycursor.execute(query1)
    mycon.commit()

    print(Style.BRIGHT+'THANK YOU FOR REGISTERING!!'+Style.RESET_ALL)
    print()
    print('Please select your SKYTOUCH pack...')
    display(uname)
    menu()
    # ch = input('Do you want to register another user?(y/n)= ').lower()
    # if ch == 'y':
    #     fun()
    # else:
    #     menu()




def otp(email,msg):
    """otp generation and verification program"""
    import smtplib
    import random
    from email.message import EmailMessage
    MSG = EmailMessage()
    # create smtp session
    s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
    # start TLS for E-mail security
    s.starttls()
    # Log in to your gmail account
    s.login("skytouch.clairie@gmail.com", "ceilotocco22")
    OTP = random.randint(1000, 9999)
    # a=str(OTP)
    msg1 = msg+' Your OTP for validation is= ' + str(OTP)

    MSG.set_content(msg1)
    MSG['Subject'] = 'SKYTOUCH: OTP for verification'
    MSG['From'] = "skytouch.clairie@gmail.com"
    MSG['To'] = email

    try:
        # s.sendmail("skytouch.clairie@gmail.com", email, msg1)
        s.send_message(MSG)
        print("OTP sent successfully to registered mail id...")
    except:
        print('Invalid Email')
        return 'invalid'

    # OTP verification program
    try:
        iOTP = int(input('Enter the OTP: '))
        if iOTP == OTP:
            print('OTP VERIFIED...')
            # close smtp session
            s.quit()
            return 'verified', email
        else:
            print('Invalid OTP!!!')
            # close smtp session
            s.quit()
            return 'invalid'

    except:
        print('Invalid OTP!!!')
        # close smtp session
        s.quit()
        return 'invalid'

def email():
    """to input email and verify it."""
    mail = input("enter your e-mail: ")
    if len(mail) == 0:
        print('Invalid Email.')
        email()
    elif mail.isspace():
        print('Invalid Email.')
        email()
    else:
        message='''Dear User,
        Thank you for registering at SKYTOUCH. We have received your request for registration.'''
        ans = otp(mail,message)
        if ans[0] == 'verified':

            return ans[1]
        else:
            print('Please input your email again.')
            email()

def mobile():
    """To input mobile no. of user."""
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
    """To input username of user"""
    loop2 = "y"
    while loop2 == "y":
        uname = input("Enter your username= ")
        length = len(uname)
        if length == 0:
            print("Enter a valid username")
            loop2 = "y"

        else:
            for i in reg_data1:
                if uname == i[2]:
                    print("This username already exists. Please select other username")
                    loop2 = "y"
                    break
            else:
                user = uname
                loop2 = "n"
                return user


def password():
    """To change / add password"""
    print("Password should not be less than 8 characters and more than 20 characters")
    print("Password should consist of only digits and alphabets")
    print("No special characters allowed")
    loop3 = "y"
    while loop3 == "y":
        pswd = input("Enter password= ")
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
    for i in reg_data1:
        if str(vt) == i[0]:
            vt = random.randrange(100000, 1000000000)
    else:
        return str(vt)


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
            return name





def basicplanhindi():
    print(Style.BRIGHT + Fore.BLUE + '## BASIC HINDI PLAN ##'.center(45), Style.RESET_ALL)
    print(Style.BRIGHT + Fore.RED + 'Rs 65.00/month' + Style.RESET_ALL)
    print("This plan includes the following channels : ")
    print(Style.BRIGHT + Fore.GREEN + '* DEVOTIONAL' + Style.RESET_ALL)

    devotional = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Sanskar', 'Aastha', 'Arihant', 'Satsang',
         'Divya TV' + Style.RESET_ALL])
    print(devotional)

    print(Style.BRIGHT + Fore.GREEN + '* KIDS' + Style.RESET_ALL)
    kids = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Hungama', 'POGO' + Style.RESET_ALL])
    print(kids)

    print(Style.BRIGHT + Fore.GREEN + '* MUSIC' + Style.RESET_ALL)
    music = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Bindass', 'Zing', 'Masti', 'B4U', '9XM', 'MTV Beats',
         'VH1' + Style.RESET_ALL])
    print(music)

    print(Style.BRIGHT + Fore.GREEN + '* MOVIES' + Style.RESET_ALL)
    movies = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + '& pictures', 'Star gold HD', 'Star movies', 'Sony max',
         'zee cinema', 'Pix', '& flix', 'UTV Action', 'UTV Movies', 'Zee Action' + Style.RESET_ALL])
    print(movies)

    print(Style.BRIGHT + Fore.GREEN + '* SPORTS' + Style.RESET_ALL)
    sports = PrettyTable([Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Star Sports 1' + Style.RESET_ALL])
    print(sports)

    print(Style.BRIGHT + Fore.GREEN + '* NEWS' + Style.RESET_ALL)
    news = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'News 24', 'Aaj Tak', 'Republic Bharat' + Style.RESET_ALL])
    print(news)

    print(
        Style.BRIGHT + Fore.LIGHTRED_EX + "*****************************************************************************************************************",
        Style.RESET_ALL)
    price = 65
    return price


def premiumhindiplan():
    print(Style.BRIGHT + Fore.BLUE + '## PREMIUM HINDI PLAN ##'.center(45), Style.RESET_ALL)
    print(Style.BRIGHT + Fore.RED + 'Rs 165.00/month' + Style.RESET_ALL)
    print("This plan includes the following channels :")

    devotional = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Sanskar', 'Aastha', 'Arihant', 'Satsang' + Style.RESET_ALL])
    print(devotional)

    print(Style.BRIGHT + Fore.GREEN + '* KIDS' + Style.RESET_ALL)
    kids = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Hungama', 'POGO', 'Disney', 'Nicklodeon' + Style.RESET_ALL])
    print(kids)

    print(Style.BRIGHT + Fore.GREEN + '* MUSIC' + Style.RESET_ALL)
    music = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Bindass', 'Zing', 'Masti', 'B4U', '9XM', 'MTV Beats', 'VH1',
         'MTV Beats HD', 'Tarang Music', 'Dhoom Music' + Style.RESET_ALL])
    print(music)

    print(Style.BRIGHT + Fore.GREEN + '* INFOTAINMENT' + Style.RESET_ALL)
    infotainment = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Epic', 'Discovery Science', 'History TV18 HD',
         'Animal planet' + Style.RESET_ALL])
    print(infotainment)

    print(Style.BRIGHT + Fore.GREEN + '* MOVIES' + Style.RESET_ALL)
    movies = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + '& pictures', 'Star gold HD', 'Star movies', 'Sony max',
         'zee cinema', 'sony max hd', '&Prive HD', 'UTV Action', 'UTV Movies', 'Zee Action',
         'B4U Movies' + Style.RESET_ALL])
    print(movies)

    print(Style.BRIGHT + Fore.GREEN + '* SPORTS' + Style.RESET_ALL)
    sports = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Star Sports 1', 'Star Sports 1 HD', 'Star Sports Select 1',
         'DD Sports' + Style.RESET_ALL])
    print(sports)

    print(Style.BRIGHT + Fore.GREEN + '* NEWS' + Style.RESET_ALL)
    news = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'News 24', 'Aaj Tak', 'India News', 'INDIA TV',
         'Republic Bharat', 'DD News', 'NDTV', 'Zee News' + Style.RESET_ALL])
    print(news)

    print(
        Fore.MAGENTA + "You can access our" + Style.BRIGHT + Fore.RED + " DHAMAKA offer" + Fore.MAGENTA + Style.NORMAL + " after purchasing this plan!!!" + Style.RESET_ALL)

    print()
    print(Style.BRIGHT + Fore.BLUE + "dhamaka offer".upper().center(55))
    print()
    print('NO ADS, JUST ENTERTAINMENT AND WORK!!!' + Style.RESET_ALL)
    print(Fore.BLUE + '''Add more masala to your entertainment with SKYTOUCH\'s DHAMAKA active services. From jamming to the most popular music, or 
    finding peace and faith in devotional songs, to setting high scores on our collection of incredibly fun games, 
    there\'s always more you can do with your television.Now you get these amazing services for FREE!!!''')
    print()

    dhamaka = PrettyTable(
        [Style.BRIGHT + Back.LIGHTGREEN_EX, Fore.BLACK + 'COMEDY ACTIVE', 'MOVIES ACTIVE', 'MUSIC ACTIVE',
         'KOREAN DRAMA', 'BHAKTI ACTIVE', 'DANCE ACTIVE' + Style.RESET_ALL])
    print(dhamaka)

    print(
        Style.BRIGHT + Fore.LIGHTRED_EX + "*****************************************************************************************************************",
        Style.RESET_ALL)
    price = 165
    return 165


def basicengplan():
    print(Style.BRIGHT + Fore.BLUE + '## BASIC ENGLISH PLAN ##'.center(45), Style.RESET_ALL)
    print(Style.BRIGHT + Fore.RED + 'Rs 70.00/month' + Style.RESET_ALL)
    print("This plan includes the following channels :")

    print(Style.BRIGHT + Fore.GREEN + '* MOVIES' + Style.RESET_ALL)
    movies = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Movies Now', 'MNX', 'd2h hollywood', 'HBO',
         'WB', 'sony pix' + Style.RESET_ALL])
    print(movies)

    print(Style.BRIGHT + Fore.GREEN + '* MUSIC' + Style.RESET_ALL)
    music = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'VH1', 'mx0', 'nat geo music' + Style.RESET_ALL])
    print(music)

    print(Style.BRIGHT + Fore.GREEN + '* INFOTAINMENT' + Style.RESET_ALL)
    infotainment = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Epic', 'Discovery Science', 'History TV18 HD',
         'Animal planet' + Style.RESET_ALL])
    print(infotainment)

    print(Style.BRIGHT + Fore.GREEN + '* SPORTS' + Style.RESET_ALL)
    sports = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Star Sports 1' + Style.RESET_ALL])
    print(sports)

    print(Style.BRIGHT + Fore.GREEN + '* NEWS' + Style.RESET_ALL)
    news = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'CNN-News18', 'BBC Worldwide (India)', 'DD News',
         'TV18' + Style.RESET_ALL])
    print(news)

    print(
        Style.BRIGHT + Fore.LIGHTRED_EX + "*****************************************************************************************************************",
        Style.RESET_ALL)
    price = 70
    return price


def premiumengplan():
    print(Style.BRIGHT + Fore.BLUE + '## PREMIUM ENGLISH PLAN ##'.center(45), Style.RESET_ALL)
    print(Style.BRIGHT + Fore.RED + 'Rs 179.00/month' + Style.RESET_ALL)
    print("This plan includes the following channels :")

    print(Style.BRIGHT + Fore.GREEN + '* MOVIES' + Style.RESET_ALL)
    movies = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Movies Now', 'MNX', 'd2h hollywood', 'HBO',
         'WB', 'sony pix', 'fox action', 'romedy now', 'warner brothers', 'zee studio' + Style.RESET_ALL])
    print(movies)

    print(Style.BRIGHT + Fore.GREEN + '* MUSIC' + Style.RESET_ALL)
    music = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'VH1', 'mx0', 'nat geo music' + Style.RESET_ALL])
    print(music)

    print(Style.BRIGHT + Fore.GREEN + '* INFOTAINMENT' + Style.RESET_ALL)
    infotainment = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Epic', 'Discovery Science', 'History TV18 HD',
         'Animal planet', 'NAT Geo Wild', 'NAT Geo People', 'sony bbc earth' + Style.RESET_ALL])
    print(infotainment)

    print(Style.BRIGHT + Fore.GREEN + '* SPORTS' + Style.RESET_ALL)
    sports = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Star Sports 1', 'Star Sports 1 HD',
         'Star Sports Select 1' + Style.RESET_ALL])
    print(sports)

    print(Style.BRIGHT + Fore.GREEN + '* NEWS' + Style.RESET_ALL)
    news = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'CNN-News18', 'BBC Worldwide (India)', 'DD News',
         'TV18', 'India News', 'News 24', 'NDTV India' + Style.RESET_ALL])
    print(news)

    print(
        Fore.MAGENTA + "You can access our" + Fore.RESET + Fore.RED + Style.BRIGHT + " DHAMAKA offer" + Fore.RESET + Fore.MAGENTA + Style.NORMAL + " after purchasing this plan!!!" + Style.RESET_ALL)

    print()
    print(Style.BRIGHT + Fore.BLUE + "dhamaka offer".upper().center(55))
    print()
    print('NO ADS, JUST ENTERTAINMENT AND WORK!!!' + Style.RESET_ALL)
    print(Fore.BLUE + '''Add more masala to your entertainment with SKYTOUCH\'s DHAMAKA active services. From jamming to the most popular music, or 
    finding peace and faith in devotional songs, to setting high scores on our collection of incredibly fun games, 
    there\'s always more you can do with your television.Now you get these amazing services for FREE!!!''')
    print()

    dhamaka = PrettyTable(
        [Style.BRIGHT + Back.LIGHTBLUE_EX, Fore.BLACK + 'COMEDY ACTIVE', 'MOVIES ACTIVE', 'MUSIC ACTIVE',
         'KOREAN DRAMA', 'BHAKTI ACTIVE', 'DANCE ACTIVE' + Style.RESET_ALL])
    print(dhamaka)

    print(
        Style.BRIGHT + Fore.LIGHTRED_EX + "*****************************************************************************************************************",
        Style.RESET_ALL)
    price = 179
    return price


def familyplan():
    print(Style.BRIGHT + Fore.BLUE + '## FAMILY PLAN ##'.center(45), Style.RESET_ALL)
    print(Style.BRIGHT + Fore.RED + 'Rs 260.00/month' + Style.RESET_ALL)
    print("This plan includes the following channels :")

    print(Style.BRIGHT + Fore.GREEN + '* INFOTAINMENT' + Style.RESET_ALL)
    infotainment = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Epic', 'Discovery Science', 'History TV18 HD',
         'Animal planet', 'sony bbc earth' + Style.RESET_ALL])
    print(infotainment)

    print(Style.BRIGHT + Fore.GREEN + '* MOVIES' + Style.RESET_ALL)
    movies = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + '& pictures', 'Star gold HD', 'Star movies', 'Sony max',
         'zee cinema', 'sony pix"', 'WB', 'UTV Action', 'd2h hollywood', 'MNX', 'Movies Now', 'HBO' + Style.RESET_ALL])
    print(movies)
    print(Style.BRIGHT + Fore.GREEN + '* SPORTS' + Style.RESET_ALL)
    sports = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Star Sports 1', 'Star Sports 1 HD',
         'Star Sports Select 1', 'DD Sports' + Style.RESET_ALL])
    print(sports)

    print(Style.BRIGHT + Fore.GREEN + '* NEWS' + Style.RESET_ALL)
    news = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'News 24', 'Aaj Tak', 'INDIA TV',
         'Republic Bharat', 'DD News' + Style.RESET_ALL])
    print(news)

    print(Style.BRIGHT + Fore.GREEN + '* MUSIC' + Style.RESET_ALL)
    music = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'MTV', 'Bindass', 'Zing', 'nat geo music', 'B4U', 'VH1',
         'mx0', 'masti' + Style.RESET_ALL])
    print(music)

    print(Style.BRIGHT + Fore.GREEN + '* REGIONAL' + Style.RESET_ALL)
    regional = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Jalsha Movies', 'Zee Cinemalu', 'INDIA TV',
         'STAR Maa' + Style.RESET_ALL])
    print(regional)

    print(Style.BRIGHT + Fore.GREEN + '* KIDS' + Style.RESET_ALL)
    kids = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Hungama', 'POGO', 'Disney', 'Nicklodeon' + Style.RESET_ALL])
    print(kids)

    print(
        Fore.MAGENTA + "You can access our" + Style.BRIGHT + Fore.RED + " SPECIAL offer " + Style.NORMAL + Fore.MAGENTA + "afer purchasing this plan!!!" + Style.RESET_ALL)

    print(
        Style.BRIGHT + Fore.LIGHTRED_EX + "*****************************************************************************************************************",
        Style.RESET_ALL)
    price = 260
    return price


def mahafamilypack():
    print(Style.BRIGHT + Fore.BLUE + '##  MAHA FAMILY PLAN ##'.center(45), Style.RESET_ALL)
    print(Style.BRIGHT + Fore.RED + 'Rs 325.00/month' + Style.RESET_ALL)
    print("This plan includes the following channels :")

    print(Style.BRIGHT + Fore.GREEN + '* INFOTAINMENT' + Style.RESET_ALL)
    infotainment = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Epic', 'Discovery Science', 'History TV18 HD',
         'Animal planet', 'sony bbc earth', 'fashion TV', 'Travel XP' + Style.RESET_ALL])
    print(infotainment)

    print(Style.BRIGHT + Fore.GREEN + '* MOVIES' + Style.RESET_ALL)
    movies = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + '& pictures', 'Star gold HD', 'Star movies', 'Sony max',
         'Sony max HD',
         'zee cinema', 'sony pix"', 'WB', 'UTV Action', 'd2h hollywood', 'MNX', 'Movies Now', 'HBO', 'UTV Movies',
         'warner brothers', 'zee studio', 'zee studio HD', 'romedy now', 'fox action', '&Prive HD',
         'B4U Movies' + Style.RESET_ALL])
    print(movies)

    print(Style.BRIGHT + Fore.GREEN + '* SPORTS' + Style.RESET_ALL)
    sports = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Star Sports 1', 'Star Sports 1 HD',
         'Star Sports Select 1', 'DD Sports', 'SONY TEN 2 HD', 'Star Sports 1 HD Hindi', 'EURO SPORTS HD',
         'Sony Six' + Style.RESET_ALL])
    print(sports)

    print(Style.BRIGHT + Fore.GREEN + '* NEWS' + Style.RESET_ALL)
    news = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'News 24', 'Aaj Tak', 'INDIA TV',
         'Republic Bharat', 'DD News', 'Mirror now', 'India ahead', 'India News', 'Zee News' + Style.RESET_ALL])
    print(news)

    print(Style.BRIGHT + Fore.GREEN + '* MUSIC' + Style.RESET_ALL)
    music = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'MTV', 'Bindass', 'Zing', 'nat geo music', 'B4U', 'VH1',
         'mx0', 'masti', 'MTV Beats', 'MTV Beats HD', 'Tarang Music', 'Dhoom Music', '9x Jalwa' + Style.RESET_ALL])
    print(music)

    print(Style.BRIGHT + Fore.GREEN + '* REGIONAL' + Style.RESET_ALL)
    regional = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Jalsha Movies', 'Zee Cinemalu', 'NANDIGHOSHA TV',
         'STAR Maa', 'Manjari TV' + Style.RESET_ALL])
    print(regional)

    print(Style.BRIGHT + Fore.GREEN + '* KIDS' + Style.RESET_ALL)
    kids = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Hungama', 'POGO', 'Disney', 'Nicklodeon', 'nick jr.',
         'Cartoon Network', 'Disney XD', 'Baby\'s TV' + Style.RESET_ALL])
    print(kids)

    print(
        Style.BRIGHT + Fore.LIGHTRED_EX + "*****************************************************************************************************************",
        Style.RESET_ALL)
    price = 325
    return price


def specialoffer():
    print(Style.BRIGHT + Fore.BLUE + '## SPECIAL OFFER ##'.center(45) + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.MAGENTA + "Purchase  any of our premium plans and get 50% off on NETFLIX basic plan!!")
    print("Purchase our family plan and get 50% off on NETFLIX standard plan" + Style.RESET_ALL)


def display(user):
    print()
    print(Style.BRIGHT+'## PACK Display WINDOW ##'.center(60)+Style.RESET_ALL)
    print()
    print("## Please select your language preference ##")
    print()
    print("Press 1 for hindi")
    print("Press 2 for english")
    print()
    a = input("Enter your choice= ")
    print(
        Style.BRIGHT + Fore.LIGHTRED_EX + "*****************************************************************************************************************",
        Style.RESET_ALL)
    specialoffer()
    print("PURCHASE ANY PLAN AND GET THESE CHANNELS FOR" + Style.BRIGHT + Fore.MAGENTA + " FREE!!!" + Style.RESET_ALL)
    offer = PrettyTable(
        [Style.BRIGHT + Fore.BLACK + Back.LIGHTMAGENTA_EX + 'DISCOVERY', 'NATIONAL GEOGRAPHIC', 'HISTORY TV 18',
         'SCIENCE', 'Animal Planet' + Style.RESET_ALL])
    print(offer)

    print(
        Style.BRIGHT + Fore.LIGHTRED_EX + "*****************************************************************************************************************",
        Style.RESET_ALL)

    if a == '1':
        basicplanhindi()
        premiumhindiplan()
        mahafamilypack()
        familyplan()
        while True:
            print("press 0 to change your language preference", "press 1 to start selecting your package.", sep='\n')

            q = input("enter your choice here:  ")
            if q == "0":
                display(user)
                break
            elif q == '1':
                select(user)
                break
            else:
                print('Please enter a valid choice!!!')

    elif a == '2':
        basicengplan()
        premiumengplan()
        familyplan()
        mahafamilypack()
        while True:
            print("press 0 to change your language preference", "press 1 to start selecting your package.", sep='\n')

            q = input("enter your choice here:  ")
            if q == "0":
                display(user)
                break
            elif q == '1':
                select(user)
                break
            else:
                print('Please enter a valid choice!!!')
    else:
        print(Style.BRIGHT + 'Please enter a valid choice!' + Style.RESET_ALL)
        display(user)


def select(u):
    print(Style.BRIGHT+ '## Pack SELECTION WINDOW ##'.center(60)+Style.RESET_ALL)
    print(f'Welcome {u}')
    print('Press 0 to view our Skytouch Combos')
    print('Press 1 to select Basic Hindi Plan.')
    print('Press 2 to select Premium Hindi Plan.')
    print('Press 3 to select Basic English Plan.')
    print('Press 4 to select Premium English Plan.')
    print('Press 5 to select Family Plan.')
    print('Press 6 to select Maha Family Plan.')
    ch = input('Enter your choice here= ')
    if ch == '1':
        print('You\'ve selected Basic Hindi Plan which includes following channels: ')
        amount = basicplanhindi()
        print()
        print()
        selection_confirm('Basic Hindi Plan', amount, u)
    elif ch == '2':
        print('You\'ve selected Premium Hindi Plan which includes following channels: ')
        amount = premiumhindiplan()
        print()
        print()
        selection_confirm('Premium Hindi Plan', amount, u)
    elif ch == '3':
        print('You\'ve selected Basic English Plan which includes following channels: ')
        amount = basicengplan()
        print()
        print()
        selection_confirm('Basic English Plan', amount, u)
    elif ch == '4':
        print('You\'ve selected Premium English Plan which includes following channels: ')
        amount = premiumengplan()
        print()
        print()
        selection_confirm('Premium English Plan', amount, u)
    elif ch == '5':
        print('You\'ve selected Family Plan which includes following channels: ')
        amount = familyplan()
        print()
        print()
        selection_confirm('Family Plan', amount, u)
    elif ch == '6':
        print('You\'ve selected Maha Family Plan which includes following channels: ')
        amount = mahafamilypack()
        print()
        print()
        selection_confirm('Maha Family Plan', amount, u)
    elif ch == '0':
        display(u)
    else:
        print('Please Enter a valid choice.')
        select(u)


def selection_confirm(pack, price, U):
    print('press 0 to confirm your selection.')
    print('Press 1 to change your selection')
    ans = input('Enter your choice here: ')
    if ans == '0':
        query = f"insert into user_info(username,pack,price) values('{U}','{pack}',{price})"
        mycursor.execute(query)
        mycon.commit()
        print('Press 1 to make payment')
        print('Else press any key to skip payment, you can pay later by logging into your account.')
        ch=input('Enter your choice here: ')
        if ch=='1':
            time_period(price,U)
        else:
            query1 = f"update user_info set paid=0 where username='{U}';"
            mycursor.execute(query1)
            mycon.commit()
            menu()
    elif ans == '1':
        select(U)
    else:
        print('Please enter a valid choice.')
        selection_confirm(pack, price, U)


# channel guide
def guide():
    print(Style.BRIGHT + Fore.RED + "# MOVIES #".center(85) + Style.RESET_ALL)
    x = PrettyTable()
    column_names = [Back.LIGHTYELLOW_EX + Fore.BLUE + Style.BRIGHT + "channel number".upper(),
                    "channel name".upper() + Style.RESET_ALL]
    # for i in range(131,152):
    x.add_column(column_names[0],
                 [Style.BRIGHT + "131", "132", "133", "134", "135", "136", "137", "138", "139", "140", "141", "142",
                  "143", "144", "145", "146", "147", "148", "149", "150", "151" + Style.RESET_ALL])
    x.add_column(column_names[1],
                 ['& pictures', 'Star gold HD', 'Star movies', 'Sony max', 'Sony max HD', 'zee cinema', 'sony pix"',
                  'WB', 'UTV Action', 'd2h hollywood', 'MNX', 'Movies Now', 'HBO', 'UTV Movies', 'warner brothers',
                  'zee studio', 'zee studio HD', 'romedy now', 'fox action', '&Prive HD',
                  'B4U Movies' + Style.RESET_ALL])
    print(x)
    print(Style.BRIGHT + Fore.RED + "# INFOTAINMENT #".center(90) + Style.RESET_ALL)
    y = PrettyTable()
    column_names = [Style.BRIGHT + Fore.BLUE + Back.LIGHTYELLOW_EX + "channel number".upper(),
                    "channel name".upper() + Style.RESET_ALL]
    y.add_column(column_names[0], [111, 112, 113, 114, 115, 116, 117])
    y.add_column(column_names[1], [Style.BRIGHT + 'Epic', 'Discovery Science', 'History TV18 HD', 'Animal planet',
                                   'sony bbc earth'.capitalize(), 'fashion TV'.capitalize(),
                                   'Travel XP' + Style.RESET_ALL])
    print(y)
    print(Style.BRIGHT + Fore.RED + "# SPORTS #".center(90) + Style.RESET_ALL)
    z = PrettyTable()
    column_names = [Style.BRIGHT + Fore.BLUE + Back.LIGHTYELLOW_EX + "channel number".upper(),
                    "channel name".upper() + Style.RESET_ALL]
    z.add_column(column_names[0], [302, 303, 304, 305, 306, 307, 308, 309])
    z.add_column(column_names[1],
                 [Style.BRIGHT + 'Star Sports 1', 'Star Sports 1 HD', 'Star Sports Select 1', 'DD Sports',
                  'SONY TEN 2 HD', 'Star Sports 1 HD Hindi', 'EURO SPORTS HD', 'Sony Six' + Style.RESET_ALL])
    print(z)
    print(Style.BRIGHT + Fore.RED + "# * NEWS #".center(90) + Style.RESET_ALL)
    a = PrettyTable()
    column_names = [Style.BRIGHT + Fore.BLUE + Back.LIGHTYELLOW_EX + "channel number".upper(),
                    "channel name".upper() + Style.RESET_ALL]
    a.add_column(column_names[0], [310, 311, 312, 313, 314, 315, 316, 317, 318])
    a.add_column(column_names[1],
                 [Style.BRIGHT + 'News 24', 'Aaj Tak', 'INDIA TV', 'Republic Bharat', 'DD News', 'Mirror now',
                  'India ahead', 'India News', 'Zee News' + Style.RESET_ALL])
    print(a)
    print(Style.BRIGHT + Fore.RED + "# * MUSIC #".center(90) + Style.RESET_ALL)
    b = PrettyTable()
    column_names = [Style.BRIGHT + Fore.BLUE + Back.LIGHTYELLOW_EX + "channel number".upper(),
                    "channel name".upper() + Style.RESET_ALL]
    b.add_column(column_names[0], [451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463])
    b.add_column(column_names[1],
                 [Style.BRIGHT + 'MTV', 'Bindass', 'Zing', 'nat geo music', 'B4U', 'VH1', 'mx0', 'masti', 'MTV Beats',
                  'MTV Beats HD', 'Tarang Music', 'Dhoom Music', '9x Jalwa' + Style.RESET_ALL])
    print(b)
    print(Style.BRIGHT + Fore.RED + "# REGIONAL #".center(90) + Style.RESET_ALL)
    column_names = [Style.BRIGHT + Fore.BLUE + Back.LIGHTYELLOW_EX + "channel number".upper(),
                    "channel name".upper() + Style.RESET_ALL]
    c = PrettyTable()
    c.add_column(column_names[0], [151, 152, 153, 154, 155])
    c.add_column(column_names[1], [Style.BRIGHT + 'Jalsha Movies', 'Zee Cinemalu', 'NANDIGHOSHA TV', 'STAR Maa',
                                   'Manjari TV' + Style.RESET_ALL])
    print(c)
    print(Style.BRIGHT + Fore.RED + "# KIDS #".center(90) + Style.RESET_ALL)
    d = PrettyTable()
    column_names = [Style.BRIGHT + Fore.BLUE + Back.LIGHTYELLOW_EX + "channel number".upper(),
                    "channel name".upper() + Style.RESET_ALL]
    d.add_column(column_names[0], [291, 292, 293, 294, 295, 296, 297, 298])
    d.add_column(column_names[1],
                 [Style.BRIGHT + 'Hungama', 'POGO', 'Disney', 'Nicklodeon', 'nick jr.', 'Cartoon Network', 'Disney XD',
                  'Baby\'s TV' + Style.RESET_ALL])
    print(d)


# modify pack
def modify(u):
    print(Style.BRIGHT+'## Pack MODIFICATION WINDOW ##'.center(60)+Style.RESET_ALL)
    print("Press 0 to return to your profile.")
    print('Press 1 to select Basic Hindi Plan.')
    print('Press 2 to select Premium Hindi Plan.')
    print('Press 3 to select Basic English Plan.')
    print('Press 4 to select Premium English Plan.')
    print('Press 5 to select Family Plan.')
    print('Press 6 to select Maha Family Plan.')
    ch = input('Enter your choice here= ')
    if ch == '1':
        print('You\'ve selected Basic Hindi Plan which includes following channels: ')
        amount = basicplanhindi()
        print()
        print()
        modify_confirm('Basic Hindi Plan', amount, u)
    elif ch == '2':
        print('You\'ve selected Premium Hindi Plan which includes following channels: ')
        amount = premiumhindiplan()
        print()
        print()
        modify_confirm('Premium Hindi Plan', amount, u)
    elif ch == '3':
        print('You\'ve selected Basic English Plan which includes following channels: ')
        amount = basicengplan()
        print()
        print()
        modify_confirm('Basic English Plan', amount, u)
    elif ch == '4':
        print('You\'ve selected Premium English Plan which includes following channels: ')
        amount = premiumengplan()
        print()
        print()
        modify_confirm('Premium English Plan', amount, u)
    elif ch == '5':
        print('You\'ve selected Family Plan which includes following channels: ')
        amount = familyplan()
        print()
        print()
        modify_confirm('Family Plan', amount, u)
    elif ch == '6':
        print('You\'ve selected Maha Family Plan which includes following channels: ')
        amount = mahafamilypack()
        print()
        print()
        modify_confirm('Maha Family Plan', amount, u)
    elif ch == '0':
        welcome(u)
    else:
        print('Please Enter a valid choice.')
        modify(u)


def modify_confirm(pack, price, U):
    print('Press 0 to confirm your selection.')
    print('Press 1 to change your selection')
    ans = input('Enter your choice here: ')
    if ans == '0':
        amount = time_period(price,U)
        query1=f"select paid from user_info where username='{U}';"
        mycursor.execute(query1)
        balance = mycursor.fetchall()
        mycon.commit()
        final=int(amount-balance)
        query = f"update user_info set pack='{pack}',paid='{final}' where username='{U}';"
        mycursor.execute(query)
        mycon.commit()
    elif ans == '1':
        modify(U)
    else:
        print('Please enter a valid choice.')
        modify_confirm(pack, price, U)

def time_period(am,user):
    # print('############################################################################################################')
    print(Style.BRIGHT+'## OFFERS FOR YOU! ##'.center(60)+Style.RESET_ALL)
    print('On 3 month recharge get 7 Days extra!!')
    print('On 6 month recharge get 15 Days extra!!')
    print('On 1 year recharge get 30 Days extra!!')
    print('###########################################################################################################')
    print("Please select your Skytouch Recharge Time Period...")
    print("Press 0 to recharge for 3 months")
    print('Press 1 to recharge for 6 months')
    print('Press 2 to recharge for 1 year')
    ch=input('Enter your choice here: ')
    if ch=='0':
        Total_amount=am*3
        print(f'Your total amount = Rs. {Total_amount}')
        ans=input('Press 1 to change your time period else press any key to proceed : ')
        if ans=='1':
            time_period(am,user)
        else:

            transaction(Total_amount,user)
        return Total_amount
    elif ch=='1':
        Total_amount = am*6
        print(f'Your total amount = Rs. {Total_amount}')
        ans = input('Press 1 to change your time period else press any key to proceed : ')
        if ans == '1':
            time_period(am,user)
        else:
            transaction(Total_amount,user)
        return Total_amount
    elif ch=='2':
        Total_amount = am*12
        print(f'Your total amount = Rs. {Total_amount}')
        ans = input('Press 1 to change your time period else press any key to proceed : ')
        if ans == '1':
            time_period(am,user)
        else:
            transaction(Total_amount,user)
        return Total_amount
    else:
        print('Please enter a valid choice!!!')
        time_period(am,user)

def transaction(total_amount,User):
    print(Style.BRIGHT+'#Make your payment HERE...##'.center(60)+Style.RESET_ALL)
    print('Select the mode of payment')
    print('Press 1 for net banking.')
    print('Press 2 for Debit card.')
    print('Press 3 for UPI Autopay')

    ch=input('Enter your choice here: ')
    if ch=='1':
        print(Style.BRIGHT+"## NET BANKING WINDOW ##".center(60)+Style.RESET_ALL)
        ans = input('Press 1 to change mode of payment else press any key to proceed: ')
        if ans=='1':
            transaction(total_amount,User)
        else:
            net_banking()
            print(f'Your total amount is= Rs. {total_amount}')
            print(f'Press 1 to pay Rs. {total_amount}')
            print('Press any key to skip the transaction, you can pay later by logging into your account')
            Ans = input('Enter your choice here: ')
            if Ans=='1':
                pay_date = date.today().isoformat()
                query=f"update user_info set paid={total_amount} ,pay_date='{pay_date}' where username='{User}';"
                mycursor.execute(query)
                mycon.commit()
                print('Please Wait, your payment is in process...')
                print("...Do not refresh the page... ")
                print('Payment made successfully!!')
                payment_confirmation(total_amount,User)
            else:
                query = f"update user_info set paid=0;"
                mycursor.execute(query)
                mycon.commit()





    elif ch=='2':
        print(Style.BRIGHT+'## DEBIT CARD WINDOW ##'.center(60)+Style.RESET_ALL)
        ans=input('Press 1 to change mode of payment else press any key to proceed: ')
        if ans=='1':
            transaction(total_amount,User)
        else:

            card_no()
            cardholder()
            expiry_date()
            cvv()
            print(f'Your total amount is= Rs. {total_amount}')
            print(f'Press 1 to pay Rs. {total_amount}')
            print('Press any key to skip the transaction, you can pay later by logging into your account')
            Ans=input('Enter your choice here: ')
            if Ans=='1':
                pay_date = date.today().isoformat()
                query = f"update user_info set paid={total_amount},pay_date='{pay_date}' where username='{User}';"
                mycursor.execute(query)
                mycon.commit()
                print('Please Wait, your payment is in process...')
                print("...Do not refresh the page... ")
                print('Payment made successfully!!')
                payment_confirmation(total_amount,User)
            else:
                query = f"update user_info set paid=0;"
                mycursor.execute(query)
                mycon.commit()

                menu()
    elif ch=="3":
        print(Style.BRIGHT+'## UPI WINDOW ##'.center(60)+Style.RESET_ALL)
        print("UPI AutoPay is a new way to pay with UPI that will charge you automatically every month. "
              "That way you’ll never miss out on your shows and movies.")
        print("Now accepting: @upi, @paytm, @ibl, @axl, @ybl, @apl")
        upi=input("enter you UPI Id= ".capitalize())
        if len(upi)==14 or len(upi)==16:
            if upi[10]=="@":
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



def card_no():
    card_number = input('CARD NUMBER: ')
    if len(card_number)!=16:
        print('Invalid card number!!')
        card_no()
    else:
        return card_number
def cardholder():
    name = input('CARDHOLDER NAME: ').upper()
    if name=='' or name.isspace() or name.isdigit():
        print("Invalid Cardholder name!!")
        cardholder()
    else:
        return name
def expiry_date():
    exp_date = input('EXPIRY DATE (MM/YYYY): ')
    if len(exp_date)!=7:
        print('Invalid expiry date!!')
        expiry_date()
    else:
        return exp_date
def cvv():
    Cvv=input('CVV: ')
    if len(Cvv)!=3:
        print('Invalid CVV!!')
    else:
        return Cvv

def contact():
    print('You can contact us for your  queries, provide feedback and register your complaint at any time. We are pleased to help you! '.upper())
    print("We provide 24/7 service to our customers. Feel free to contact us".upper())
    print('Press 1 to know about our contact  details \nElse press any key to skip'.capitalize())
    ch=input("Enter your choice= ")
    if ch=="1":
        print("You can contact us through our mail provided below:-")
        print(Style.BRIGHT+"skytouch.clairie@gmail.com"+Style.RESET_ALL)
    else:
        menu()


def net_banking():
    print("## Select your bank ##".capitalize())
    print("press 1 to select central bank of india".upper())
    print("press 2 to select HDFC bank".upper())
    print("press 3 to select pnb bank".upper())
    print("press 4 to select SBI".upper())
    ch = input("Enter your choice= ")
    if ch == "1":
        customer_id = input("enter your customer id")
        if len(customer_id) != 11:
            print("Invalid customer id")
        else:
            pswd = input("enter your password= ")
    elif ch == "2":
        customer_id = input("enter your customer id")
        if len(customer_id) != 9:
            print("Invalid customer id")
        else:
            pswd = input("enter your password= ")

    elif ch == "3":
        customer_id = input("enter your customer id")
        if len(customer_id) != 9:
            print("Invalid customer id")
        else:
            pswd = input("enter your password= ")
    elif ch == "4":
        customer_id = input("enter your customer id")
        if len(customer_id) != 11:
            print("invalid customer id")
        else:
            pswd = input("enter your password= ")
    else:
        print('Please enter a valid choice!!')
        net_banking()

def payment_confirmation(t_amount,u):
    from random import randint
    import smtplib
    from email.message import EmailMessage

    reference_no=randint(10000000,99999999)
    receipt_no=randint(1000,9999)
    now=datetime.now()
    t_date= now.strftime('%d %b %Y, %H:%M:%S')

    query=f"select mail,vc from reg where username= '{u}';"
    mycursor.execute(query)
    mail,vc=mycursor.fetchall()[0]
    mycon.commit()

    msg = EmailMessage()

    # create smtp session
    s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
    # start TLS for E-mail security
    s.starttls()
    # Log in to your gmail account
    s.login("skytouch.clairie@gmail.com", "ceilotocco22")

    MSG=' Payment Confirmation:SKYTOUCH '.center(60,'#')+'\n' \
        'Thank you.' \
        'Your payment request has been successfully recorded. Please quote your transaction reference number for' \
        'any queries relating to this request.\n\n'+' Transaction Details '.center(60,'#')+'\n\n'\
        'Transaction status : SUCCESS\n' \
        f'Transaction reference no : {reference_no} \n' \
        f'Transaction date and time: {t_date} \n' \
        f'VC number= {vc} \n' \
        f'Username= {u} \n' \
        f'Receipt Number= {receipt_no} \n'\
        f'Amount Paid= {t_amount} \n'
    print()
    print(MSG)
    msg.set_content(MSG)
    msg['Subject'] = 'SKYTOUCH: PAYMENT CONFIRMATION RECEIPT'
    msg['From'] = "skytouch.clairie@gmail.com"
    msg['To'] = mail
    s.send_message(msg)
    print('Payment slip has been sent to your registered mail id.Thank You!')
    print()
    s.quit()


menu()


