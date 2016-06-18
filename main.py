import app
import app.map
import app.reducers
import app.utils
import app.keyboard
import app.monsters
import blessed

def main():

    s = app.map.MapGenerator()
    map = s.getMap(1, 1, 1, [80, 20])
    s_map = map

    position = [0, 0]
    screen_size = [21, 13]
    map_size = s_map['size']

    s = app.Screen()
    v = app.MapView()
    k = app.keyboard.MapKeyHandler()

    mah = app.KeyboardActionBuilder(
        app.keyboard.MoveAndAttackHandler()
    )

    vtp = app.map.ValidTilePicker()

    positions = s.draw(map_size, screen_size, position)

    objects = []
    s_map['objects'] = []
    id = 2
    monsters = 2
    for e in range(monsters):
        tile = vtp.getRandomEmptyFloorTile(map)
        x = tile['pos'][0]
        y = tile['pos'][1]
        id += 1
        o = app.monsters.Rat(position=tile['pos'],x=x,y=y,id=id,hp=2)
        objects.append(o)

    state = {
        'map': s_map,
        'character': app.Character(id = 0, position=[40, 10]),
        'objects': objects,
        'view': 'main',
    }

    store_saver = app.utils.StoreSaver()
    store_saver.save(state)

    reducers = [
        # view-related actions first?
        app.reducers.ViewSwitcher(),

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
    screen = app.utils.Screen(term)
    panel = app.utils.Panel()
    menu_panel = app.utils.MenuPanel()

    print(term.clear)
    term.enter_fullscreen()
    while True:
        term.move(0, 0)
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

        tiles = shadow_caster.shade(map['tiles'], pos)
        tiles_map = [ ''.join(l) for l in v.draw(tiles, positions, objects) ]
        menu = [
            '  (S): Save And Quit',
            '  (Q): Quit         ',
            '(ESC): Continue     ',
        ]

        if new_state['view'] == 'main':
            screen.draw(0, 21, panel.draw(20, 10, [
                action['name'],
                'hp:' + str(new_state['character'].hp),
                'xp:' + str(new_state['character'].xp),
                key,
                new_state['view'],
            ] + [ a['target'] for a in monster_actions if a['name'] == 'ATTACK']))
            screen.draw(0, 0, panel.draw(80, 20, tiles_map))
        else:
            screen.draw(5, 5, panel.draw(40, 20,
                 menu_panel.draw(40, 20, menu)
            ))

        if 'game_over' in new_state:
            term.exit_fullscreen()
            break;

        with term.cbreak():
            key = term.inkey()
            if key.is_sequence:
                key = key.name
    print(term.clear)
    print('seeya!')

if __name__ == "__main__":
    main()
