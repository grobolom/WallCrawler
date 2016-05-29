from app import Screen

class TestScreen:
    def test_it_should_draw_a_screen_around_the_character(self):
        m = {
            'character_position': (0, 0),
            'map_size': (10, 10),
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
