from app.utils import Panel

class TestPanel:
    def test_it_should_draw_some_stuff(self):
        somestuff = [
            ".......",
            "xxx",
            "y",
            "!!!!!!!",
        ]
        expected = [
            ".....",
            "xxx  ",
            "y    ",
        ]
        sut = Panel()
        result = sut.draw(5, 3, somestuff)

        assert result == expected

    def test_it_should_treat_none_as_an_empty_line(self):
        somestuff = [
            "...",
            None,
            "...",
        ]
        expected = [
            "..",
            "  ",
        ]
        sut = Panel()
        result = sut.draw(2, 2, somestuff)

        assert result == expected
