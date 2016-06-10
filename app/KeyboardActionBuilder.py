class KeyboardActionBuilder:
    # TODO: we can probably separate this into different classes that are
    # responsible for their own portions of the view. It's less clear that way
    # where the state transitions are but it keeps each state compartmentalized
    def getAction(self, key, view = 'main'):
        if view == 'main':
            return self.getMapAction(key)
        if view == 'menu':
            return self.getMenuAction(key)
        return { 'name': 'NONE' }

    def getMapAction(self, key):
        if key == 'k':
            return { 'name': 'MOVE_UP' }
        if key == 'j':
            return { 'name': 'MOVE_DOWN' }
        if key == 'h':
            return { 'name': 'MOVE_LEFT' }
        if key == 'l':
            return { 'name': 'MOVE_RIGHT' }
        if key == 'KEY_ESCAPE':
            return {
                'name': 'SWITCH_VIEW',
                'to': 'menu',
            }
        return { 'name': 'NO_MOVE' }

    def getMenuAction(self, key):
        if key == 'KEY_ESCAPE':
            return {
                'name': 'SWITCH_VIEW',
                'to': 'main',
            }
        return { 'name': 'NONE' }
