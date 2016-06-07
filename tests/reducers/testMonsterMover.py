import app
from app.reducers import MonsterMover

class TestMonsterMover:
    def test_it_should_move_a_monster(self):
        sut = MonsterMover()

        first_monster = app.Monster(position = [0, 1], id = 1)
        second_monster = app.Monster(position = [0, 0], id = 2)

        action = {
            'name': 'MOVE',
            'target': 2,
            'to': [1, 1],
        }
        state = { 'objects': [ first_monster, second_monster ] }

        new_state = sut.reduce(state, action)

        assert new_state['objects'][0].position == [0, 1]
        assert new_state['objects'][1].position == [1, 1]

    def test_it_should_not_move_monsters_into_occupied_squares(self):
        sut = MonsterMover()

        first_monster = app.Monster(position = [0, 1], id = 1)
        second_monster = app.Monster(position = [1, 1], id = 2)

        action = {
            'name': 'MOVE',
            'target': 1,
            'to': [1, 1],
        }
        state = { 'objects': [ first_monster, second_monster ] }

        new_state = sut.reduce(state, action)

        assert new_state['objects'][0].position == [0, 1]
        assert new_state['objects'][1].position == [1, 1]
