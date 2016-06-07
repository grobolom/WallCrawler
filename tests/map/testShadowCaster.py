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
            list('.......'),
            list('......!'),
            list('.....!!'),
            list('...!!!!'),
            list('..!!!!!'),
            list('.!!!!!!'),
            list('@!!!!..'),
        ]
        sut = ShadowCaster()
        result = sut.castOctant(squares)

        for k, row in enumerate(result):
            print ''.join(result[k]) + ' ' + ''.join(expected[k])

        assert result == expected
