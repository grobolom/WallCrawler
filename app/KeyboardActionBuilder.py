class KeyboardActionBuilder:
    def getAction(self, key):
        if key == 'k':
            return { 'name': 'MOVE_UP' }
        if key == 'j':
            return { 'name': 'MOVE_DOWN' }
        if key == 'h':
            return { 'name': 'MOVE_LEFT' }
        if key == 'l':
            return { 'name': 'MOVE_RIGHT' }
        return { 'name': 'NO_MOVE' }
