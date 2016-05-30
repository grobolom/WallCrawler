import app
import blessed

def main():
    state = {
        'character_position': [0, 0],
        'map_size': [5, 5],
        'screen_size': [3, 3],
    }

    s = app.Screen()
    r = app.PositionReducer()
    k = app.KeyboardActionBuilder()

    key = None
    new_state = state

    while True:
        with blessed.Terminal().cbreak():
            key = blessed.Terminal().inkey()

        action = k.getAction(key)
        new_state = r.reduce(new_state, action)
        print('\n'. join(s.draw(new_state)))
        print(state['character_position'])


if __name__ == "__main__":
    main()
