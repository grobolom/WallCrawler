from app import KeyboardActionBuilder

class TestKeyboardActionBuilder:
    def test_it_should_map_j_to_move_down(self):
        key = 'j'
        k = KeyboardActionBuilder()

        assert k.getAction(key) == { 'name': 'MOVE_DOWN' }
    def test_it_should_map_k_to_move_up(self):
        key = 'k'
        k = KeyboardActionBuilder()

        assert k.getAction(key) == { 'name': 'MOVE_UP' }
    def test_it_should_map_l_to_move_right(self):
        key = 'l'
        k = KeyboardActionBuilder()

        assert k.getAction(key) == { 'name': 'MOVE_RIGHT' }
    def test_it_should_map_h_to_move_left(self):
        key = 'h'
        k = KeyboardActionBuilder()

        assert k.getAction(key) == { 'name': 'MOVE_LEFT' }

    def test_it_should_move_other_keys_to_nothing(self):
        key = ''
        k = KeyboardActionBuilder()

        assert k.getAction(key) == { 'name': 'NO_MOVE' }