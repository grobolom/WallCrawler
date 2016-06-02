import random

from . import RoomMaker

class RandomRoomMaker:
    def getRandomRoom(self, min_size, max_size):
        return [
            random.randint(min_size, max_size),
            random.randint(min_size, max_size),
        ]

    def getPossibleRoomSizes(self, min_size, max_size):
        return range(min_size, max_size) + \
               range(-min_size, -max_size, -1)
