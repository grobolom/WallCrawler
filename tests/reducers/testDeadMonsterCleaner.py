import app
from app.reducers import DeadMonsterCleaner

class TestDeadMonsterCleaner:
    def test_it_should_remove_all_dead_monsters(self):
        sut = DeadMonsterCleaner()

        character = app.Character(id = 2, dead = True)
        dead_monster = app.Monster(id = 1, hp = 0, dead = True)
        live_monster = app.Monster(id = 2, hp = 10, dead = False)
        dead_with_hp = app.Monster(id = 3, hp = -5, dead = True)

        action = {}
        state = {
            'character': character,
            'objects': [ dead_monster, live_monster, dead_with_hp ],
        }

        new_state = sut.reduce(state, action)

        assert len(new_state['objects']) == 1
        assert new_state['objects'][0].id == 2

    def test_it_should_only_remove_monsters(self):
        sut = DeadMonsterCleaner()

        dead_monster = app.Monster(id = 1, dead = True)
        character = app.Character(id = 2, dead = True)

        action = {}
        state = {
            'character': character,
            'objects': [ dead_monster, character ]
        }

        new_state = sut.reduce(state, action)

        assert len(new_state['objects']) == 1
        assert new_state['objects'][0].id == 2

    def test_it_should_give_dead_monster_xp_to_the_character(self):
        sut = DeadMonsterCleaner()

        character = app.Character(id = 2, xp = 2)
        monster = app.Monster(xp = 3, id = 1, dead = True, source = character)

        action = {}
        state = {
            'character': character,
            'objects': [ monster, character ],
        }

        new_state = sut.reduce(state, action)

        assert new_state['character'].xp == 5
