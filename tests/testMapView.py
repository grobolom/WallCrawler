from app import Tile
from app import MapView

class MockObject(object):
    def __init__(self):
        self.position = [1, 1]
        self.ascii_rep = '@'

class TestMapView:
    def test_it_should_draw_a_tile(self):
        map_view = MapView()

        tile = Tile()
        tile.ascii_rep = 'x'

        map = [[ tile ]]
        positions = [[(0, 0)]]

        expected = [['x']]
        assert expected == map_view.draw(map, positions, [])

    def test_it_should_draw_several_tiles(self):
        map_view = MapView()

        tile = Tile()
        tile.ascii_rep = 'y'

        map = [[ tile, tile, tile ]]
        positions = [[(0, 0), (1, 0)]]

        expected = [['y', 'y']]
        assert expected == map_view.draw(map, positions, [])

    def test_it_should_draw_objects_on_top_of_tiles(self):
        obj = MockObject()
        objects = [ obj ]

        map_view = MapView()

        tile = Tile(ascii_rep = '.', lit = True)
        map = [[ tile, tile ],[ tile, tile ]]
        positions = [[(0, 0), (1, 0)],[(0, 1), (1, 1)]]

        expected = [['.', '.'],['.', '@']]

        assert expected == map_view.draw(map, positions, objects)

    def test_it_should_not_draw_objects_off_the_screen(self):
        obj1 = MockObject()
        obj1.position = [0, 1]

        obj2 = MockObject()
        obj2.position = [2, 2]

        objects = [ obj1, obj2 ]

        map_view = MapView()

        tile = Tile(ascii_rep = '.', lit = True)
        map = [[ tile, tile, tile ],[ tile, tile, tile ],[ tile, tile, tile ]]
        positions = [[(0, 0), (1, 0)],[(1, 0), (1, 1)]]

        expected = [['.', '.'],['@', '.']]

        assert expected == map_view.draw(map, positions, objects)
