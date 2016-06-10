from mock import MagicMock as Mock
from app import KeyboardActionBuilder

class TestKeyboardActionBuilder:
    def test_it_should_delegate_movement_to_another_handler(self):
        key = 'j'
        state = {}
        handler = Mock()
        sut = KeyboardActionBuilder(handler)
        sut.getAction(key, state)

        handler.getAction.assert_called_once_with(key, state)

    def test_it_should_move_other_keys_to_nothing(self):
        key = ''
        k = KeyboardActionBuilder()

        assert k.getAction(key, {}) == { 'name': 'NO_MOVE' }

    def test_it_should_open_the_menu_on_escape(self):
        key = 'KEY_ESCAPE'
        k = KeyboardActionBuilder()
        assert k.getAction(key, {}) == {
            'name': 'SWITCH_VIEW',
            'to': 'menu',
        }

    def test_it_should_leave_the_menu_on_escape(self):
        key = 'KEY_ESCAPE'
        state = { 'view': 'menu' }
        k = KeyboardActionBuilder()
        assert k.getAction(key, state) == {
            'name': 'SWITCH_VIEW',
            'to': 'main',
        }
