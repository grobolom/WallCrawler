from app.Map import ShadowCaster

class TestShadowCaster:
    def test_it_should_draw_a_super_small_shadow(self):
        octet = [
            '   .',
            '  ..',
            ' ...',
            '@.#.',
        ]
        result = [
            '   .',
            '  ..',
            ' ...',
            '@.#.',
        ]
        sut = ShadowCaster()
        assert sut.getShadowMap(octet) == result

    def test_it_should_cast_some_small_shadows(self):
        octet = [
            '     .',
            '    ..',
            '   #..',
            '  ...#',
            ' .....',
            '@...#.',
        ]
        result = [
            '     s',
            '    s.',
            '   #..',
            '  ...#',
            ' .....',
            '@...#s',
        ]
    def test_it_should_cast_some_shadows(self):
        sut = ShadowCaster()
        octet = [
            '                .',
            '               ..',
            '              ...',
            '             ....',
            '            .....',
            '           ......',
            '          .......',
            '         ...####.',
            '        ....####.',
            '       ......###.',
            '      ...........',
            '     ............',
            '    .........#...',
            '   ..............',
            '  ...............',
            ' ............#...',
            '@............#...',
        ]
        result = [
            '                .',
            '               ..',
            '              ...',
            '             ....',
            '            ....s',
            '           ...sss',
            '          ...ssss',
            '         ...#ssss',
            '        ....##sss',
            '       ......###s',
            '      ...........',
            '     ............',
            '    .........#ss.',
            '   ..............',
            '  ...............',
            ' ............#sss',
            '@............#sss',
        ]
