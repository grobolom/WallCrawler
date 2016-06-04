from app.Map import ShadowCaster

class TestShadowCaster:
    def test_it_should_check_if_square_is_in_sector(self):
        sut = ShadowCaster()
        square = [2, 2]
        sector = [1.0, 0]
        assert sut.squareInSector(square, sector) == True

    def test_it_should_include_if_bottom_right_corner_is_in_sector(self):
        sut = ShadowCaster()
        square = [4, 3]
        sector = [5.0 / 7.0, 0]
        assert sut.squareInSector(square, sector) == True

    def test_it_should_exclude_if_the_bottom_right_touches_top_line(self):
        sut = ShadowCaster()
        square = [3, 3]
        sector = [5.0 / 7.0, 0]
        assert sut.squareInSector(square, sector) == False

    def test_it_should_include_if_center_is_between_lines(self):
        sut = ShadowCaster()
        square = [5, 3]
        sector = [5.0 / 7.0, 5.0 / 9.0]
        assert sut.squareInSector(square, sector) == True

    def test_it_should_include_if_top_left_between_lines(self):
        sut = ShadowCaster()
        square = [4, 2]
        sector = [5.0 / 7.0, 5.0 / 9.0]
        assert sut.squareInSector(square, sector) == True

