from connection import Connection

class Intro(Connection):
    def __init__(self, link):
        print("""
||||||||  ||||      ||  ||||||||       ||||||||
||        || ||     ||  ||      ||   ||        ||
||||||||  ||  ||    ||  ||       ||  ||        ||
||        ||    ||  ||  ||      ||   ||        ||
||||||||  ||      ||||  ||||||||       ||||||||
""")
        Connection.__init__(self, link)
