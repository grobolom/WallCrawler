from app import Tile
from app import MapView

class MockObject(object):
    def __init__(self):
        self.x = 1
        self.y = 1
        self.ascii_rep = '@'

class TestMapView:
    def test_it_should_draw_a_tile(self):
        map_view = MapView()

        tile = Tile()
        tile.ascii_rep = 'x'

        map = [[ tile ]]
        positions = [[(0, 0)]]

        expected = [['x']]
        assert expected == map_view.draw(map, positions)

    def test_it_should_draw_several_tiles(self):
        map_view = MapView()

        tile = Tile()
        tile.ascii_rep = 'y'

        map = [[ tile, tile, tile ]]
        positions = [[(0, 0), (0, 1)]]

        expected = [['y', 'y']]
        assert expected == map_view.draw(map, positions)

    def test_it_should_draw_objects_on_top_of_tiles(self):
        obj = MockObject()
        objects = [ obj ]

        map_view = MapView()

        tile = Tile()
        tile.ascii_rep = '.'
        map = [[ tile, tile ],[ tile, tile ]]
        positions = [[(1, 1)]]

        expected = [['@']]

        assert expected == map_view.draw(map, positions, objects)
