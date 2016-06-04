from app.Map import ShadowCaster

class TestShadowCaster:
    def test_it_should_check_if_square_is_in_sector(self):
        sut = ShadowCaster()
        square = [2, 2]
        sector = [1, 0]
        assert sut.squareInSector(square, sector) == True
