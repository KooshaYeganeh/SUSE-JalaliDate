from persiantools.jdatetime import JalaliDate, JalaliDateTime
from persiantools import characters, digits
import datetime
import pytz
import sys
from colorama import init
from colorama import Fore, Back, Style




now = JalaliDateTime.now()
today = JalaliDate.today()


year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second



main_date = JalaliDateTime(year, month, day, hour, minute , second ,0, pytz.utc).strftime("%c")


digit = JalaliDate(year, month, day).strftime("%Y/%m/%d")

info = "> Developer : koosha Yeganeh\n> GitHub : https://github.com/KooshaYeganeh\n> DockerHub : https://hub.docker.com/u/kooshakooshadv\n> GitBooks : kooshayeganeh.gitbook.io\nAnd a Little More :)"


try:
    if sys.argv[1] == "-h" or sys.argv[1] == "--human":
        print(Fore.GREEN + Style.BRIGHT + "--- openSUSE JalaiDate --- ")
        print(Fore.GREEN + Style.BRIGHT +  f"{main_date}")
    elif sys.argv[1] == "-d" or sys.argv[1] == "--digit":
        print(Fore.GREEN + Style.BRIGHT + "--- openSUSE JalaiDate --- ")
        print(Fore.GREEN + Style.BRIGHT +  f"\t{digit}")
    elif sys.argv[1] == "-v" or sys.argv[1] == "--verbose":
        print(Fore.GREEN + Style.BRIGHT + "--- openSUSE JalaiDate --- ")
        print(Fore.GREEN + Style.BRIGHT +  f"{main_date}")
        print(Fore.GREEN + Style.BRIGHT + f"{digit}")
    elif sys.argv[1] == "-i" or sys.argv[1] == "--info":
        print(Fore.GREEN + Style.BRIGHT + "--- openSUSE JalaiDate --- ")
        print(Fore.GREEN + Style.BRIGHT + f"{info}")

except:
    print(Fore.GREEN + Style.BRIGHT + "--- openSUSE JalaiDate --- ")
    print(Fore.GREEN + Style.BRIGHT +  f"{main_date}")
    print(Fore.GREEN + Style.BRIGHT + f"\t{digit}")
