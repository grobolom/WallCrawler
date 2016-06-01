import app

class MapKeyHandler:
    def getAction(self, key, state):
        if key not in [ 'h', 'j', 'k', 'l' ]:
            return None

        to = self._getTo(key, state['character'])

        return {
            'name': 'MOVE_CHARACTER',
            'to': to
        }

    def _getTo(self, key, character):
        (x, y) = (character.x, character.y)

        if key == 'h':
            return [x - 1, y]
        if key == 'l':
            return [x + 1, y]

        if key == 'j':
            return [x, y + 1]
        if key == 'k':
            return [x, y - 1]
