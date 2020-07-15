"""
L stands for Liskov Substitution Principle
==> If S is a subtype of T, then all objects of T in a program can be replaced by objects of S, without altering the desirable properties of program
"""

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height


    @height.setter
    def height(self, height):
        self._height = height

    def area(self):
        return self._width*self._height

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)

    @Rectangle.width.setter
    def width(self, side):
        _width = _height = side

    @Rectangle.height.setter
    def height(self, side):
        _width = _height = side


def modified_area(ob):
    w = ob.width
    ob.height = 10 # This negates the above value of w to 10
    expected_area = w * 10
    actual_area = ob.area()
    print(f"Expected Area = {expected_area} "\
          f"Actual Area = {actual_area}")

rc = Rectangle(2, 3)
modified_area(rc)

sq = Square(5)
modified_area(sq)


