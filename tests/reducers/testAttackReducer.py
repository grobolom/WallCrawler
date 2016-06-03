import app
from app.reducers import AttackReducer

class TestAttackReducer:
    def test_it_should_reduce_target_health(self):
        sut = AttackReducer()

        START_HP = 10
        END_HP = 9

        character = app.Character()
        monster = app.Monster(id = 2, hp = START_HP)

        action = {
            'name': 'ATTACK_CHARACTER',
            'source': character,
            'target': monster,
        }

        state = {
            'character': character,
            'objects': [ monster ]
        }

        new_state = sut.reduce(action, state)

        assert new_state['objects'][0].hp == END_HP
