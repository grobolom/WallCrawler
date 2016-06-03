class AttackReducer:
    def reduce(self, state, action):
        if action['name'] != 'ATTACK_CHARACTER':
            return state

        new_state = state

        id = action['target'].id
        objects = new_state['objects']
        source = action['source']

        objects, target = self.changeHealthById(objects, id, -1, source)

        if target.hp < 1:
            new_state['character'].xp += target.xp

        new_state['objects'] = objects

        return new_state

    def changeHealthById(self, objects, id, change, source):
        new_objects = objects
        target = None

        for o in new_objects:
            if o.id == id:
                target = o
                o = self.changeHealth(o, source, change)
                break

        return new_objects, target

    def changeHealth(self, target, source, change):
        t = target
        t.hp += change
        if t.hp < 1:
            t.dead = True
            t.killed_by = source
        return t
