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
        s = Screen()
        map_size = [10, 10]
        screen_size = [3, 3]
        selected_point = [9, 0]

        expected = [
            [(7, 0), (8, 0), (9, 0)],
            [(7, 1), (8, 1), (9, 1)],
            [(7, 2), (8, 2), (9, 2)],
        ]
        assert expected == s.draw(map_size, screen_size, selected_point)

    def test_it_should_not_draw_past_the_top_left(self):
        s = Screen()
        map_size = [10, 10]
        screen_size = [3, 3]
        selected_point = [0, 9]

        expected = [
            [(0, 7), (1, 7), (2, 7)],
            [(0, 8), (1, 8), (2, 8)],
            [(0, 9), (1, 9), (2, 9)],
        ]
        assert expected == s.draw(map_size, screen_size, selected_point)

    def test_it_should_draw_an_even_size_screen(self):
        s = Screen()
        map_size = [4, 4]
        screen_size = [4, 4]
        selected_point = [0, 0]
        expected = [
            [(0, 0), (1, 0), (2, 0), (3, 0)],
            [(0, 1), (1, 1), (2, 1), (3, 1)],
            [(0, 2), (1, 2), (2, 2), (3, 2)],
            [(0, 3), (1, 3), (2, 3), (3, 3)],
        ]

        assert expected == s.draw(map_size, screen_size, selected_point)

    def test_it_should_draw_an_even_size_sub_screen(self):
        s = Screen()
        map_size = [6, 6]
        screen_size = [4, 4]
        selected_point = [5, 5]
        expected = [
            [(2, 2), (3, 2), (4, 2), (5, 2)],
            [(2, 3), (3, 3), (4, 3), (5, 3)],
            [(2, 4), (3, 4), (4, 4), (5, 4)],
            [(2, 5), (3, 5), (4, 5), (5, 5)],
        ]

        assert expected == s.draw(map_size, screen_size, selected_point)
