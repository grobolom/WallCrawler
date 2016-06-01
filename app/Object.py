class Object(object):
    def __init__(self, *args, **kwargs):
        self.x = 0
        self.y = 0
        self.ascii_rep = '@'
        self.type = 'Object'

        for dictionary in args:
            for key in dictionary:
                setattr(self, key, dictionary[key])

        for key in kwargs:
            setattr(self, key, kwargs[key])
