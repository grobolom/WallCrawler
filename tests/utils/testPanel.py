from app.utils import Panel

class TestPanel:
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
