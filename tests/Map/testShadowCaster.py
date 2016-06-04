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

    def test_it_should_return_the_next_set_of_sectors(self):
        sut = ShadowCaster()
        column = ['#','.','.','.']
        start_sectors = ( [1.0, 0.0], )
        result = sut.getSectors(column, start_sectors)
        assert result == [ [2.5 / 3.5, 0.0], ]

    def test_it_should_adjust_only_needed_sectors(self):
        sut = ShadowCaster()
        column = ['.','.','.','#']
        start_sectors = ( [1.0, 0.0], )
        result = sut.getSectors(column, start_sectors)
        assert result == [ [1.0, 0.5 / 2.5], ]

    def test_it_should_adjust_both_ends_of_the_sector(self):
        sut = ShadowCaster()
        column = ['#','.','.','#']
        start_sectors = ( [1.0, 0.0], )
        result = sut.getSectors(column, start_sectors)
        assert result == [ [2.5 / 3.5, 0.5 / 2.5], ]

    def test_it_should_split_a_sector_with_a_blocker(self):
        sut = ShadowCaster()
        column = ['.','.','#','.']
        start_sectors = ( [1.0, 0.0], )
        result = sut.getSectors(column, start_sectors)
        """
        assert result == (
            [ 1.0, 1.5 / 2.5 ],
            [ 0.5 / 3.5, 0.0 ],
        )
        """
