from app.map import ShadowCaster

class TestShadowCaster:
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
        result = ShadowCaster().shade(squares, [4, 4])

        for key, row in enumerate(result):
            print(''.join(result[key]) + ' ' + ''.join(expected[key]))

        assert result == expected

    def test_it_should_color_an_octant(self):
        squares = [
            list('.......'),
            list('.......'),
            list('.......'),
            list('...#...'),
            list('.....#.'),
            list('.......'),
            list('@...#..'),
        ]
        expected = [
            list('...... '),
            list('..... .'),
            list('.... ..'),
            list('...#...'),
            list('.....#.'),
            list('.......'),
            list('@...#  '),
        ]
        sut = ShadowCaster()
        result = sut.shade(squares, [0, 6])

        for key, row in enumerate(result):
            print(''.join(result[key]) + ' ' + ''.join(expected[key]))

        assert result == expected

    def test_it_should_handle_non_square_areas(self):
        squares = [
            list('..........'),
            list('..........'),
            list('..........'),
            list('...#......'),
            list('.....#....'),
            list('..........'),
            list('@...#.....'),
        ]
        expected = [
            list('......  ..'),
            list('..... ....'),
            list('.... .... '),
            list('...#...  .'),
            list('.....#....'),
            list('..........'),
            list('@...#     '),
        ]
        sut = ShadowCaster()
        result = sut.shade(squares, [0, 6])

        for key, row in enumerate(result):
            print(''.join(result[key]) + ' ' + ''.join(expected[key]))

        assert result == expected
