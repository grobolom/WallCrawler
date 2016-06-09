import app

class TestTile:
    def test_it_should_return_an_ascii_rep_when_lit(self):
        sut = app.Tile()
        sut.ascii_rep = '#'
        sut.lit = True
        assert sut.getAsciiRep() == '#'

    def test_it_should_return_an_empty_space_when_not_lit(self):
        sut = app.Tile()
        sut.ascii_rep = '#'
        sut.lit = False
        assert sut.getAsciiRep() == ' '

    def test_it_should_return_an_empty_space_when_not_set(self):
        sut = app.Tile()
        sut.ascii_rep = '#'
        assert sut.getAsciiRep() == ' '
