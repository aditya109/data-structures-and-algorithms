"""
O stands for Open-Closed Principle
==> A class which tested and deployed should always be extended and not modified.
"""

from enum import Enum
from abc import abstractmethod, ABC


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
"""
This is bad... Cuz each time we get a new requirement we modify the origin class.
Also we have to preserve the S of Solid principle. 
"""
class NormalFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size ):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_color_and_size(self, products, color, size):
        for p in products:
            if p.color == color and p.size == size:
                yield p

"""
Solution: using Enterprise Design Pattern
"""
class Specification(ABC):
    def is_satisfied(self, item):
        """
        should return true if condition is satisfied else returns false
        :param item:
        :type item:
        :return: boolean output
        :rtype:  bool
        """
        pass

class Filter(ABC):
    def filter(self, items, spec):  pass

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


if __name__ == '__main__':
    A = Product("A", Color.RED, Size.SMALL)
    B = Product("B", Color.GREEN, Size.SMALL)
    C = Product("C", Color.RED, Size.SMALL)

    products = [A, B, C]

    # pf = NormalFilter()
    # for p in pf.filter_by_color(products=products, color=Color.RED):
    #     print(f"{p.name} is RED")
    # for p in pf.filter_by_size(products=products, size=Size.SMALL):
    #     print(f"{p.name} is SMALL")
    #

    bf = BetterFilter()
    green = ColorSpecification(Color.GREEN)
    small = ColorSpecification(Size.SMALL)

    for p in bf.filter(products, green):
        print(f"{p.name} is GREEN")

