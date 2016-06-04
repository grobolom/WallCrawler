class MonsterMover:
    def reduce(self, state, action):
        new_state = state

        if action['name'] != 'MOVE':
            return new_state

        id = action['target']
        to = action['to']

        new_objects = state['objects']
        for key, o in enumerate(new_objects):
            if o.id == id:
                new_objects[key].position = to
                break
        state['objects'] = new_objects

        return new_state
