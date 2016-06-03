import app
from app.reducers import DeadMonsterCleaner

class TestDeadMonsterCleaner:
    def test_it_should_remove_a_monster_with_zero_health(self):
        sut = DeadMonsterCleaner()

        dead_monster = app.Monster(id = 1, hp = 0)
        action = {}
        state = {
            'objects': [ dead_monster ]
        }

        new_state = sut.reduce(state, action)

        assert new_state['objects'] == []

    def test_it_should_remove_all_monsters_with_less_than_one_health(self):
        sut = DeadMonsterCleaner()

        dead_monster = app.Monster(id = 1, hp = 0)
        live_monster = app.Monster(id = 2, hp = 10)
        superdead_monster = app.Monster(id = 3, hp = -5)

        action = {}
        state = {
            'objects': [ dead_monster, live_monster, superdead_monster ]
        }

        new_state = sut.reduce(state, action)

        assert len(new_state['objects']) == 1
        assert new_state['objects'][0].id == 2

    def test_it_should_only_remove_monsters(self):
        sut = DeadMonsterCleaner()

        dead_monster = app.Monster(id = 1, hp = 0)
        character = app.Character(id = 2)

        action = {}
        state = {
            'objects': [ dead_monster, character ]
        }

        new_state = sut.reduce(state, action)

        assert len(new_state['objects']) == 1
        assert new_state['objects'][0].id == 2
