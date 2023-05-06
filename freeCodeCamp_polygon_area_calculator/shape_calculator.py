
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        a = self.width * self.height
        return a

    def get_perimeter(self):
        p = 2 * self.width + 2 * self.height
        return p

    def get_diagonal(self):
        d = (self.width ** 2 + self.height ** 2) ** .5
        return d

    def get_picture(self):
        output = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for i in range(self.height):
            for j in range(self.width):
                output += "*"
            output += "\n"
        return output

    def get_amount_inside(self, shape):
        amount = self.get_area() // shape.get_area()
        return amount

    def __str__(self):
        out = f"Rectangle(width={self.width}, height={self.height})"
        return out


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"


