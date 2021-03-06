class Screen:
    def draw(self, map_size, screen_size, selected_point):
        pos = self._getFakeCenter(map_size, screen_size, selected_point)

        screen_size_x = screen_size[0]
        screen_size_y = screen_size[1]

        radius_x = (screen_size_x - 1) / 2
        radius_y = (screen_size_y - 1) / 2

        x_offset = 1
        y_offset = 1

        if screen_size_x % 2 == 0:
            x_offset += 1

        if screen_size_y % 2 == 0:
            y_offset += 1

        indices_x = range(pos[0] - radius_x, pos[0] + radius_x + x_offset)
        indices_y = range(pos[1] - radius_y, pos[1] + radius_y + y_offset)

        return [[ (x, y) for x in indices_x ] for y in indices_y ]

    def _getFakeCenter(self, m, screen, point):
        map_x    = m[0] - 1
        map_y    = m[1] - 1

        screen_x = screen[0]
        screen_y = screen[1]

        radius_x = (screen_x - 1) / 2
        radius_y = (screen_y - 1) / 2

        point_x = point[0]
        point_y = point[1]

        offset_x = 0
        offset_y = 0

        if screen_x % 2 == 0:
            offset_x += 1

        if screen_x % 2 == 0:
            offset_y += 1

        if point_x + radius_x + offset_x <= map_x and \
           point_y + radius_y + offset_y <= map_y and \
           point_x - radius_x >= 0 and \
           point_y - radius_y >= 0:
            return point

        fake_x = sorted([0 + radius_x, point_x, map_x - radius_x - offset_x])[1]
        fake_y = sorted([0 + radius_y, point_y, map_y - radius_y - offset_y])[1]

        return [fake_x, fake_y]
