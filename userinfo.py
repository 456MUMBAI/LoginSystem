from prettytable import PrettyTable
from colorama import Fore, Back, Style


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


def specialoffer():
    print(Style.BRIGHT + Fore.BLUE + '## SPECIAL OFFER ##'.center(45) + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.MAGENTA + "Purchase  any of our premium plans and get 50% off on NETFLIX basic plan!!")
    print("Purchase our family plan and get 50% off on NETFLIX standard plan" + Style.RESET_ALL)


def basic():
    specialoffer()
    print("## Please select your language preference ##")
    print("Press 1 for hindi")
    print("Press 2 for english")
    a = input("Enter your choice= ")

    print(
        Style.BRIGHT + Fore.LIGHTRED_EX + "*****************************************************************************************************************",
        Style.RESET_ALL)

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
        print("press 0 to change your language preference else press any key to skip")
        q = input("enter your choice here:  ")
        if q == "0":
            basic()


        else:
            pass

    elif a == '2':
        basicengplan()
        premiumengplan()
        familyplan()
        mahafamilypack()

        print("press 0 to change your language preference else press any key to skip")
        q = input("enter your choice here:  ")

        if q == "0":
            basic()

        else:
            pass

    else:
        print(Style.BRIGHT + 'Please enter a valid choice!' + Style.RESET_ALL)
        basic()


basic()

print(
    Fore.BLUE + Style.BRIGHT + " We are best known for providing entertainment and knowledge at cheap and affordable rates ")
print("**************Thank you for viewing  our plans *****************" + Style.RESET_ALL)


# print('i')
# dsfdf