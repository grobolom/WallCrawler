from app.keyboard import MoveAndAttackHandler

class KeyboardActionBuilder:
    def __init__(self, moveAndAttackHandler = None):
        if not moveAndAttackHandler:
            moveAndAttackHandler = MoveAndAttackHandler()
        self.mah = moveAndAttackHandler

    # TODO: we can probably separate this into different classes that are
    # responsible for their own portions of the view. It's less clear that way
    # where the state transitions are but it keeps each state compartmentalized
    def getAction(self, key, state):

        view = 'main'
        if 'view' in state:
            view = state['view']

        if view == 'main':
            return self.getMapAction(key, state)
        if view == 'menu':
            return self.getMenuAction(key)

        return { 'name': 'NONE' }

    def getMapAction(self, key, state):
        if key == 'KEY_ESCAPE':
            return {
                'name': 'SWITCH_VIEW',
                'to': 'menu',
            }
        if key == '':
            return { 'name': 'NO_MOVE' }
        return self.mah.getAction(key, state)

    def getMenuAction(self, key):
        if key == 'KEY_ESCAPE':
            return {
                'name': 'SWITCH_VIEW',
                'to': 'main',
            }
        return { 'name': 'NONE' }
