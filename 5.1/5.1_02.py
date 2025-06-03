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