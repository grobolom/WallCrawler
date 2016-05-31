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

    position = [6, 6]
    screen_size = [7, 7]
    map_size = s_map['size']

    s = app.Screen()
    v = app.MapView()
    r = app.PositionReducer()
    k = app.KeyboardActionBuilder()

    positions = s.draw(map_size, screen_size, position)

    state = {
        'map': s_map,
        'character': app.Character(),
        'objects': [],
    }

    key = None
    new_state = state

    while True:
        with blessed.Terminal().cbreak():
            key = blessed.Terminal().inkey()

        action    = k.getAction(key)
        new_state = r.reduce(new_state, action)

        c = new_state['character']
        pos = (c.x, c.y)
        positions = s.draw(map_size, screen_size, pos)
        objects = new_state['objects']

        for l in v.draw(new_state['map']['tiles'], positions, objects):
            print(''.join(l))

if __name__ == "__main__":
    main()
