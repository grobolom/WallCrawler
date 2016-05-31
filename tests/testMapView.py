from app import Tile
from app import MapView

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
