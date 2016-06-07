from app.map import ShadowCaster

class TestShadowCaster:
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

        for k, row in enumerate(result):
            print ''.join(result[k]) + ' ' + ''.join(expected[k])

        assert result == expected
