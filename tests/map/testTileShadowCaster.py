from app.map import TileShadowCaster
from app.map import MapToTileConverter

class TestTileShadowCaster:
    def test_it_should_color_from_any_square_correctly(self):
        squares = [
            list('...#.#...'),
            list('.........'),
            list('...#.#...'),
            list('.........'),
            list('...#.#...'),
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
            list('   #.#   '),
            list('   ...   '),
            list('  .#.#.  '),
            list(' . ... . '),
            list('.  #.#  .'),
        ]
        tiles = MapToTileConverter().convertToTiles(squares)

        res = TileShadowCaster().shade(tiles, [4, 4])
        result = MapToTileConverter().convertToSquares(res)

        assert result == expected

    def test_it_should_color_an_octant(self):
        squares = MapToTileConverter().convertToTiles([
            list('.......'),
            list('.......'),
            list('.......'),
            list('...#...'),
            list('.....#.'),
            list('.......'),
            list('....#..'),
        ])
        expected = [
            list('...... '),
            list('..... .'),
            list('.... ..'),
            list('...#...'),
            list('.....#.'),
            list('.......'),
            list('....#  '),
        ]
        sut = TileShadowCaster()
        result = MapToTileConverter().convertToSquares(
            sut.shade(squares, [0, 6]))

        assert result == expected

    def test_it_should_handle_non_square_areas(self):
        squares = MapToTileConverter().convertToTiles([
            list('..........'),
            list('..........'),
            list('..........'),
            list('...#......'),
            list('.....#....'),
            list('..........'),
            list('....#.....'),
        ])
        expected = [
            list('......  ..'),
            list('..... ....'),
            list('.... .... '),
            list('...#...  .'),
            list('.....#....'),
            list('..........'),
            list('....#     '),
        ]
        sut = TileShadowCaster()
        res = sut.shade(squares, [0, 6])
        result = MapToTileConverter().convertToSquares(res)

        for key, row in enumerate(result):
            print(''.join(result[key]) + ' ' + ''.join(expected[key]))

        assert result == expected
