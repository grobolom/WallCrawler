import app
import app.Map
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

        print(blessed.Terminal().clear)
        for l in v.draw(new_state['map']['tiles'], positions, objects):
            print(''.join(l))

if __name__ == "__main__":
    main()
