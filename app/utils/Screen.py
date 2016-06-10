from blessed import Terminal

class Screen:
    def __init__(self, term = Terminal()):
        self.term = term

    def draw(self, x, y, stuff):
        with self.term.location(x, y):
            for line in stuff:
                print(line)
