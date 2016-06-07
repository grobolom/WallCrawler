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
            list('....#..'),
        ]
        expected = [
            list('......s'),
            list('.....s.'),
            list('....s..'),
            list('...#...'),
            list('.....#.'),
            list('.......'),
            list('....#ss'),
        ]
        sut = ShadowCaster()
        result = sut.castOctant(squares)

        for row in result:
            print ''.join(row)

        assert result == expected
