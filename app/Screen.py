class Screen:
    def draw(self, obj):
        c_position  = obj['character_position']
        map_size    = obj['map_size']
        screen_size = obj['screen_size']

        centered = self.centered(obj)
        if centered:
            pos = self.centered_pos(obj)
        else:
            pos = self.offset_pos(obj)

        m = [ '.' * screen_size[0] ] * screen_size[1]

        line = m[pos[1]]
        m[pos[1]] = line[:pos[0]] + '@' + line[pos[0] + 1:]

        return m

    def centered_pos(self, obj):
        screen_size_x = obj['screen_size'][0]
        screen_size_y = obj['screen_size'][1]

        radius_x = (screen_size_x - 1) / 2
        radius_y = (screen_size_y - 1) / 2

        return (
            radius_x,
            radius_y,
        )

    def offset_pos(self, obj):
        pass

    def centered(self, obj):
        screen_size_x = obj['screen_size'][0]
        screen_size_y = obj['screen_size'][1]

        position_x = obj['character_position'][0]
        position_y = obj['character_position'][1]

        radius_x = (screen_size_x - 1) / 2
        radius_y = (screen_size_y - 1) / 2

        map_end_x = obj['map_size'][0] - 1
        map_end_y = obj['map_size'][1] - 1

        return  position_x + radius_x <= map_end_x and \
                position_y + radius_y <= map_end_y and \
                position_x - radius_x >= 0 and \
                position_y - radius_y >= 0
