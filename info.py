class Info:
    def __init__(self):
        cell = ""
        for i in range(26):
            if i == 0 or i == 25:
                cell = cell+"+"
            else:
                cell = cell+"-"
        for j in range(9):
            if j == 1:
                print("+ Endo System Info       +")
            elif j == 3:
                print("+ Url: localhost:8080    +")
            elif j == 5:
                print("+ Webpages: Bootstrap    +")
            elif j == 7:
                print("+ Desktop app: Electron  +")
            else:
                print(cell)
