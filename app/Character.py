from app import Object

class Character(Object):
    def __init__(self, *args, **kwargs):
        self.x = 0
        self.y = 0
        self.ascii_rep = 'v'
        self.type = 'char'
        self.hp = 10
        self.xp = 0
        self.dead = False

        for dictionary in args:
            for key in dictionary:
                setattr(self, key, dictionary[key])

        for key in kwargs:
            setattr(self, key, kwargs[key])

    def isDead(self):
        return self.dead
