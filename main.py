import app
import app.map
import app.reducers
import app.utils
import app.keyboard
import app.monsters
import blessed

def main():

    s = app.map.MapGenerator()
    map = s.getMap(100, 1, 15, [600, 200])
    s_map = map

    position = [0, 0]
    screen_size = [21, 13]
    map_size = s_map['size']

    s = app.Screen()
    v = app.MapView()
    k = app.keyboard.MapKeyHandler()
    mah = app.keyboard.MoveAndAttackHandler()

    vtp = app.map.ValidTilePicker()

    positions = s.draw(map_size, screen_size, position)

    objects = []
    s_map['objects'] = []
    id = 2
    monsters = 100
    for e in range(monsters):
        tile = vtp.getRandomEmptyFloorTile(map)
        x = tile['pos'][0]
        y = tile['pos'][1]
        id += 1
        o = app.monsters.Rat(position=tile['pos'],x=x,y=y,id=id,hp=2)
        objects.append(o)

    state = {
        'map': s_map,
        'character': app.Character(id = 0, position=[300, 100]),
        'objects': objects,
    }

    reducers = [
        # handle character actions first
        app.reducers.AttackReducer(),
        app.reducers.CharacterMover(),
        app.reducers.CharacterShovel(),

        # monster and environment actions here
        app.reducers.MonsterMover(),

        # cleanup phase
        app.reducers.XpAssigner(),
        app.reducers.DeadMonsterCleaner(),
        app.reducers.GameOver(),
    ]

    key = None

    st = app.utils.Store(reducers, state)
    term = blessed.Terminal()
    moah = app.monsters.MonsterActionHandler()
    shadow_caster = app.map.TileShadowCaster()

    print(term.clear)
    while True:
        term.enter_fullscreen()
        state = st.getState()

        action    = mah.getAction(key, state)
        st.dispatch(action)

        monster_actions = moah.getMonsterActions(state)
        for a in monster_actions:
            st.dispatch(a)

        new_state = st.getState()

        c = new_state['character']
        pos = c.position
        positions = s.draw(map_size, screen_size, pos)
        objects = new_state['objects']

        with term.location(0, 0):
            tiles = shadow_caster.shade(map['tiles'], pos)

            for l in v.draw(tiles, positions, objects):
                print(''.join(l))

            print(action)
            print('hp:' + str(new_state['character'].hp))
            print('xp:' + str(new_state['character'].xp))

        if 'game_over' in new_state:
            term.exit_fullscreen()
            break;

        with term.cbreak():
            key = term.inkey()
    print(term.clear)
    print('seeya!')

if __name__ == "__main__":
    main()
