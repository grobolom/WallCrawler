import app

def main():
    state = {
        'character_position': [0, 0],
        'map_size': [5, 5],
        'screen_size': [3, 3],
    }

    s = app.Screen()
    r = app.PositionReducer()

    while True:
        print('\n'. join(s.draw(state)))
        i = raw_input('> ')

if __name__ == "__main__":
    main()
