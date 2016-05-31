class Tile(object):
    def __init__(self):
        self.walkable = True
        self.blocks_los = False
        self.ascii_rep = ' '

class Floor(Tile):
    def __init__(self):
        super(Floor, self).__init__()
        self.ascii_rep = '.'

class Wall(Tile):
    def __init__(self):
        super(Wall, self).__init__()
        self.ascii_rep = '#'
