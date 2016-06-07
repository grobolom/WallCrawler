from app.map import ShadowCaster

class TestShadowCaster:
    def test_it_should_color_from_any_square_correctly(self):
        squares = [
            list('.........'),
            list('.........'),
            list('.........'),
            list('.........'),
            list('....@....'),
            list('.........'),
            list('.........'),
            list('.........'),
            list('.........'),
        ]
        expected = [
            list('.ss#..sss'),
            list('s.s..#sss'),
            list('ss.#..sss'),
            list('sss..#.#.'),
            list('sss#@....'),
            list('sss..#.#.'),
            list('ss.#..sss'),
            list('s.s..#sss'),
            list('.ss#..sss'),
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
            list('sssssss'),
            list('ssssss.'),
            list('sssss..'),
            list('sss#...'),
            list('ss...#.'),
            list('s......'),
            list('@...#ss'),
        ]
        sut = ShadowCaster()
        result = sut.castOctant(squares, 1)

        assert result == expected

    def test_it_should_color_any_octant(self):
        squares = [
            list('@#.....'),
            list('.......'),
            list('.#.....'),
            list('.......'),
            list('.#.....'),
            list('.......'),
            list('.#.....'),
        ]
        expected = [
            list('@#sssss'),
            list('..sssss'),
            list('.#.ssss'),
            list('..s.sss'),
            list('.#ss.ss'),
            list('..sss.s'),
            list('.#ssss.'),
        ]
        sut = ShadowCaster()
        result = sut.castOctant(squares, 3)

        for key, row in enumerate(result):
            print(''.join(result[key]) + ' ' + ''.join(expected[key]))

        # assert result == expected
