from app.utils import MenuPanel

class TestMenuPanel:
    def test_it_should_draw_a_border_around_some_centered_stuff(self):
        sut = MenuPanel()
        menu_stuff = [
            'some stuff',
            'some more stuff',
            'x',
        ]
        result = sut.draw(25, 7, menu_stuff)

        assert result == [
            '=========================',
            '=                       =',
            '=       some stuff      =',
            '=    some more stuff    =',
            '=           x           =',
            '=                       =',
            '=========================',
        ]
