class Panel:
    def draw(self, width, height, lines):
        return [ line.ljust(width, ' ')[:width] for line in lines[:height] ]
