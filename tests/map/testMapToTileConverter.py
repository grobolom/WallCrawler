import app
from app.map import MapToTileConverter

class TestMapToTileConverter:
    def test_it_should_convert_tiles(self):
        squares = [
            list('..#..'),
            list('.#...'),
            list('#....'),
            list('....#'),
            list('...#.'),
        ]
        expected = [
            [ app.Floor(), app.Floor(), app.Wall(),  app.Floor(), app.Floor() ],
            [ app.Floor(), app.Wall(),  app.Floor(), app.Floor(), app.Floor() ],
            [ app.Wall(),  app.Floor(), app.Floor(), app.Floor(), app.Floor() ],
            [ app.Floor(), app.Floor(), app.Floor(), app.Floor(), app.Wall()  ],
            [ app.Floor(), app.Floor(), app.Floor(), app.Wall(),  app.Floor() ],
        ]
        sut = MapToTileConverter()
        result = sut.convertToTiles(squares)

        assert result == expected

    def test_it_should_convert_simple_tiles_back_to_squares(self):
        tiles = [
            [ app.Floor(), app.Floor(), app.Wall(),  app.Floor(), app.Floor() ],
            [ app.Floor(), app.Wall(),  app.Floor(), app.Floor(), app.Floor() ],
            [ app.Wall(),  app.Floor(), app.Floor(), app.Floor(), app.Floor() ],
            [ app.Floor(), app.Floor(), app.Floor(), app.Floor(), app.Wall()  ],
            [ app.Floor(), app.Floor(), app.Floor(), app.Wall(),  app.Floor() ],
        ]
        expected = [
            list('..#..'),
            list('.#...'),
            list('#....'),
            list('....#'),
            list('...#.'),
        ]
        sut = MapToTileConverter()
        result = sut.convertToSquares(tiles)

        assert result == expected

    def test_it_should_convert_until_tiles_to_blanks(self):
        tiles = [
            [ app.Floor(lit = False) ],
        ]
        expected = [[ ' ' ]]
        sut = MapToTileConverter()
        result = sut.convertToSquares(tiles)

        assert result == expected
