# for now, some bs code to figure out how we want to do state transitions


class State:
    def handleStateTransition(self):
        state = ''
        key = ''
        action = reduce(state, key)

        view = ''

        # start
        if view == 'start' and key == 'load':
            load_game()
            go_to_main_view()

        if view == 'start' and key == 'new':
            go_to_main_view()

        # menu
        if view == 'menu' and key == 'save_and_quit':
            save_game()
            quit()

        if view == 'menu' and key == 'quit':
            quit()

        if view == 'menu' and key == 'escape':
            go_to_main_view()

    def displayView(self,  view):
        if view == 'splash_screen':
            return displayScreen()

        if view == 'start_menu':
            return displayStartMenu()

        if view == 'menu':
            return displayGameMenu()

        return displayMapView()

