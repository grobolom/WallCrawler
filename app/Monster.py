from app import Object

class Monster(Object):
    def __init__(self, *args, **kwargs):
        super(Object, self).__init__()

        self.hp = 10
        self.ascii_rep = 'R'
        self.name = 'monster'
