class Screen:
    width = 80
    height = 20
    def printScreen(self, data):
        for i in range(1, 20):
            print '' for i in range(1, self.width)

s = Screen();
s.printScreen('something');
