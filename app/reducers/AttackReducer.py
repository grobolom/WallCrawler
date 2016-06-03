class AttackReducer:
    def reduce(self, action, state):
        if action['name'] != 'ATTACK_CHARACTER':
            return state

        new_state = state

        target_id = action['target'].id
        objects = new_state['objects']

        objects = self.changeHealthById(objects, target_id, -1)

        new_state['objects'] = objects

        return new_state

    def changeHealthById(self, objects, id, change):
        new_objects = objects
        for o in new_objects:
            if o.id == id:
                o.hp += change
                break;
        return new_objects
