import unittest
from app import Screen

import app

class TestScreen(unittest.TestCase):
    def test_it_should_draw_a_screen_around_a_point(self):
        s = Screen()
        map_size = [10, 10]
        screen_size = [3, 3]
        selected_point = [1, 1]

        expected = [
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
        ]
        assert expected == s.draw(map_size, screen_size, selected_point)

    def test_it_should_not_draw_past_the_bottom_right(self):
        s = Screen()
        map_size = [10, 10]
        screen_size = [3, 3]
        selected_point = [9, 9]

        expected = [
            [(7, 7), (8, 7), (9, 7)],
            [(7, 8), (8, 8), (9, 8)],
            [(7, 9), (8, 9), (9, 9)],
        ]
        assert expected == s.draw(map_size, screen_size, selected_point)

    def test_it_should_not_draw_past_the_top_right(self):
        pass
    def test_it_should_not_draw_past_the_top_left(self):
        pass
