import unittest
from app import Screen

import app

class TestScreen(unittest.TestCase):
    def setUp(self):
        self.map = {
            'tiles': [ [ app.Floor() for i in range(10) ] for j in range(10) ],
            'size': [10, 10]
        }

    def test_it_should_draw_a_screen_around_the_character(self):
        self.map['tiles'][2][2] = app.Wall()
        m = {
            'character_position': (2, 2),
            'screen_size':        (5, 5),
            'map':                self.map,
        }
        s = Screen()

        result = s.draw(m)
        assert result == [
            list('.....'),
            list('.....'),
            list('..#..'),
            list('.....'),
            list('.....'),
        ]


    def test_it_should_draw_the_bottom_right_corner(self):
        self.map['tiles'][8][8] = app.Wall()
        m = {
            'character_position': (8, 8),
            'screen_size':        (3, 3),
            'map':                self.map
        }
        s = Screen()

        result = s.draw(m)
        assert result == [
            list('...'),
            list('.#.'),
            list('...'),
        ]

    def test_it_should_draw_a_character_in_the_bottom_right(self):
        self.map['tiles'][9][9] = app.Wall()
        m = {
            'character_position': (9, 9),
            'screen_size':        (5, 5),
            'map':                self.map
        }
        s = Screen()

        result = s.draw(m)
        assert result == [
            list('.....'),
            list('.....'),
            list('.....'),
            list('.....'),
            list('....#'),
        ]

    def test_it_should_draw_a_character_in_the_top_right(self):
        self.map['tiles'][8][0] = app.Wall()
        m = {
            'character_position': (8, 0),
            'screen_size':        (5, 5),
            'map':                self.map
        }
        s = Screen()

        result = s.draw(m)
        assert result == [
            list('...#.'),
            list('.....'),
            list('.....'),
            list('.....'),
            list('.....'),
        ]

    def test_it_should_draw_a_character_in_the_top_left(self):
        self.map['tiles'][0][0] = app.Wall()
        m = {
            'character_position': (0, 0),
            'screen_size':        (5, 5),
            'map':                self.map
        }
        s = Screen()

        result = s.draw(m)
        assert result == [
            list('#....'),
            list('.....'),
            list('.....'),
            list('.....'),
            list('.....'),
        ]
