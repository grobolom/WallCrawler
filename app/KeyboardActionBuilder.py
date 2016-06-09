class KeyboardActionBuilder:

    def getAction(self, key, view = 'main'):
        if view == 'main':
            return self.getMapAction(key)
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
        if key == 'KEY_ESC':
            return {
                'name': 'SWITCH_VIEW',
                'to': 'menu',
            }
        return { 'name': 'NO_MOVE' }
