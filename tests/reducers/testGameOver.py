from app.reducers import GameOver

class TestGameOver:
    def it_should_end_the_game_when_the_action_is_game_over(self):
        sut = GameOver()

        action = { 'name': 'GAME_OVER' }
        state = {}

        new_state = sut.reduce(state, action)

        assert new_state['game_over'] == True
