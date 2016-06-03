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
