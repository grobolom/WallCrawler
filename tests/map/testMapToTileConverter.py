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

