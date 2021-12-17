from prettytable import PrettyTable
from colorama import Fore, Back, Style
# import main
# import reg

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
    price=65
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
    price=165
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
    price=70
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
    price=179
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
    price=260
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
    price=325
    return price

def specialoffer():
    print(Style.BRIGHT + Fore.BLUE + '## SPECIAL OFFER ##'.center(45) + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.MAGENTA + "Purchase  any of our premium plans and get 50% off on NETFLIX basic plan!!")
    print("Purchase our family plan and get 50% off on NETFLIX standard plan" + Style.RESET_ALL)


def display():
    print('## PACK Display WINDOW ##')
    print("## Please select your language preference ##")
    print("Press 1 for hindi")
    print("Press 2 for english")
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
        print("press 0 to change your language preference","press 1 to start selecting your package.",sep='\n')
        q = input("enter your choice here:  ")
        if q == "0":
            display()
        elif q== '1':
            select()
        else:
            pass

    elif a == '2':
        basicengplan()
        premiumengplan()
        familyplan()
        mahafamilypack()
        print("press 0 to change your language preference", "press 1 to start selecting your package.", sep='\n')
        q = input("enter your choice here:  ")
        if q == "0":
            display()
        elif q == '1':
            select()
        else:
            pass

    else:
        print(Style.BRIGHT + 'Please enter a valid choice!' + Style.RESET_ALL)
        display()


# basic()

# print(
#     Fore.BLUE + Style.BRIGHT + " We are best known for providing entertainment and knowledge at cheap and affordable rates ")
# print("**************Thank you for viewing  our plans *****************" + Style.RESET_ALL)


def select():
    #menu
    print(f'Welcome !!')
    print('Press 0 to view our Skytouch Combos')
    print('Press 1 to select Basic Hindi Plan.')
    print('Press 2 to select Premium Hindi Plan.')
    print('Press 3 to select Basic English Plan.')
    print('Press 4 to select Premium English Plan.')
    print('Press 5 to select Family Plan.')
    print('Press 6 to select Maha Family Plan.')
    ch= input('Enter your choice here= ')
    if ch=='1':
        print('You\'ve selected Basic Hindi Plan which includes following channels: ')
        amount=basicplanhindi()
        print()
        print()
        confirm('Basic Hindi Plan',amount)
    elif ch=='2':
        print('You\'ve selected Premium Hindi Plan which includes following channels: ')
        amount=premiumhindiplan()
        print()
        print()
        confirm('Premium Hindi Plan',amount)
    elif ch=='3':
        print('You\'ve selected Basic English Plan which includes following channels: ')
        amount=basicengplan()
        print()
        print()
        confirm('Basic English Plan',amount)
    elif ch=='4':
        print('You\'ve selected Premium English Plan which includes following channels: ')
        amount=premiumengplan()
        print()
        print()
        confirm('Premium English Plan',amount)
    elif ch=='5':
        print('You\'ve selected Family Plan which includes following channels: ')
        amount=familyplan()
        print()
        print()
        confirm('Family Plan',amount)
    elif ch=='6':
        print('You\'ve selected Maha Family Plan which includes following channels: ')
        amount=mahafamilypack()
        print()
        print()
        confirm('Maha Family Plan',amount)
    elif ch=='0':
        display()
    else:
        print('Please Enter a valid choice.')
        select()


def confirm(pack,price):
    print('press 0 to confirm your selection.')
    print('Press 1 to change your selection')
    ans=input('Enter your choice here: ')
    if ans=='0':
        query = f"insert into user_info values('{reg.details.u}','{pack},'{price}')"
        main.mycursor.execute(query)
        main.mycon.commit()
        pass
    elif ans=='1':
        select()
    else:
        print('Please enter a valid choice.')
        confirm(pack,price)




