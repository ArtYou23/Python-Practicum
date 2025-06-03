class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x_1, y_1):
        self.x += x_1
        self.y += y_1

    def length(self, point):
        ln = round((abs(self.x - point.x) ** 2 + abs(self.y - point.y) ** 2) ** 0.5, 2)
        return ln


class PatchedPoint(Point):

    def __init__(self, *args):
        match len(args):
            case 0:
                super().__init__(0, 0)
            case 1:
                super().__init__(*args[0])
            case 2:
                super().__init__(*args)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'PatchedPoint({self.x}, {self.y})'