class AttackReducer:
    def reduce(self, state, action):
        if action['name'] != 'ATTACK_CHARACTER':
            return state

        new_state = state

        target_id = action['target'].id
        objects = new_state['objects']

        objects, target = self.changeHealthById(objects, target_id, -1)

        if target.hp < 1:
            new_state['character'].xp += target.xp

        new_state['objects'] = objects

        return new_state

    def changeHealthById(self, objects, id, change):
        new_objects = objects
        target = None

        for o in new_objects:
            if o.id == id:
                target = o
                o.hp += change
                break

        return new_objects, target
