import app
from app.Map import LightCaster

class TestShadowCaster:
    def test_it_should_return_what_squares_in_a_row_should_be_shadowed(self):
        sut = LightCaster()

        squares = ['.', '.', '.']
        sectors = [ [1.0, 1.0 / 2.0] ]

        result = sut.getShadowedSquares(squares, sectors)

        assert result == ['.', '.', 's']

    def test_it_should_return_the_right_squres_with_multiple_sectors(self):
        sut = LightCaster()

        squares = ['.', '.', '.', '.']
        sectors = [ [1.0, 2.2 / 3.0], [0.4 / 3.5, 0.0] ]

        result = sut.getShadowedSquares(squares, sectors)

        assert result == ['.', '.', 's', '.']

    def test_it_should_return_new_sectors_from_old_ones(self):
        sut = LightCaster()
        squares = [ '.', '.', '#', '.']
        sectors = [ [ 1.0, 0.0 ] ]

        result = sut.getNewSectors(squares, sectors)

        assert result == [ [1.0, 1.5 / 2.5], [0.5 / 3.5, 0.0] ]

    def test_it_should_get_all_stuff_right(self):
        sut = LightCaster()
        squares = [
            '.................',
            ' ......###.......',
            '  .....###.......',
            '   ....###..#..##',
            '    ...##........',
            '     ............',
            '      ...........',
            '       ..........',
            '        .........',
            '         ........',
            '          .......',
            '           ......',
            '            .....',
            '             ....',
            '              ...',
            '               ..',
            '                .',
        ]
        result = sut.getMask(squares)
        assert result == [
            '....ssssss.....ss',
            ' ....ssss#..s..ss',
            '  ...ssss#..s..ss',
            '   ...ss##..#..##',
            '    ...##........',
            '     ............',
            '      ...........',
            '       ..........',
            '        .........',
            '         ........',
            '          .......',
            '           ......',
            '            .....',
            '             ....',
            '              ...',
            '               ..',
            '                .',
        ]
