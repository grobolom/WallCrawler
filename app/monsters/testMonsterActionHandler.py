import app
from app.monsters import MonsterActionHandler

from mock import MagicMock as Mock

class TestMonsterActionHandler:
    def test_it_should_get_an_action_from_every_monster(self):
        sut = MonsterActionHandler()

        monster1 = app.Monster(id = 1)
        monster2 = app.Monster(id = 2)

        monster1.getAction = Mock()
        monster2.getAction = Mock()

        state = {
            'objects': [ monster1, monster2 ],
        }
        actions = sut.getMonsterActions(state)

        assert len(actions) == 2
        assert monster1.getAction.called_once_with(state)
        assert monster2.getAction.called_once_with(state)
