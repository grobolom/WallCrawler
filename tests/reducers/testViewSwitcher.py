from app.reducers import ViewSwitcher

class TestViewSwitcher:
    def test_it_should_switch_view_to_the_target_view(self):
        sut = ViewSwitcher()
        state = { 'view': 'main' }
        action = { 'name': 'SWITCH_VIEW', 'to': 'menu' }
        result = sut.reduce(state, action)
        expected = { 'view': 'menu' }

        assert expected == result
