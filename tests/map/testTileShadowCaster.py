from app.map import TileShadowCaster
from app.map import MapToTileConverter

class TestTileShadowCaster:
    def test_it_should_color_from_any_square_correctly(self):
        squares = [
            list('...#.#...'),
            list('.........'),
            list('...#.#...'),
            list('.........'),
            list('...#@#...'),
            list('.........'),
            list('...#.#...'),
            list('.........'),
            list('...#.#...'),
        ]
        expected = [
            list('.  #.#  .'),
            list(' . ... . '),
            list('  .#.#.  '),
            list('   ...   '),
            list('   #@#   '),
            list('   ...   '),
            list('  .#.#.  '),
            list(' . ... . '),
            list('.  #.#  .'),
        ]
        tiles = MapToTileConverter().convertToTiles(squares)

        res = TileShadowCaster().shade(tiles, [4, 4])
        result = MapToTileConverter().convertToSquares(res)

        assert result == expected
