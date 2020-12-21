class Road:
    def __init__(self, _length, _width):
        self.thickness = 5
        self.calculated_weight = 25
        self._length = _length
        self._width = _width

    def massa(self):
        return round(self._length * self._width * self.thickness * self.calculated_weight / 1000)


m = Road(20, 5000)
print(f'Масса асфальта составит: {m.massa()} т.')
