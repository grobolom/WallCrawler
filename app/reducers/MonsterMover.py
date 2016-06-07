class MonsterMover:
    def reduce(self, state, action):
        new_state = state

        if action['name'] != 'MOVE':
            return new_state

        id = action['target']
        to = action['to']

        if not self.toSquareIsFree(to, new_state):
            return new_state

        new_objects = state['objects']
        for key, o in enumerate(new_objects):
            if o.id == id:
                new_objects[key].position = to
                break
        state['objects'] = new_objects

        return new_state

    def toSquareIsFree(self, square, state):
        objects = state['objects']

        for o in objects:
            if o.position == square:
                return False

        return True
