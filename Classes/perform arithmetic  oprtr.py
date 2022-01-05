class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"x = {self.x}, y = {str.y}"


point1 = point(10, 20)
point2 = point(1, 2)

print(point1 + point2)
