import app
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

    def test_it_should_light_up_a_simple_scene(self):
        tiles = [
            [ app.Floor(), app.Wall(), app.Floor() ]
        ]

        sut = TileShadowCaster()
        result = sut.shade(tiles, [0, 0])

        assert result[0][0].lit == True
        assert result[0][1].lit == True
        assert result[0][2].lit == False
