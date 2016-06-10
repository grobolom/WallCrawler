from blessed import Terminal

class Screen:
    def __init__(self, term = Terminal()):
        self.term = term

    def draw(self, position, stuff):
        with term.location(position[0], position[1]):
            for line in stuff:
                print(stuff)
