class Screen:
    def draw(self, obj):
        center = obj['character_position']
        map_size = obj['map_size']

        x_min = max(center[0] - 5, 0)
        y_min = max(center[1] - 5, 0)
        x_max = min(center[0] + 5, map_size[0])
        y_max = min(center[1] + 5, map_size[1])

        x_size = x_max - x_min
        y_size = y_max - y_min

        m = [ '.' * x_size ] * y_size

        change = m[center[1]]
        m[center[1]] = change[:center[0]] + '@' + change[center[0] + 1:]

        print(m)

        return m
