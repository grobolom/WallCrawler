from app import Screen

class TestScreen:
    def test_it_should_draw_a_screen_around_the_character(self):
        m = {
            'character_position': (0, 0),
            'map_size':           (10, 10),
            'screen_size':        (5, 5),
        }
        s = Screen()

        result = s.draw(m)
        assert result == [
            '@....',
            '.....',
            '.....',
            '.....',
            '.....',
        ]

    def test_it_should_draw_something_around_a_center_point(self):
        m = {
            'character_position': (2, 2),
            'map_size':           (10, 10),
            'screen_size':        (7, 7),
        }
        s = Screen()

        result = s.draw(m)
        assert result == [
            '.......',
            '.......',
            '..@....',
            '.......',
            '.......',
            '.......',
            '.......',
        ]
