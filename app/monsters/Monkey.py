from app import Monster

class Monkey(Monster):
    def __init__(self, *args, **kwargs):
        super(Monster, self).__init__()

        self.hp = 20
        self.xp = 5
        self.ascii_rep = 'M'
        self.name = 'monkey'
        self.type = 'monkey'
        self.damage = 3

        for dictionary in args:
            for key in dictionary:
                setattr(self, key, dictionary[key])

        for key in kwargs:
            setattr(self, key, kwargs[key])
