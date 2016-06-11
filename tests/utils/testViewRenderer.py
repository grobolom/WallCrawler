from mock import MagicMock as Mock
from app.utils import ViewRenderer

class TestViewRenderer:
    def test_it_should_draw_a_view(self):
        mockView = Mock()
        sut = ViewRenderer({
            'main': mockView
        })
        state = { 'view': 'main' }
        sut.draw(state)

        mockView.draw.assert_called_once_with(state)
