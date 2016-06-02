from app import Object

class Monster(Object):
    def __init__(self, *args, **kwargs):
        super(Object, self).__init__()

        self.hp = 10
        self.ascii_rep = 'R'
        self.name = 'monster'
        self.type = 'monster'

        for dictionary in args:
            for key in dictionary:
                setattr(self, key, dictionary[key])

        for key in kwargs:
            setattr(self, key, kwargs[key])
