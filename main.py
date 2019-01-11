from intro import Intro
from installation import Installer
from colorama import Fore, Style
from info import Info
from commands_list import Commands
from get_data import GetData
import os
import sys
from time import sleep
from open_file import OpenFile
import webbrowser

print("""
||||||||  ||||      ||  ||||||||       ||||||||
||        || ||     ||  ||      ||   ||        ||
||||||||  ||  ||    ||  ||       ||  ||        ||
||        ||    ||  ||  ||      ||   ||        ||
||||||||  ||      ||||  ||||||||       ||||||||
""")


intro = Intro('https://api.jsonbin.io/b/5c26fbae412d482eae5706fc')
intro.show_details()
web_data = 'https://api.jsonbin.io/b/5c26bd046265442e46fe1f1c/3'
app_data = 'https://api.jsonbin.io/b/5c2ea1c57b31f426f8508620/5'
installer = Installer()


def endo():
    command = input()
    command = command.lower()
    if (command[:14]) == 'create project':
        website_name = command[17:]
        data = GetData(web_data)
        if hasattr(data, 'is_loaded') and data.is_loaded == True:
            installer.run_installer(data.json_data, website_name)
            print(Fore.YELLOW + "Type 'start' to deploy the server")
            print(Style.RESET_ALL)
        else:
            data.retrieve_failed()
    elif (command[:10]) == 'create app':
        app_name = command[13:]
        data = GetData(app_data)
        if hasattr(data, 'is_loaded') and data.is_loaded == True:
            installer.run_installer(data.json_data, app_name)
            print(Fore.YELLOW + "Type 'run' to start up the app")
            print(Style.RESET_ALL)
        else:
            data.retrieve_failed()
    elif command == 'info':
        info = Info()
    elif command == 'commands':
        command = Commands()
    elif command == 'start':
        installer.start_server()
    elif command == 'run':
        installer.start_app()
    elif (command[:4]) == 'open':
        folder = command[8:]
        try:
            open = OpenFile(folder)
        except:
            print(Fore.RED + "ERROR_10: Invalid directory be sure to type 'open - directory name' and please try again")
            print(Style.RESET_ALL)
    elif command == 'quit':
        print("Endo is shutting down...")
        sleep(1)
        sys.exit()
    elif command == 'endo':
        webbrowser.open('https://hugopage17.github.io/endo/')
    else:
        print(Fore.RED + "ERROR_05: "+command+" is not a valid command, type 'commands' to get a list of all valid commands")
        print(Style.RESET_ALL)

while True:
    endo()
