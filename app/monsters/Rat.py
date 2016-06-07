import app
from app import Monster
import random

class Rat(Monster):
    def getAction(self, state):
        map = state['map']
        square = self.findANearbySquare(map)
        return {
            'name': 'MOVE',
            'target': self,
            'to': square,
        }

    def findANearbySquare(self, map):
        pos_x, pos_y = self.position
        map_x, map_y = map['size']

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        random.shuffle(directions)

        for d in directions:
            x = pos_x + d[0]
            y = pos_y + d[1]

            if x < 0 or y < 0 or x >= map_x or y >= map_y:
                continue

            if type(map['tiles'][y][x]) == app.Floor:
                return [x, y]
