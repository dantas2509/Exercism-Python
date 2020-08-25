class Robot:
    def __init__(self):
        from random import randint, seed
        self.name = f'{chr(randint(ord("A"), ord("Z")))}{chr(randint(ord("A"), ord("Z")))}{randint(0,999):0>3}'
    def reset(self):
        self.__init__

        '''import string
        from random import choice
        self.name = ''
        for i in range(2):
            self.name += choice(string.ascii_uppercase)
        for i in range(3):
            self.name += choice(string.digits)'''
