import os
from pathlib import Path
import subprocess
from colorama import Fore, Style

class OpenFile:
    def __init__(self):
        your_dir = input('Project Directory: ')
        your_dir = your_dir.replace('"', "")
        os.chdir(your_dir)
        server_file = Path('server.py')
        mainJS = Path('main.js')
        if server_file.is_file():
            try:
                os.system('cls')
                os.system('server.py')
            except:
                print(Fore.RED + "ERROR_08: server.py file not found, please chck you have the correct directory")
                print(Style.RESET_ALL)
        elif mainJS.is_file():
            try:
                os.system('cls')
                subprocess.check_call('npm start', shell=True)
            except:
                print(Fore.RED + "ERROR_07: Endo App failed to start, this may be because you have not installed NodeJS.\n For more info please visit https://nodejs.org/en/")
                print(Style.RESET_ALL)
        else:
            print(Fore.RED + "ERROR_09: Endo failed to start up your project, please check you have the correct directory and try again")
            print(Style.RESET_ALL)
