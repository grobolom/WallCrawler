import app

class MapKeyHandler:
    def getAction(self, key, state):
        if key not in [ 'h', 'j', 'k', 'l' ]:
            return None

        to = self._getTo(key, state['character']['position'])

        return {
            'name': 'MOVE_CHARACTER',
            'to': to
        }

    def _getTo(self, key, current_position):
        (x, y) = current_position

        if key == 'h':
            return [x - 1, y]
        if key == 'l':
            return [x + 1, y]

        if key == 'j':
            return [x, y + 1]
        if key == 'k':
            return [x, y - 1]

        return current_position
