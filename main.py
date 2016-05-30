import app
import blessed

def main():
    s_map = {
        'tiles': [ [ app.Floor() for i in range(10) ] for j in range(10) ],
        'size': [10, 10]
    }
    s_map['tiles'][2][2] = app.Wall()
    s_map['tiles'][7][7] = app.Wall()
    s_map['tiles'][7][2] = app.Wall()
    s_map['tiles'][2][7] = app.Wall()

    state = {
        'character_position': [0, 0],
        'screen_size': [5, 5],
        'map': s_map,
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

        for l in s.draw(new_state):
            print(''.join(l))

        print(state['character_position'])


if __name__ == "__main__":
    main()
