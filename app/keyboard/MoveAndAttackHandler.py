class MoveAndAttackHandler:
    def getAction(self, key, state):
        objects = state['map']['objects']
        character = state['character']

        if key == 'KEY_RIGHT':
            square = self.getSquare(character, 1, 0)
        elif key == 'KEY_LEFT':
            square = self.getSquare(character, -1, 0)
        elif key == 'KEY_UP':
            square = self.getSquare(character, 0, -1)
        elif key == 'KEY_DOWN':
            square = self.getSquare(character, 0, 1)

        monster = self.getMonster(square, objects)
        if monster is not None:
            return {
                'name': 'ATTACK_CHARACTER',
                'source': character,
                'target': monster,
            }

        return {
            'name': 'MOVE_CHARACTER',
            'to': square,
        }

    def getSquare(self, character, x, y):
        pos = character.position
        return [ pos[0] + x, pos[0] + y ]

    def getMonster(self, square, objects):
        for o in objects:
            if o.type == 'monster' and o.position == square:
                return o
        return None
