import app

class TestCharacterShovel:
    def test_it_should_shovel_the_character_into_the_list_of_objects(self):
        c = app.Character()
        someObject = app.Object()
        objects = [ someObject ]

        state = {
            'objects': objects,
            'character': c,
        }

        expected = [ someObject, c ]

        reducer = app.reducers.CharacterShovel()
        new_state = reducer.reduce(state, {})

        assert expected == new_state['objects']
