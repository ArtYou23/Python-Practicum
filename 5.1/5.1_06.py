class Rectangle:

    def __init__(self, corner_1, corner_2):
        self.left_up = [min(corner_1[0], corner_2[0]), max(corner_1[1], corner_2[1])]
        self.right_down = [max(corner_1[0], corner_2[0]), min(corner_1[1], corner_2[1])]
        self.width = round(abs(self.left_up[0] - self.right_down[0]), 2)
        self.height = round(abs(self.left_up[1] - self.right_down[1]), 2)

    def perimeter(self):
        return round((self.width + self. height) * 2, 2)

    def area(self):
        return round(self.width * self. height, 2)

    def get_pos(self):
        return self.left_up[0], self.left_up[1]

    def get_size(self):
        return self.width, self.height

    def move(self, dx, dy):
        self.left_up = round(self.left_up[0] + dx, 2), round(self.left_up[1] + dy, 2)
        self.right_down = round(self.right_down[0] + dx, 2), round(self.right_down[1] + dy, 2)

    def resize(self, width, height):
        self.width = width
        self.height = height