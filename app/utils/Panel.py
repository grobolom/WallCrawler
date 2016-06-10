class Panel:
    def draw(self, width, height, lines):
        result = []
        for line in lines[:height]:
            if line:
                result += [ line.ljust(width, ' ')[:width] ]
            else:
                result += [ ' ' * width ]
        return result
