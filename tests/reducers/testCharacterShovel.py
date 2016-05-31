import app

class TestCharacterShovel:
    def test_it_should_shovel_the_character_into_the_list_of_objects(self):
        c = app.Character()
        some_object = app.Object()
        objects = [ some_object ]

        state = {
            'objects': objects,
            'character': c,
        }

        expected = [ some_object, c ]

        reducer = app.reducers.CharacterShovel()
        new_state = reducer.reduce(state, {})

        assert expected == new_state['objects']

    def test_it_should_overwrite_the_existing_character_object(self):
        c = app.Character()
        some_object = app.Object()
        objects = [ some_object, c ]

        changed_c = app.Character()
        changed_c.x = 'blablabla'

        state = {
            'objects': objects,
            'character': c,
        }

        expected = [ some_object, c ]

        reducer = app.reducers.CharacterShovel()
        new_state = reducer.reduce(state, {})

        assert expected == new_state['objects']
