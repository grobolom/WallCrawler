import random
import app

class ValidTilePicker:
    def getRandomEmptyFloorTile(self, map):
        tiles    = map['tiles']
        map_size = map['size']

        found = False
        while not found:
            x = random.randint(0, map_size[0] - 1)
            y = random.randint(0, map_size[1] - 1)

            if type(tiles[y][x]) == app.Floor:
                found = True
                return {
                    'pos': [x, y],
                    'tile': tiles[y][x],
                }
