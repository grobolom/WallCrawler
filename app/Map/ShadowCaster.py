class ShadowCaster:
    def getShadowMap(self, octet):
        height = len(octet)
        width = len(octet[0])

        result = [[
            ' ' for col in range(width) ]
                for row in range(height) ]

        for x in range(width):
            for y in range(height):
                if octet[y][x] == ' ':
                    result[y][x] = ' '
                    continue
                result[y][x] = 'x'

        print( [ ''.join(row) for row in result ] )
        return [ ''.join(row) for row in result ]
