class Road:


    def __init__(self, length, width):
        self._length, self._width = length, width


    def get_weight(self, depth, gravity):
        try:
            return self._length * self._width * depth * gravity
        except Exception:
            raise ValueError('Params incorrect!')

if __name__ == '__main__':
    road = Road(5000, 20)
    print(f'{road.get_weight(5, 1.5)} tonnes')