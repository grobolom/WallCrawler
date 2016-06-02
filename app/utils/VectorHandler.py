class VectorHandler:
    """
    this class if for handling vectors, especially in making maps.
    """
    def getPositiveVectors(self, v1, v2):
        """
        this is used in making rooms - it's easy to generate a room start
        point and a random vector representing the size but for ease of use we
        would rather both the position AND the size be positive
        """

        x1 = v1[0]
        x2 = v2[0]

        y1 = v1[1]
        y2 = v2[1]

        if x2 < 0:
            x1 = x1 + x2
            x2 = abs(x2)

        if y2 < 0:
            y1 = y1 + y2
            y2 = abs(y2)

        return ([x1, y1], [x2, y2])
  
