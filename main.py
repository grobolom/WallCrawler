import app
import app.Map
import app.reducers
import app.keyboard
import app.utils
import blessed

def main():

    s = app.Map.MapGenerator()
    map = s.getMap(30, 1, 10, [80, 20])
    s_map = map

    position = [0, 0]
    screen_size = [80, 20]
    map_size = s_map['size']

    s = app.Screen()
    v = app.MapView()
    k = app.keyboard.MapKeyHandler()

    vtp = app.Map.ValidTilePicker()

    positions = s.draw(map_size, screen_size, position)

    objects = []
    s_map['objects'] = []
    for e in range(10):
        tile = vtp.getRandomEmptyFloorTile(map)
        x = tile['pos'][0]
        y = tile['pos'][1]
        o = app.Monster(position=tile['pos'],x=x,y=y)
        objects.append(o)

    state = {
        'map': s_map,
        'character': app.Character(x=41,y=11),
        'objects': objects,
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
        # print(blessed.Terminal().clear)

        action    = k.getAction(key, state)

        st.dispatch(action)
        new_state = st.getState()

        c = new_state['character']
        pos = (c.x, c.y)
        positions = s.draw(map_size, screen_size, pos)
        objects = new_state['objects']

        print("0123456789" * 8)
        for l in v.draw(new_state['map']['tiles'], positions, objects):
            print(''.join(l)) + '!'

if __name__ == "__main__":
    main()
