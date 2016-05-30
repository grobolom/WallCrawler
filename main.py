import app

def main():
    state = {
        'character_position': [0, 0],
        'map_size': [5, 5],
        'screen_size': [3, 3],
    }

    s = app.Screen()
    r = app.PositionReducer()
    k = app.KeyboardActionBuilder()

    i = ''
    new_state = state
    while True:
        action = k.getAction(i)
        new_state = r.reduce(new_state, action)
        print('\n'. join(s.draw(new_state)))
        print(state['character_position'])

        i = raw_input('> ')

if __name__ == "__main__":
    main()
