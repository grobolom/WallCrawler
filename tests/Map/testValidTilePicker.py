import app
from app.Map import ValidTilePicker

class TestValidTilePicker:
    def test_it_should_pick_a_random_floor_tile(self):
        sut = ValidTilePicker()

        map = {
            'tiles': [[ app.Wall(), app.Floor() ]],
            'size': [2, 1],
            'objects': [],
        }
        tile = sut.getRandomEmptyFloorTile(map)

        assert tile['pos'] == [1, 0]

    def test_it_should_not_pick_a_tile_with_an_object_on_it(self):
        sut = ValidTilePicker()

        map = {
            'tiles': [[ app.Floor(), app.Floor() ]],
            'size': [2, 1],
            'objects': [ app.Object(position = [0,0]) ]
        }
        tile = sut.getRandomEmptyFloorTile(map)

        assert tile['pos'] == [1, 0]

    def test_it_should_only_pick_floor_tiles(self):
        sut = ValidTilePicker()

        map = {
            'tiles': [[ app.Floor(), app.Wall() ]],
            'size': [2, 1],
            'objects': []
        }

        assert sut.isPlaceableTile(map, [0, 0]) == True
        assert sut.isPlaceableTile(map, [1, 0]) == False

    def test_it_should_only_pick_empty_tiles(self):
        sut = ValidTilePicker()

        map = {
            'tiles': [[ app.Floor(), app.Floor() ]],
            'size': [2, 1],
            'objects': [ app.Object(position = [0,0]) ]
        }

        assert sut.isPlaceableTile(map, [0, 0]) == False
        assert sut.isPlaceableTile(map, [1, 0]) == True

