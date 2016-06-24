import app
from app import Monster
from app.utils import MapStuff

import random

class Rat(Monster):
    def getAction(self, state):
        map = state['map']
        square = self.findANearbySquare(map)
        if self.characterInSquare(square, state['character']):
            return {
                'name': 'ATTACK',
                'target': 'character',
                'source': self.id,
            }

        return {
            'name': 'MOVE',
            'target': self.id,
            'to': square,
        }

    def findANearbySquare(self, map):
        pos = self.position
        return MapStuff.findANearbySquare(position, map)

    def characterInSquare(self, square, character):
        return square == character.position
