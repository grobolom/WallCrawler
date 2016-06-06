import app
from app.Map import LightCaster

class TestShadowCaster:
    def test_it_should_correctly_split_existing_sectors(self):
        sut = LightCaster()
        squares = list('....###..#..##')
        sectors = [ [1.0, 9.5 / 11.5], [7.5 / 12.5, 0.0] ]
        result = sut.getNewSectors(squares, sectors)

        expected = [
            [1.0,        9.5 / 11.5],
            [6.5 / 13.5, 4.5 / 12.5],
            [3.5 / 13.5, 1.5 / 12.5],
        ]

        print('result:')
        for k in result:
            print(k)

        print('\nexpected:')
        for k in expected:
            print(k)

        assert result == expected

    def test_it_should_return_what_squares_in_a_row_should_be_shadowed(self):
        sut = LightCaster()

        squares = ['.', '.', '.']
        sectors = [ [1.0, 1.0 / 2.0] ]

        result = sut.getShadowedSquares(squares, sectors)

        assert result == ['.', '.', 's']

    def test_it_should_return_the_same_lights_if_nothing_is_shaded(self):
        sut = LightCaster()

        squares = ['.', '.', '.']
        sectors = [ [1.0, 0.0] ]

        result = sut.getShadowedSquares(squares, sectors)

        assert result == ['.', '.', '.']

    def test_it_should_return_the_same_lights_for_the_empty_square(self):
        sut = LightCaster()

        squares = ['.']
        sectors = [ [1.0, 0.0] ]

        result = sut.getShadowedSquares(squares, sectors)

        assert result == ['.']

    def test_it_should_return_the_right_squres_with_multiple_sectors(self):
        sut = LightCaster()

        squares = ['.', '.', '.', '.']
        sectors = [ [1.0, 2.2 / 3.0], [0.4 / 3.5, 0.0] ]

        result = sut.getShadowedSquares(squares, sectors)

        # assert result == ['.', '.', 's', '.']

    def test_it_should_not_miss_shadow_squares_by_one(self):
        sut = LightCaster()
        squares  = list('..............')
        expected = list('...ss.........')
        sectors = [ [ 1.0, 9.5 / 11.5 ], [0.6, 0.0] ]
        result = sut.getShadowedSquares(squares, sectors)

        print(''.join(result), ''.join(expected))

        assert result == expected

    def test_it_should_return_new_sectors_from_old_ones(self):
        sut = LightCaster()
        squares = [ '.', '.', '#', '.']
        sectors = [ [ 1.0, 0.0 ] ]

        result = sut.getNewSectors(squares, sectors)

        assert result == [ [1.0, 1.5 / 2.5], [0.5 / 3.5, 0.0] ]

    def test_it_should_return_new_sectors_from_empty_ones(self):
        sut = LightCaster()
        squares = [ '.', '.', '.', '.']
        sectors = [ [ 1.0, 0.0 ] ]

        result = sut.getNewSectors(squares, sectors)

        assert result == [ [1.0, 0.0] ]

    def test_it_should_return_best_sectors_from_empty_ones(self):
        sut = LightCaster()
        squares = [ '.', '.', '#', '#',  '.']
        sectors = [ [ 1.0, 0.0 ] ]

        result = sut.getNewSectors(squares, sectors)

        assert result == [ [1.0, 2.5 / 3.5], [ 0.5 / 4.5, 0.0] ]

    def test_the_fourteenth_line(self):
        sut = LightCaster()
        expected = list('...ssss...s..ss')
        squares  = list('.....###.......')
        _prev    = list(' ...sss#..#..##')
        _prev2   = list(' ....##........')
        sectors = [
            [1.0,        9.5 / 11.5],
            [6.5 / 13.5, 4.5 / 12.5],
            [3.5 / 13.5, 1.5 / 12.5],
        ]
        result = sut.getShadowedSquares(squares, sectors)

        print('result: ' + ''.join(result))
        print('expect: ' + ''.join(expected))

        assert result == expected

    def test_the_thirteenth_line(self):
        sut = LightCaster()
        expected = list('...sss........')
        squares  = list('....###..#..##')
        _prev    = list(' ...##........')
        sectors = [
            [1.0, 9.5 / 11.5],
            [0.6, 0.0],
        ]
        result = sut.getShadowedSquares(squares, sectors)

        print('result: ' + ''.join(result))
        print('expect: ' + ''.join(expected))

        assert result == expected


    def test_it_should_get_all_stuff_right(self):
        sut = LightCaster()
        squares = [
            '.................', #16
            ' ......###.......', #15
            '  .....###.......', #14
            '   ....###..#..##', #13
            '    ...##........', #12
            '     ............', #11
            '      ...........', #10
            '       ..........', #9
            '        .........', #8
            '         ........', #7
            '          .......', #6
            '           ......', #5
            '            .....', #4
            '             ....', #3
            '              ...', #2
            '               ..', #1
            '                .', #0
        ]
        result = sut.getMask(squares)
        assert result == [
            '....sssss......ss',
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
