import app
from app.reducers import XpAssigner

class TestXpAssigner:
    def test_it_should_give_dead_monster_xp_to_the_character(self):
        sut = XpAssigner()
        character = app.Character(xp = 7)
        dead_monster = app.Monster(xp = 2, dead = True)
        live_monster = app.Monster(xp = 5)

        action = {}
        state = {
            'character': character,
            'objects': [ character, dead_monster, live_monster ],
        }

        new_state = sut.reduce(state, action)

        assert new_state['character'].xp == 9
