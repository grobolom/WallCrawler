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

        new_state = sut.reduce(state, action)

        assert new_state['objects'][0].hp == END_HP

    # TODO: switch this to 'character dies' instead of 'hp below 1'
    # we should be using actual game terms
    def test_it_should_mark_monster_as_dead_if_hp_gets_below_1(self):
        sut = AttackReducer()

        character = app.Character(xp = 0)
        monster = app.Monster(id = 2, hp = 1, xp = 2)

        action = {
            'name': 'ATTACK_CHARACTER',
            'source': character,
            'target': monster,
        }

        state = {
            'character': character,
            'objects': [ monster ],
        }

        new_state = sut.reduce(state, action)

        assert new_state['objects'][0].isDead() == True

    def test_it_should_only_target_health_with_correct_id(self):
        sut = AttackReducer()

        START_HP = 10
        END_HP = 9

        character = app.Character()
        monster_right = app.Monster(id = 2, hp = START_HP)
        monster_wrong = app.Monster(id = 3, hp = START_HP)

        action = {
            'name': 'ATTACK_CHARACTER',
            'source': character,
            'target': monster_right,
        }

        state = {
            'character': character,
            'objects': [ monster_right, monster_wrong ]
        }

        new_state = sut.reduce(state, action)

        assert new_state['objects'][0].hp == END_HP
        assert new_state['objects'][1].hp == START_HP

