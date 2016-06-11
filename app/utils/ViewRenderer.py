class ViewRenderer:
    def __init__(self, views):
        self.views = views


    def draw(self, state):
        view_to_draw = state['view']
        return self.views[view_to_draw].draw(state)
