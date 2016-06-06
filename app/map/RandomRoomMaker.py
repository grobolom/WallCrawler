import random

from . import RoomMaker

class RandomRoomMaker:
    def getRandomRoom(self, min_size, max_size):
        r = self.getPossibleRoomSizes(min_size, max_size)

        return [
            random.choice(r),
            random.choice(r),
        ]

    def getPossibleRoomSizes(self, min_size, max_size):
        return range(min_size, max_size + 1) + \
               range(-min_size, -max_size - 1, -1)
