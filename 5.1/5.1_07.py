class Rectangle:

    def __init__(self, corner1, corner2):
        self.x, self.y = round(min(corner1[0], corner2[0]), 2), round(min(corner1[1], corner2[1]), 2)
        self.width, self.height = round(abs(corner1[0] - corner2[0]), 2), round(abs(corner1[1] - corner2[1]), 2)

    def perimeter(self):
        return round((self.width + self.height) * 2, 2)

    def area(self):
        return round(self.width * self.height, 2)

    def get_pos(self):
        return self.x, self.y + self.height

    def get_size(self):
        return self.width, self.height

    def move(self, dx, dy):
        self.x, self.y = round(self.x + dx, 2), round(self.y + dy, 2)

    def resize(self, width, height):
        self.width, self.height = round(width, 2), round(height, 2)

    def turn(self):
        cx, cy = self.x + self.width / 2, self.y + self.height / 2
        self.width, self.height = self.height, self.width
        self.x, self.y = round(cx - self.width / 2, 2), round(cy - self.height / 2, 2)

    def scale(self, ratio):
        cx, cy = self.x + self.width / 2, self.y + self.height / 2
        self.width, self.height = round(self.width * ratio, 2), round(self.height * ratio, 2)
        self.x, self.y = round(cx - self.width / 2, 2), round(cy - self.height / 2, 2)