from app.components import MapScreen

class TestMapScreen:
    def test_it_should_use_the_screen_to_draw_a_map(self):
        state = {
            'settings': {
                'screen_size': [21, 13]
            }
        }
        sut = MapScreen()
        new_state = sut.render(state)
