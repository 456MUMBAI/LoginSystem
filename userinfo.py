
import random
from prettytable import PrettyTable
from colorama import Fore, Back, Style

def basicplanhindi():

    print(Style.BRIGHT + Fore.BLUE + '## BASIC HINDI PLAN ##'.center(45), Style.RESET_ALL)
    print(Style.BRIGHT + Fore.RED +'Rs 65.00'+ Style.RESET_ALL)
    print("This plan includes the following channels : ")
    print(Style.BRIGHT + Fore.GREEN + '* DEVOTIONAL' + Style.RESET_ALL)
    devotional = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Sanskar', 'Aastha', 'Arihant', 'Satsang',
         'Divya TV' + Style.RESET_ALL])
    print(devotional)
    # print("                    sanskar                       ")
    # print("                    aastha                         ")
    # print("                    arihant                         ")
    # print("                     satsang                        ")
    # print("                     divya tv                       ")


    # print("******************2 kids channel****************************")
    # print("                   hungama                     ")
    # print("                     pogo                       ")
    print(Style.BRIGHT + Fore.GREEN + '* KIDS' + Style.RESET_ALL)
    kids = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Hungama', 'POGO' + Style.RESET_ALL])
    print(kids)

    # print("**************************7 music channels*************************")
    # print("                      Bindass                  ")
    # print("                       Zing                     ")
    # print("                       Masti                    ")
    # print("                       B4U                       ")
    # print("                       9XM                       ")
    # print("                    MTV Beats                    ")
    # print("                         VH1                        ")

    print(Style.BRIGHT + Fore.GREEN + '* MUSIC' + Style.RESET_ALL)
    music = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Bindass', 'Zing','Masti','B4U','9XM','MTV Beats','VH1' + Style.RESET_ALL])
    print(music)
    # print(" ************************10 movies channel****************************")
    # print("                   & pictures")
    # print("                   Star gold HD")
    # print("                    Star movies")
    # print("                    Sony max")
    # print("                   zee cinema")
    # print("                        Pix")
    # print("                     & flix")
    # print("                  UTV Action")
    # print("                  UTV Movies")
    # print("                    Zee Action")
    print(Style.BRIGHT + Fore.GREEN + '* MOVIES' + Style.RESET_ALL)
    movies = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + '& pictures', 'Star gold HD','Star movies','Sony max','zee cinema','Pix','& flix','UTV Action','UTV Movies','Zee Action' + Style.RESET_ALL])
    print(movies)

    # print("***********************1 sport channel***********************")
    # print("                 Star Sports 1")
    print(Style.BRIGHT + Fore.GREEN + '* SPORTS' + Style.RESET_ALL)
    sports = PrettyTable([Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Star Sports 1'+ Style.RESET_ALL])
    print(sports)

    # print("************* 1 news channel**********************")
    # print("                    news 24")
    print(Style.BRIGHT + Fore.GREEN + '* NEWS' + Style.RESET_ALL)
    news = PrettyTable([Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'News 24','Aaj Tak','Republic Bharat' + Style.RESET_ALL])
    print(news)



def premiumhindiplan():
    print(Style.BRIGHT + Fore.BLUE + '## PREMIUM HINDI PLAN ##'.center(45), Style.RESET_ALL)
    print(Style.BRIGHT + Fore.RED + 'Rs 165.00' + Style.RESET_ALL)
    print("This plan includes the following channels :")

    # print("************5 famous devotional channels*************")
    # print("                    sanskar")
    # print("                     aastha")
    # print("                    arihant")
    # print("                  satsang")
    # print
    devotional = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Sanskar', 'Aastha', 'Arihant', 'Satsang' + Style.RESET_ALL])
    print(devotional)
    #
    # print("*******************4 kids channel*************************")
    # print("     hungama")
    # print(         "pogo")
    # print("        disney")
    # print("      nicklodeon")
    print(Style.BRIGHT + Fore.GREEN + '* KIDS' + Style.RESET_ALL)
    kids = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Hungama', 'POGO','Disney','Nicklodeon' + Style.RESET_ALL])
    print(kids)

    # print("**********************10 music channels******************")
    # print("         Bindass")
    # print("         Zing")
    # print("         masti")
    # print("         B4U")
    # print("          9XM")
    # print("        MTV Beats")
    # print("          VH1")
    # print("       MTV Beats HD")
    # print("          Tarang Music")
    # print("         Dhoom Music")
    print(Style.BRIGHT + Fore.GREEN + '* MUSIC' + Style.RESET_ALL)
    music = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Bindass', 'Zing','Masti','B4U','9XM','MTV Beats','VH1','MTV Beats HD','Tarang Music','Dhoom Music' + Style.RESET_ALL])
    print(music)
    # print("********* 4 infotainment channels************")
    # print("       Epic")
    # print("     Discovery Science")
    # print("      History TV18 HD")
    # print("       Animal planet")
    print(Style.BRIGHT + Fore.GREEN + '* INFOTAINMENT' + Style.RESET_ALL)
    infotainment = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Epic', 'Discovery Science', 'History TV18 HD', 'Animal planet' + Style.RESET_ALL])
    print(infotainment)
    # print("*************12 movies channel*******************")
    # print("& pictures")
    # print("star gold hd")
    # print("star movies")
    # print("sony max")
    # print("zee cinema")
    # print("sony max ")
    # print("sony max hd")
    # print("UTV Action")
    # print("UTV Movies")
    # print("Zee Action")
    # print("&Prive HD")
    # print("B4U Movies")
    print(Style.BRIGHT + Fore.GREEN + '* MOVIES' + Style.RESET_ALL)
    movies = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + '& pictures', 'Star gold HD', 'Star movies', 'Sony max',
         'zee cinema', 'sony max hd', '&Prive HD', 'UTV Action', 'UTV Movies', 'Zee Action','B4U Movies' + Style.RESET_ALL])
    print(movies)

    # print("**************3 sports channels****************")
    # print("   Star Sports 1")
    # print("     Star Sports 1 HD")
    # print("    Star Sports Select 1")
    print(Style.BRIGHT + Fore.GREEN + '* SPORTS' + Style.RESET_ALL)
    sports = PrettyTable([Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Star Sports 1','Star Sports 1 HD','Star Sports Select 1','DD Sports' + Style.RESET_ALL])
    print(sports)
    # print("***************************** 3 news channels*************************")
    # print("   India News")
    # print("    INDIA TV")
    # print("    news 24")
    print(Style.BRIGHT + Fore.GREEN + '* NEWS' + Style.RESET_ALL)
    news = PrettyTable([Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'News 24', 'Aaj Tak', 'India News','INDIA TV','Republic Bharat','DD News','NDTV','Zee News' + Style.RESET_ALL])
    print(news)

    print(Fore.MAGENTA + "You can access our" + Style.BRIGHT + " DHAMAKA offer"+ Style.NORMAL + " after purchasing this plan!!!"+Style.RESET_ALL)


def basicengplan():
    print(Style.BRIGHT + Fore.BLUE + '## BASIC ENGLISH PLAN ##'.center(45), Style.RESET_ALL)
    print(Style.BRIGHT + Fore.RED + 'Rs 70.00' + Style.RESET_ALL)
    print("This plan includes the following channels :")
    # print("*************6 movies channels***********************")
    # print("Movies Now")
    # print("MNX")
    # print("d2h hollywood")
    # print("HBO")
    # print("WB")
    # print("sony pix")
    print(Style.BRIGHT + Fore.GREEN + '* MOVIES' + Style.RESET_ALL)
    movies = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Movies Now', 'MNX', 'd2h hollywood', 'HBO',
         'WB', 'sony pix' + Style.RESET_ALL])
    print(movies)

    # print("*******************************3 music channels**************************")
    # print("       VH1")
    # print("      mx0")
    # print("      nat geo music")
    print(Style.BRIGHT + Fore.GREEN + '* MUSIC' + Style.RESET_ALL)
    music = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'VH1', 'mx0', 'nat geo music' + Style.RESET_ALL])
    print(music)
    # print("********* 4 infotainment channels************")
    # print("      Epic")
    # print("  Discovery Science")
    # print("   History TV18 HD")
    # print("    Animal planet")
    print(Style.BRIGHT + Fore.GREEN + '* INFOTAINMENT' + Style.RESET_ALL)
    infotainment = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Epic', 'Discovery Science', 'History TV18 HD',
         'Animal planet' + Style.RESET_ALL])
    print(infotainment)
    # print("***********************1 sport channel***********************")
    # print("                       Star Sports 1")
    print(Style.BRIGHT + Fore.GREEN + '* SPORTS' + Style.RESET_ALL)
    sports = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Star Sports 1'+ Style.RESET_ALL])
    print(sports)
    # print("************* 1 news channel**********************")
    # print("                      news 24")
    print(Style.BRIGHT + Fore.GREEN + '* NEWS' + Style.RESET_ALL)
    news = PrettyTable([Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK +'CNN-News18','BBC Worldwide (India)','DD News','TV18' + Style.RESET_ALL])
    print(news)

def premiumengplan():
    print(Style.BRIGHT + Fore.BLUE + '## PREMIUM ENGLISH PLAN ##'.center(45), Style.RESET_ALL)
    print(Style.BRIGHT + Fore.RED + 'Rs 179.00' + Style.RESET_ALL)
    print("This plan includes the following channels :")

    # print("*************12 movies channels***********************")
    # print("Movies Now")
    # print("MNX")
    # print("d2h hollywood")
    # print("HBO")
    # print("WB")
    # print("sony pix")
    # print("fox action")
    # print("romedy now")
    # print("sony pix")
    # print("warner brothers")
    # print("zee studio")
    # print("zee studio HD")
    print(Style.BRIGHT + Fore.GREEN + '* MOVIES' + Style.RESET_ALL)
    movies = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Movies Now', 'MNX', 'd2h hollywood', 'HBO',
         'WB', 'sony pix','fox action','romedy now','sony pix','warner brothers','zee studio','zee studio HD' + Style.RESET_ALL])
    print(movies)

    # print("*******************************4 music channels**************************")
    # print("                                    VH1")
    # print("                                     mx0")
    # print("                                 nat geo music")
    # print("                                international mix")
    print(Style.BRIGHT + Fore.GREEN + '* MUSIC' + Style.RESET_ALL)
    music = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'VH1', 'mx0', 'nat geo music' + Style.RESET_ALL])
    print(music)


    # print("********* 7 infotainment channels************")
    # print("               Epic")
    # print("           Discovery Science")
    # print("           History TV18 HD")
    # print("            Animal planet")
    # print("           NAT Geo Wild")
    # print("            NAT Geo People")
    # print(            "sony bbc earth")
    print(Style.BRIGHT + Fore.GREEN + '* INFOTAINMENT' + Style.RESET_ALL)
    infotainment = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Epic', 'Discovery Science', 'History TV18 HD',
         'Animal planet','NAT Geo Wild','NAT Geo People','sony bbc earth' + Style.RESET_ALL])
    print(infotainment)

    print(Style.BRIGHT + Fore.GREEN + '* SPORTS' + Style.RESET_ALL)
    sports = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Star Sports 1','Star Sports 1 HD','Star Sports Select 1' + Style.RESET_ALL])
    print(sports)

    # print(" ***************3 news channels******************")
    # print("India News")
    # print("INDIA TV")
    # print("news 24")
    print(Style.BRIGHT + Fore.GREEN + '* NEWS' + Style.RESET_ALL)
    news = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'CNN-News18', 'BBC Worldwide (India)', 'DD News',
         'TV18','India News','News 24','NDTV India' + Style.RESET_ALL])
    print(news)
    print(Fore.MAGENTA + "You can access our" + Fore.RESET+ Fore.RED + Style.BRIGHT + " DHAMAKA offer"+ Fore.RESET+ Fore.MAGENTA+ Style.NORMAL + " after purchasing this plan!!!"+Style.RESET_ALL)

def familyplan():
    print(Style.BRIGHT + Fore.BLUE + '## FAMILY PLAN ##'.center(45), Style.RESET_ALL)
    print(Style.BRIGHT + Fore.RED + 'Rs 260.00' + Style.RESET_ALL)
    print("This plan includes the following channels :")
    # print("********* 4 infotainment channels************")
    # print("                  Epic")
    # print("                  Discovery Science")
    # print("                    History TV18 HD")
    # print("                  Animal planet")
    print(Style.BRIGHT + Fore.GREEN + '* INFOTAINMENT' + Style.RESET_ALL)
    infotainment = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Epic', 'Discovery Science', 'History TV18 HD',
         'Animal planet','sony bbc earth' + Style.RESET_ALL])
    print(infotainment)

    # print("*************12 movies channels***********************")
    # print("Movies Now")
    # print("MNX")
    # print("d2h hollywood")
    # print("HBO")
    # print("WB")
    # print("sony pix")
    # print("& pictures")
    # print("star gold hd")
    # print("star movies")
    # print("sony max")
    # print("zee cinema")
    # print("sony max")
    print(Style.BRIGHT + Fore.GREEN + '* MOVIES' + Style.RESET_ALL)
    movies = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + '& pictures', 'Star gold HD', 'Star movies', 'Sony max',
         'zee cinema', 'sony pix"', 'WB', 'UTV Action', 'd2h hollywood', 'MNX','Movies Now','HBO' + Style.RESET_ALL])
    print(movies)
    # print("***************3 sports channels***************")
    # print("               Star Sports 1")
    # print("                Star Sports 1 HD")
    # print("             Star Sports Select 1")
    print(Style.BRIGHT + Fore.GREEN + '* SPORTS' + Style.RESET_ALL)
    sports = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Star Sports 1', 'Star Sports 1 HD',
         'Star Sports Select 1','DD Sports' + Style.RESET_ALL])
    print(sports)

    # print(" ***************3 news channels******************")
    # print("              India News")
    # print("              INDIA TV")
    # print("               news 24")
    print(Style.BRIGHT + Fore.GREEN + '* NEWS' + Style.RESET_ALL)
    news = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'News 24', 'Aaj Tak', 'INDIA TV',
         'Republic Bharat', 'DD News' + Style.RESET_ALL])
    print(news)

    # print("**********************7 music channels******************")
    # print("Bindass")
    # print("Zing")
    # print("masti")
    # print("B4U")
    # print("VH1")
    # print("mx0")
    # print("nat geo music")
    print(Style.BRIGHT + Fore.GREEN + '* MUSIC' + Style.RESET_ALL)
    music = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'MTV','Bindass', 'Zing', 'nat geo music','B4U','VH1','mx0','masti' + Style.RESET_ALL])
    print(music)

    # print("************************** 3 regional channels ************************")
    # print("        Jalsha Movies")
    # print("         Zee Cinemalu")
    # print("         STAR Maa")
    print(Style.BRIGHT + Fore.GREEN + '* REGIONAL' + Style.RESET_ALL)
    regional = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Jalsha Movies', 'Zee Cinemalu', 'INDIA TV',
         'STAR Maa' + Style.RESET_ALL])
    print(regional)

    # print("*******************5 kids channel*************************")
    # print("hungama")
    # print("pogo")
    # print("disney")
    # print("nicklodeon")
    # print("nick jr.")
    print(Style.BRIGHT + Fore.GREEN + '* KIDS' + Style.RESET_ALL)
    kids = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Hungama', 'POGO', 'Disney', 'Nicklodeon' + Style.RESET_ALL])
    print(kids)

    # print("you can avail  our special offer through this plan")
    print(Fore.MAGENTA + "You can access our" + Style.BRIGHT + " SPECIAL offer"+ Style.NORMAL + "afer purchasing this plan!!!"+Style.RESET_ALL)





def mahafamilypack():
    print(Style.BRIGHT + Fore.BLUE + '## FAMILY PLAN ##'.center(45), Style.RESET_ALL)
    print(Style.BRIGHT + Fore.RED + 'Rs 325.00' + Style.RESET_ALL)
    print("This plan includes the following channels :")

    # print("********* 7 infotainment channels************")
    # print("                   Epic")
    # print("              Discovery Science")
    # print("              History TV18 HD")
    # print("                Animal planet")
    # print("                 fashion TV")
    # print("                   Travel XP")
    print(Style.BRIGHT + Fore.GREEN + '* INFOTAINMENT' + Style.RESET_ALL)
    infotainment = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Epic', 'Discovery Science', 'History TV18 HD',
         'Animal planet', 'sony bbc earth','fashion TV','Travel XP' + Style.RESET_ALL])
    print(infotainment)

    # print("*************24 movies channels***********************")
    # print("Movies Now")
    # print("MNX")
    # print("d2h hollywood")
    # print("HBO")
    # print("WB")
    # print("sony pix")
    # print("& pictures")
    # print("star gold hd")
    # print("star movies")
    # print("sony max")
    # print("zee cinema")
    # print("sony max")
    # print("sony max hd")
    # print("UTV Action")
    # print("UTV Movies")
    # print("Zee Action")
    # print("&Prive HD")
    # print("B4U Movies")
    # print("fox action")
    # print("romedy now")
    # print("sony pix")
    # print("warner brothers")
    # print("zee studio")
    # print("zee studio HD")
    print(Style.BRIGHT + Fore.GREEN + '* MOVIES' + Style.RESET_ALL)
    movies = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + '& pictures', 'Star gold HD', 'Star movies', 'Sony max','Sony max HD',
         'zee cinema', 'sony pix"', 'WB', 'UTV Action', 'd2h hollywood', 'MNX', 'Movies Now', 'HBO','UTV Movies',
         'warner brothers','zee studio','zee studio HD','romedy now','fox action','&Prive HD','B4U Movies' + Style.RESET_ALL])
    print(movies)
    # print("*************** 7 sports channels***************")
    # print("      Star Sports 1")
    # print("       Star Sports 1 HD")
    # print("      Star Sports Select 1")
    # print("        EURO SPORTS HD")
    # print("      Sony Six")
    # print("        SONY TEN 2 HD")
    # print("      Star Sports 1 HD Hindi")
    print(Style.BRIGHT + Fore.GREEN + '* SPORTS' + Style.RESET_ALL)
    sports = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Star Sports 1', 'Star Sports 1 HD',
         'Star Sports Select 1', 'DD Sports','SONY TEN 2 HD','Star Sports 1 HD Hindi','EURO SPORTS HD','Sony Six' + Style.RESET_ALL])
    print(sports)

    # print(" ***************5 news channels******************")
    # print("       India News")
    # print("          INDIA TV")
    # print("         news 24")
    # print("        mirror now")
    # print("      india ahead ")
    print(Style.BRIGHT + Fore.GREEN + '* NEWS' + Style.RESET_ALL)
    news = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'News 24', 'Aaj Tak', 'INDIA TV',
         'Republic Bharat', 'DD News','Mirror now','India ahead','India News','Zee News' + Style.RESET_ALL])
    print(news)
    # print("**********************12 music channels******************")
    # print("Bindass")
    # print("Zing")
    # print("masti")
    # print("B4U")
    # print("VH1")
    # print("mx0")
    # print("nat geo music")
    # print("MTV Beats")
    # print("MTV Beats HD")
    # print("Tarang Music")
    # print("Dhoom Music")
    # print("9x Jalwa")
    print(Style.BRIGHT + Fore.GREEN + '* MUSIC' + Style.RESET_ALL)
    music = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'MTV', 'Bindass', 'Zing', 'nat geo music', 'B4U', 'VH1',
         'mx0', 'masti','MTV Beats','MTV Beats HD','Tarang Music','Dhoom Music','9x Jalwa' + Style.RESET_ALL])
    print(music)

    # print("************************** 5 regional channels ************************")
    # print("      Jalsha Movies")
    # print("       Zee Cinemalu")
    # print("         STAR Maa")
    # print("       NANDIGHOSHA TV")
    # print("        Manjari TV")
    print(Style.BRIGHT + Fore.GREEN + '* REGIONAL' + Style.RESET_ALL)
    regional = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Jalsha Movies', 'Zee Cinemalu', 'NANDIGHOSHA TV',
         'STAR Maa','Manjari TV' + Style.RESET_ALL])
    print(regional)

    # print("*******************5 kids channel*************************")
    # print("hungama")
    # print("pogo")
    # print("disney")
    # print("nicklodeon")
    # print("nick jr.")
    print(Style.BRIGHT + Fore.GREEN + '* KIDS' + Style.RESET_ALL)
    kids = PrettyTable(
        [Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLACK + 'Hungama', 'POGO', 'Disney', 'Nicklodeon','nick jr.',
         'Cartoon Network','Disney XD','Baby\'s TV' + Style.RESET_ALL])
    print(kids)




def specialoffer():
    print(Style.BRIGHT+Fore.BLUE+'## SPECIAL OFFER ##'.center(45)+Style.RESET_ALL)
    print(Style.BRIGHT+Fore.MAGENTA+"Purchase  any of our premium plans and get 50% off on NETFLIX basic plan!!")
    print("Purchase our family plan and get 50% off on NETFLIX standard plan"+Style.RESET_ALL)


def basic():
    print(Style.BRIGHT+ Fore.BLACK+"## Please select your language preference ##")
    print("Press 1 for hindi")
    print("Press 2 for english")
    print("Press 3 for others")
    a=int(input("Enter your choice= "))
    if a == 1:
        print("PURCHASE ANY PLAN AND GET THESE CHANNELS FOR" +Style.BRIGHT+ Fore.MAGENTA+ "FREE!!!"+Style.RESET_ALL)
        # print("                  1)DISCOVERY                     ")
        # print("                2)NATIONAL GEOGRAPHIC              ")
        # print("                   3)HISTORY TV 18                  ")
        # print("                     4)SCIENCE                       ")
        offer=PrettyTable([Style.BRIGHT+Fore.BLACK+Back.LIGHTMAGENTA_EX+'DISCOVERY','NATIONAL GEOGRAPHIC','HISTORY TV 18','SCIENCE','Animal Planet'+Style.RESET_ALL])
        print(offer)
        basicplanhindi()
        premiumhindiplan()
        print("*************************************************************")
        print("*************************************************************")
        print("dhamaka offer")
        print("If you are going to select  any of our  plans:")
        print("You can add  any 4 channels you want for rupees 3 ")
        print("***********************")
        print("*************************************************************")
        print("press 0 if you want to view details about other plans else press any key to skip")
        q = input("please enter ")
        if q == "0":
            basicengplan()
            premiumengplan()
            familyplan()
            mahafamilypack()
            print("*****************************************************************************")
            specialoffer()
            print("******************************************************************************")


        else:
            print(" press 0 if you want to change your language preference else press any key to skip")
            r = input("please enter")
            if r == "0":
                basic()


    if a == 2:
        print("PURCHASE ANY PLAN AND GET THESE CHANNELS FOR FREE:")
        print("                  1)DISCOVERY                     ")
        print("                2)NATIONAL GEOGRAPHIC              ")
        print("                   3)HISTORY TV 18                  ")
        print("                     4)SCIENCE                       ")
        basicengplan()
        premiumengplan()
        print("*************************************************************")
        print("*****************************************")
        print("dhamaka offer")
        print("If you are going to select  any of our plans:")
        print("You can add any 4 channels you want for rupees 3 ")
        print("***********************")
        print("******************************************************************")
        print("press 0 if you want to view details about other plans else press any key to skip")
        q = input("please enter ")
        if q == "0":
            basicplanhindi()
            premiumhindiplan()
            familyplan()
            mahafamilypack()
            print("*****************************************************************************")
            specialoffer()
            print("******************************************************************************")


        else:
            print(" press 0 if you want to change your language preference else press any key to skip")
            r = input("please enter")
            if r == "0":
                basic()


    if a==3:
        print("PURCHASE ANY PLAN AND GET THESE CHANNELS FOR FREE:")
        print("                  1)DISCOVERY                     ")
        print("                2)NATIONAL GEOGRAPHIC              ")
        print("                   3)HISTORY TV 18                  ")
        print("                     4)SCIENCE                       ")
        print("please enter the name of  channel that you would like to have")
        while True:
            chnl=input("please enter")
            print("Price of the",chnl,"that you have selected is",random.randint(1,12))
            choice=input("do you want to add more channels(y/n)=")
            if choice!="y":
                break


basic()
print("#####################################################################################")
print("press 0 if you want to make your plan through single channels else press any key to skip")
s=input("please enter=")
print("#####################################################################################")
print("please enter the name of  channel that you would like to have")
if s=="0":
    while True:
        chnl = input("please enter")
        print("Price of the", chnl, "that you have selected is", random.randint(1, 12))
        choice = input("do you want to add more channels(y/n)=")
        if choice != "y":
            break

print(" we are best known for providing entertainment and knowledge at cheap and affordable rates ")
print("**************Thank you for viewing  our plans *****************")


#hello
#hi
#tanya









