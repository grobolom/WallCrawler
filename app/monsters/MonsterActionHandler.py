class MonsterActionHandler:
    def getMonsterActions(self, state):
        objects = [ o for o in state['objects'] if o.type == 'monster' ]
        return [
            o.getAction(state) for o in objects
        ]
