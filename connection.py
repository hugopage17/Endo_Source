import requests
from colorama import Fore, Style
import json

class Connection:
    def __init__(self, api_link):
        try:
            self.json_source = requests.get(api_link)
            self.get_link()
        except requests.ConnectionError:
            self.connection_warning()

    def get_link(self):
        self.json_data = json.loads(self.json_source.text)
        self.is_loaded = True

    def connection_warning(self):
        print(Fore.YELLOW + "Warning you are offline, Endo requires an internet connection")
        print(Style.RESET_ALL)

    def retrieve_failed(self):
        print (Fore.RED + 'ERROR_01: Endo failed to retrieve data, please check your network and try again.')
        self.is_loaded = False
        print(Style.RESET_ALL)

    def show_details(self):
        try:
            for data in self.json_data:
                version_num = data["version"]
                print('Endo Version: '+version_num)
            print("Type 'create project - project name' to get started")
        except AttributeError:
            pass
