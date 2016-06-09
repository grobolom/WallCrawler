class Tile(object):
    def __init__(self):
        self.walkable = True
        self.blocking = False
        self.ascii_rep = ' '
        self.lit = None

    def __eq__(self, other):
        return not other == None and \
               self.__dict__ == other.__dict__

    def getAsciiRep(self):
        if self.lit:
            return self.ascii_rep
        return ' '

class Floor(Tile):
    def __init__(self):
        super(Floor, self).__init__()
        self.ascii_rep = '.'
        self.blocking = False

class Wall(Tile):
    def __init__(self):
        super(Wall, self).__init__()
        self.ascii_rep = '#'
        self.blocking = True
