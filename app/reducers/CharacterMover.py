import app

class CharacterMover:
    """
    this is a reducer that handles moving the character. While later we will
    probably want to allow any object to fire move events, we can refactor as
    necessary. It's also more complex - we need to treat all objects as
    movable and need to be able to pick them out of the list of objects
    easily. Maybe it's easier to use something other than a plain list but
    we will tackle it when we get there.
    """
    def reduce(self, state, action):
        if action['name'] != 'MOVE_CHARACTER':
            return state

        character = state['character']
        map       = state['map']['tiles']
        to        = action['to']

        if self._targetTileIsWalkable(to, map):
            (character.x, character.y) = to

        new_state = state
        new_state['character'] = character

        return new_state

    def _targetTileIsWalkable(self, to, map):
        x = to[0]
        y = to[1]

        return type(map[y][x]) == app.Floor
