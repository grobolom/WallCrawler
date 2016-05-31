class Screen:
    def draw(self, map_size, screen_size, selected_point):
        pos = self._getFakeCenter(map_size, screen_size, selected_point)

        screen_size_x = screen_size[0]
        screen_size_y = screen_size[1]

        radius_x = (screen_size_x - 1) / 2
        radius_y = (screen_size_y - 1) / 2

        indices_x = range(pos[0] - radius_x, pos[0] + radius_x + 1)
        indices_y = range(pos[1] - radius_y, pos[1] + radius_y + 1)

        return [[ (x, y) for x in indices_x ] for y in indices_y ]

    def _getFakeCenter(self, m, s, p):
        return p

    def x_draw(self, obj):
        c_position  = obj['character_position']
        map_size    = obj['map']['size']
        screen_size = obj['screen_size']

        centered = self.centered(obj)
        if centered:
            pos = self.centered_pos(obj)
        else:
            pos = self.offset_pos(obj)

        screen_size_x = obj['screen_size'][0]
        screen_size_y = obj['screen_size'][1]

        radius_x = (screen_size_x - 1) / 2
        radius_y = (screen_size_y - 1) / 2

        indices_x = range(pos[0] - radius_x, pos[0] + radius_x + 1)
        indices_y = range(pos[1] - radius_y, pos[1] + radius_y + 1)

        s = [[
            obj['map']['tiles'][x][y].ascii_rep
                for x in indices_x ]
                for y in indices_y ]

        return s

    def centered_pos(self, obj):
        pos_x = obj['character_position'][0]
        pos_y = obj['character_position'][1]

        return (
            pos_x,
            pos_y,
        )

    def offset_pos(self, obj):
        screen_size_x = obj['screen_size'][0]
        screen_size_y = obj['screen_size'][1]

        position_x = obj['character_position'][0]
        position_y = obj['character_position'][1]

        radius_x = (screen_size_x - 1) / 2
        radius_y = (screen_size_y - 1) / 2

        map_size_x = obj['map']['size'][0] - 1
        map_size_y = obj['map']['size'][1] - 1

        fake_x = sorted([0 + radius_x, position_x, map_size_x - radius_x])[1]
        fake_y = sorted([0 + radius_y, position_y, map_size_y - radius_y])[1]

        return (
            fake_x, 
            fake_y,
        )

    def centered(self, obj):
        screen_size_x = obj['screen_size'][0]
        screen_size_y = obj['screen_size'][1]

        position_x = obj['character_position'][0]
        position_y = obj['character_position'][1]

        radius_x = (screen_size_x - 1) / 2
        radius_y = (screen_size_y - 1) / 2

        map_end_x = obj['map']['size'][0] - 1
        map_end_y = obj['map']['size'][1] - 1

        return  position_x + radius_x <= map_end_x and \
                position_y + radius_y <= map_end_y and \
                position_x - radius_x >= 0 and \
                position_y - radius_y >= 0
