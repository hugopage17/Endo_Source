import base64
from github import *
import os
from pathlib import Path
from colorama import Fore, Style
import requests
import os

class Upload:
    def __init__(self):
        self.creds_array = []
        self.repository_name = ""
        self.repo_exists = False

    def start_upload(self):
        creds_file = Path('creds.txt')
        if not creds_file.is_file():
            creds = open("creds.txt", "w")
            cred_details = input("Enter your github username followed by ' - ' then your password: ")
            cred_details = cred_details.split(" - ")
            creds.write(cred_details[0]+'\n'+cred_details[1])
            self.creds_array.append(cred_details[0])
            self.creds_array.append(cred_details[1])
            os.system('attrib +h creds.txt')
        else:
            self.creds_array = []
            with open("creds.txt", "r") as creds:
                for line in creds:
                    self.creds_array.append(line)
                self.creds_array[0] = self.creds_array[0].replace("\n", "")
        try:
            g = Github(self.creds_array[0], self.creds_array[1])
            for existing_repos in g.get_user().get_repos():
                if self.repository_name == existing_repos.name:
                    self.repo_exists = True
                else:
                    pass
            if self.repo_exists == True:
                print(Fore.YELLOW + "Connecting to repository: "+self.repository_name)
                existing_repo = g.get_user().get_repo(self.repository_name)
                existing_repo.delete()
            elif self.repo_exists == False:
                print(Fore.YELLOW + "Creating new repository: "+self.repository_name)
            new_repo = g.get_user().create_repo(self.repository_name)
            repo = g.get_user().get_repo(self.repository_name)
            dir_files = os.listdir()
            for file in dir_files:
                try:
                    f = open(file, 'rb')
                    data = f.read()
                    if not f.name == 'creds.txt':
                        repo.create_file(f.name, "init commit", data, branch="master")
                    else:
                        pass
                except:
                    print(Fore.RED + "ERROR_13: "+str(f.name)+' failed to uploaded')
                    print(Style.RESET_ALL)
            print(Fore.GREEN + self.repository_name+" successfully created")
            print(Style.RESET_ALL)
            print("View your repository at: https://github.com/"+str(self.creds_array[0])+"/"+str(self.repository_name))
        except:
            print(Fore.RED + "ERROR_12: Failed to connect to Github. This may have occured due to incorrect credentials or no internet connection")
            print(Style.RESET_ALL)
