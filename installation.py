import time
from tqdm import tqdm
import os
import requests
from colorama import Fore, Style
import getpass
import sys
from pathlib import Path
import subprocess

class Installer:
    def __init__(self):
        pass
        self.success = False

    def run_installer(self, json_data, folder_name):
        current_user = getpass.getuser()
        directory = '/Users/'+current_user+'/Desktop/'+folder_name
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(Fore.BLUE + "Creating "+folder_name+" at /Users/"+current_user+'/Desktop')
                for i in tqdm(range(100)):
                    time.sleep(0.02)
                try:
                    for data in json_data:
                        r = requests.get(data["code"])
                        file_name = data["name"]
                        print(Fore.LIGHTCYAN_EX + 'Importing '+file_name)
                        with open(directory+'/'+file_name, 'wb') as f:
                            f.write(r.content)
                    logo_link = requests.get('https://i.imgur.com/lVCIaKv.png')
                    print(Fore.LIGHTCYAN_EX + 'Importing endo_logo.png')
                    with open(directory+'/endo_logo.png', 'wb') as img:
                        img.write(logo_link.content)
                except requests.ConnectionError:
                    print(Fore.RED + "ERROR_04: No internet connection, please check your connection and try again")
                    time.sleep(1)
                    sys.exit()
                os.chdir(directory)
                current_dir = os.getcwd()
                server_file = Path(current_dir+'/server.py')
                if server_file.is_file():
                    os.system('attrib +h server.py')
                print(Fore.GREEN + "INSTALLATION COMPLETE")
                self.success = True
            else:
                print (Fore.RED + 'ERROR_03: Directory already exists, please name your project something else')
                print(Style.RESET_ALL)
        except OSError:
            print (Fore.RED + 'ERROR_02: An OS error has occured, installation failed.')
            print(Style.RESET_ALL)

    def start_server(self):
        current_dir = os.getcwd()
        server_file = Path(current_dir+'/server.py')
        if server_file.is_file():
            try:
                subprocess.call('start /wait python server.py', shell=True)
            except:
                print(Fore.RED + "ERROR_11: server.py file could not start, please install python. For more information visit https://www.python.org/")
                print(Style.RESET_ALL)
        else:
            print(Fore.RED + "ERROR_06: Please create a project first before deploying the server")
            print(Style.RESET_ALL)

    def start_app(self):
        try:
            subprocess.check_call('npm install', shell=True)
            subprocess.check_call('npm start', shell=True)
        except:
            print(Fore.RED + "ERROR_07: Endo App failed to start, this may be because you have not installed NodeJS.\n For more info please visit https://nodejs.org/en/")
            print(Style.RESET_ALL)
