from persiantools.jdatetime import JalaliDate, JalaliDateTime
import datetime
import pytz
import sys
import platform
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# ASCII art for openSUSE logo
opensuse_logo = """



┏┓┳┳┏┓┏┓  ┏┳   ┓
┗┓┃┃┗┓┣    ┃┏┏┓┃
┗┛┗┛┗┛┗┛  ┗┛┗┗┻┗
                


"""

# Display openSUSE logo at the start
print(Fore.GREEN + opensuse_logo)

# Get current date and time
now = JalaliDateTime.now()
today = JalaliDate.today()

year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

# Formatted dates
main_date = JalaliDateTime(year, month, day, hour, minute, second, 0, pytz.utc).strftime("%c")
digit_date = JalaliDate(year, month, day).strftime("%Y/%m/%d")
weekday = today.strftime("%A")

# Developer info
info = (f"{Fore.YELLOW}> Developer: Koosha Yeganeh\n"
        f"{Fore.YELLOW}> GitHub: {Fore.CYAN}https://github.com/KooshaYeganeh\n"
        f"{Fore.YELLOW}> DockerHub: {Fore.CYAN}https://hub.docker.com/u/kooshakooshadv\n"
        f"{Fore.YELLOW}> GitBooks: {Fore.CYAN}kooshayeganeh.gitbook.io\n"
        f"{Fore.YELLOW}And a Little More :)")

# Command-line argument handling
try:
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ["-h", "--human"]:
            print(Fore.GREEN + Style.BRIGHT + "--- openSUSE JalaiDate ---")
            print(Fore.GREEN + Style.BRIGHT + f"{main_date}")
        elif arg in ["-d", "--digit"]:
            print(Fore.GREEN + Style.BRIGHT + "--- openSUSE JalaiDate ---")
            print(Fore.GREEN + Style.BRIGHT + f"\t{digit_date}")
        elif arg in ["-v", "--verbose"]:
            print(Fore.GREEN + Style.BRIGHT + "--- openSUSE JalaiDate ---")
            print(Fore.GREEN + Style.BRIGHT + f"{main_date}")
            print(Fore.GREEN + Style.BRIGHT + f"\t{digit_date}")
        elif arg in ["-i", "--info"]:
            print(Fore.GREEN + Style.BRIGHT + "--- openSUSE JalaiDate ---")
            print(info)
        elif arg in ["-t", "--time"]:
            current_time_24 = now.strftime("%H:%M:%S")
            current_time_12 = now.strftime("%I:%M:%S %p")
            print(Fore.GREEN + Style.BRIGHT + "--- openSUSE JalaiDate ---")
            print(Fore.GREEN + Style.BRIGHT + f"Current Time (24-hour): {current_time_24}")
            print(Fore.GREEN + Style.BRIGHT + f"Current Time (12-hour): {current_time_12}")
        elif arg in ["-w", "--weekday"]:
            print(Fore.GREEN + Style.BRIGHT + "--- openSUSE JalaiDate ---")
            print(Fore.GREEN + Style.BRIGHT + f"Today is: {weekday}")
        elif arg in ["-c", "--convert"]:
            if len(sys.argv) >= 5:
                g_year, g_month, g_day = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
                gregorian_date = datetime.date(g_year, g_month, g_day)
                jalali_date = JalaliDate.from_gregorian(gregorian_date)
                print(Fore.GREEN + Style.BRIGHT + "--- openSUSE JalaiDate ---")
                print(Fore.GREEN + Style.BRIGHT + f"Gregorian Date: {gregorian_date}")
                print(Fore.GREEN + Style.BRIGHT + f"Jalali Date: {jalali_date}")
            else:
                print(Fore.RED + "Error: Please provide a Gregorian date in the format: -c YYYY MM DD")
        elif arg in ["-m", "--message"]:
            if len(sys.argv) >= 3:
                custom_message = ' '.join(sys.argv[2:])
                print(Fore.GREEN + Style.BRIGHT + "--- openSUSE JalaiDate ---")
                print(Fore.GREEN + Style.BRIGHT + custom_message)
            else:
                print(Fore.RED + "Error: Please provide a custom message.")
        elif arg in ["-s", "--system"]:
            system_info = (f"{Fore.YELLOW}System: {platform.system()}\n"
                           f"{Fore.YELLOW}Node: {platform.node()}\n"
                           f"{Fore.YELLOW}Release: {platform.release()}\n"
                           f"{Fore.YELLOW}Version: {platform.version()}\n"
                           f"{Fore.YELLOW}Machine: {platform.machine()}\n"
                           f"{Fore.YELLOW}Python Version: {platform.python_version()}")
            print(Fore.GREEN + Style.BRIGHT + "--- openSUSE JalaiDate ---")
            print(system_info)
        elif arg in ["--help"]:
            print(Fore.GREEN + Style.BRIGHT + "--- openSUSE JalaiDate ---")
            print(Fore.YELLOW + "Usage: script.py [options]")
            print(Fore.YELLOW + "Options:")
            print(Fore.YELLOW + "\t-h, --human\tShow human-readable date")
            print(Fore.YELLOW + "\t-d, --digit\tShow date in digits")
            print(Fore.YELLOW + "\t-v, --verbose\tShow both human-readable and digit date")
            print(Fore.YELLOW + "\t-i, --info\tShow developer information")
            print(Fore.YELLOW + "\t-t, --time\tShow current time in 24-hour and 12-hour formats")
            print(Fore.YELLOW + "\t-w, --weekday\tShow current weekday")
            print(Fore.YELLOW + "\t-c, --convert YYYY MM DD\tConvert Gregorian date to Jalali")
            print(Fore.YELLOW + "\t-m, --message [message]\tDisplay a custom message")
            print(Fore.YELLOW + "\t-s, --system\tShow system information")
            print(Fore.YELLOW + "\t--help\t\tShow this help message")
        else:
            print(Fore.RED + "Error: Invalid argument. Use --help for usage information.")
    else:
        print(Fore.GREEN + Style.BRIGHT + "--- openSUSE JalaiDate ---")
        print(Fore.GREEN + Style.BRIGHT + f"{main_date}")
        print(Fore.GREEN + Style.BRIGHT + f"\t{digit_date}")

except Exception as e:
    print(Fore.RED + "Error:", str(e))
    print(Fore.RED + "Use --help for usage information.")
