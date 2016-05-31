import app

class TestCharacterShovel:
    def test_it_should_shovel_the_character_into_the_list_of_objects(self):
        c = app.Character()
        objects = []

        state = {
            'objects': objects,
            'character': c,
        }

        expected = [ c ]

        reducer = app.reducers.CharacterShovel()
        new_state = reducer.reduce(state, {})

        assert expected == new_state['objects']
