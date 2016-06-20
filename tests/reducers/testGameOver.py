import app
import app.monsters
from app.reducers import GameOver

class TestGameOver:
    def test_it_should_end_the_game_when_the_action_is_game_over(self):
        sut = GameOver()

        action = { 'name': 'GAME_OVER' }
        state = { 'objects': [] }

        new_state = sut.reduce(state, action)

        assert new_state['game_over'] == True

    def test_it_should_end_the_game_when_there_are_no_monsters_left(self):
        sut = GameOver()

        action = { 'name': 'RANDOM' }
        state = { 'objects': [] }

        new_state = sut.reduce(state, action)

        assert new_state['game_over'] == True

    def test_it_should_end_the_game_if_the_player_has_no_hp(self):
        sut = GameOver()

        action = { 'name': 'RANDOM' }
        state = {
            'objects': [ app.monsters.Rat() ],
            'character': app.Character(hp = 0),
        }

        new_state = sut.reduce(state, action)

        assert new_state['game_over'] == True

    def test_it_should_not_end_the_game_if_there_are_monsters_left(self):
        sut = GameOver()

        action = { 'name': 'RANDOM' }
        state = { 'objects': [ app.Monster() ], 'character': app.Character() }

        new_state = sut.reduce(state, action)

        assert 'game_over' not in state
