class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width


class MassOfAsphalt(Road):
    def __init__(self, _length, _width, thickness):
        super().__init__(_length, _width)
        self.thickness = thickness

    def mas_of_as(self):
        return self._length * self._width * self.thickness

result = MassOfAsphalt(25, 10000, 125)
print(result.mas_of_as())
