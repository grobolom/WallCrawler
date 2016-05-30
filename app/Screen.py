class Screen:
    def draw(self, obj):
        return [
            '@' + '.' * 4,
        ] + ['.' * 5] * 4
