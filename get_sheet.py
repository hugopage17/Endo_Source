import gspread
from oauth2client.service_account import ServiceAccountCredentials
from colorama import Fore, Style

class GetSheet:
    def __init__(self):
        self.connection_made = False
        try:
            scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
            creds = ServiceAccountCredentials.from_json_keyfile_name('EndoWebAPI-56b939fe54b0.json', scope)
            client = gspread.authorize(creds)
            sheet = client.open('endo_web_sheet').sheet1
            web_link = sheet.col_values(3)
            app_link = sheet.col_values(4)
            details_link = sheet.col_values(5)
            self.web_link = web_link[0]
            self.app_link = app_link[0]
            self.details_link = details_link[0]
            self.connection_made = True
        except:
            self.connection_made = False

    def show_warning(self):
        print(Fore.YELLOW + "Warning you are offline, Endo requires an internet connection")
        print(Style.RESET_ALL)
