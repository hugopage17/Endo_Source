import requests
from colorama import Fore, Style

class CreateFile:
    def __init__(self, file_name):
        file_break = file_name.split(".")
        file_extension = file_break[1]
        if file_extension == 'html':
            print("creating new html: "+file_name)
            try:
                r = requests.get('https://rawcdn.githack.com/hugopage17/endo_files/53fa7980ca842a5c0972a39adcf1d144a96f7d68/html_template.html')
                with open(file_name, 'wb') as f:
                    f.write(r.content)
                    print(Fore.GREEN + file_name+' successfully created')
                    print(Style.RESET_ALL)
            except requests.ConnectionError:
                warning = input(Fore.YELLOW + "Warning you are offline, cannot import Endo html bootstrap, do you still wish to continue (y/n): ")
                if warning == 'y':
                    with open(file_name, 'w') as f:
                        f.write("<!--Insert HTML Code-->")
                    print(Fore.GREEN + file_name+' successfully created')
                    print(Style.RESET_ALL)
                else:
                    pass
        elif file_extension == 'css':
            print("creating new css: "+file_name)
            with open(file_name, 'w') as f:
                f.write("/*Insert CSS Code*/")
            print(Fore.GREEN + file_name+' successfully created')
            print(Style.RESET_ALL)
        elif file_extension == 'js':
            print("creating new css: "+file_name)
            with open(file_name, 'w') as f:
                f.write("//Insert Javascript Code")
            print(Fore.GREEN + file_name+' successfully created')
            print(Style.RESET_ALL)
