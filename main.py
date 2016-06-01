import app
import app.Map
import app.reducers
import app.keyboard
import app.utils
import blessed

def main():

    rm = app.Map.RoomMaker()
    s_map = {
        'tiles': [ [ app.Tile() for i in range(80) ] for j in range(20) ],
        'size': [80, 20],
    }

    s_map = rm.addRoom(s_map, (0, 0), (5, 5))
    s_map = rm.addRoom(s_map, (5, 4), (5, 5))
    s_map = rm.addRoom(s_map, (2, 5), (3, 3))

    position = [6, 6]
    screen_size = [7, 7]
    map_size = s_map['size']

    s = app.Screen()
    v = app.MapView()
    k = app.keyboard.MapKeyHandler()

    positions = s.draw(map_size, screen_size, position)

    state = {
        'map': s_map,
        'character': app.Character(),
        'objects': [],
    }

    reducers = [
        app.reducers.CharacterMover(),
        app.reducers.CharacterShovel(),
    ]

    key = None

    st = app.utils.Store(reducers, state)

    while True:
        state = st.getState()
        with blessed.Terminal().cbreak():
            key = blessed.Terminal().inkey()
        print(blessed.Terminal().clear)

        action    = k.getAction(key, state)

        st.dispatch(action)
        new_state = st.getState()

        c = new_state['character']
        pos = (c.x, c.y)
        positions = s.draw(map_size, screen_size, pos)
        objects = new_state['objects']

        for l in v.draw(new_state['map']['tiles'], positions, objects):
            print(''.join(l))

        print(action)

if __name__ == "__main__":
    main()
