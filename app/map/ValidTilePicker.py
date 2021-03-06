import random
import app

class ValidTilePicker:
    def getRandomEmptyFloorTile(self, map):
        tiles    = map['tiles']
        map_size = map['size']
        objects  = map['objects']

        found = False
        while not found:
            x = random.randint(0, map_size[0] - 1)
            y = random.randint(0, map_size[1] - 1)
            pos = [x, y]

            if self.isPlaceableTile(map, pos):
                return {
                    'pos': pos,
                    'tile': tiles[y][x],
                }
        # TODO: fix if every tile is taken

    def tileDoesNotHaveAnObjectOnIt(self, pos, objects):
        for obj in objects:
            if obj.position == pos:
                return False
        return True

    def isPlaceableTile(self, map, pos):
        x = pos[0]
        y = pos[1]
        tiles = map['tiles']
        objects = map['objects']

        return type(tiles[y][x]) == app.Floor and \
               self.tileDoesNotHaveAnObjectOnIt(pos, objects)
