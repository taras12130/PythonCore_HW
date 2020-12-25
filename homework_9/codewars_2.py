# Color Ghost

from random import randint
class Ghost(object):
    def __init__(self):
        colors = ['white', 'yellow', 'purple', 'red']
        self.color = colors[randint(0, 3)]