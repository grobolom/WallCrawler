import app
from app.Map import ValidTilePicker

class TestValidTilePicker:
    def test_it_should_pick_a_random_empty_floor_tile(self):
        sut = ValidTilePicker()

        map = {
            'tiles': [[ app.Wall(), app.Floor() ]],
            'size': [2, 1],
        }
        tile = sut.getRandomEmptyFloorTile(map)

        assert tile['pos'] == [1, 0]

