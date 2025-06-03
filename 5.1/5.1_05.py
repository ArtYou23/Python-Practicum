class Rectangle:

    def __init__(self, p_1, p_2):
        self.p_1 = p_1
        self.p_2 = p_2

    def perimeter(self):
        return round((abs(self.p_1[0] - self.p_2[0]) + abs(self.p_1[1] - self.p_2[1])) * 2, 2)

    def area(self):
        return round((abs(self.p_1[0] - self.p_2[0]) * abs(self.p_1[1] - self.p_2[1])), 2)