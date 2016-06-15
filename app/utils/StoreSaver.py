import jsonpickle

class StoreSaver:
    def save(state):
        to_save = jsonpickle.encode(state)
        with open('../saves/store.json', 'w') as file:
            file.write(to_save)

    def load():
        state = '{}'
        with open('../saves/store.json', 'r') as file:
            state = file.read()
        return jsonpickle.decode(state)
