from app.keyboard import MoveAndAttackHandler
import app

class TestMoveAndAttackHandler:
    def test_it_should_attack_if_the_move_square_contains_a_monster(self):
        character = app.Character(position=[0, 0])
        monster = app.Monster(position=[1, 0])

        state = {
            'map': {
                'tiles': [[ app.Floor(), app.Floor() ]],
                'size': [2, 1],
            },
            'character': character,
            'objects': [ character, monster ],
        }

        key = 'l'

        sut = MoveAndAttackHandler()

        expected = {
            'name': 'ATTACK_CHARACTER',
            'source': character,
            'target': monster,
        }

        assert sut.getAction(key, state) == expected

    def test_it_should_move_if_the_square_is_empty(self):
        character = app.Character(position=[0, 0])

        state = {
            'map': {
                'tiles': [[ app.Floor(), app.Floor() ]],
                'size': [2, 1],
            },
            'character': character,
            'objects': [ character ],
        }

        key = 'l'

        sut = MoveAndAttackHandler()

        expected = {
            'name': 'MOVE_CHARACTER',
            'to': [1, 0]
        }

        assert sut.getAction(key, state) == expected
