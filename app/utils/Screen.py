from blessed import Terminal

class Screen:
    def __init__(self, term = Terminal()):
        self.term = term

    def draw(self, x, y, stuff):
        i = 0
        for line in stuff:
            with self.term.location(x, y + i):
                print(line)
            i += 1
