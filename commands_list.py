from colorama import Fore, Style

class Commands:
    def __init__(self):
        print(Fore.YELLOW + "ENDO COMMAND LIST")
        print(Fore.CYAN + "")
        print("create project - project name: 'creates a new web project and starts the installer'")
        print("create app - app name: 'creates a new desktop project and starts the installer'")
        print("info: 'displays all technical info about the software'")
        print("start: 'after installation, this command starts the server and deploys the web project'")
        print("run: 'after installation, this command builds the project and deploys the desktop app'")
        print("open: 'prompts you to enter the diretory of your project then opens the project'")
        print("quit: 'Exits the program'")
        print(Style.RESET_ALL)
