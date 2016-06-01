import random

from . import RoomMaker

class RandomRoomMaker:
    def getRandomRoom(self, min_size, max_size):
        return [
            random.randint(min_size, max_size),
            random.randint(min_size, max_size),
        ]

