from __future__ import generators
from pyatspi.enum import Enum
import random

class ShapeType(Enum):
    CIRCLE = 'Circle'
    SQUARE = 'Square'

class Shape(object):
    def draw(self): print 'not implemented yet'
    def erase(self): print 'not implemented yet'

    @staticmethod
    def factory(type):
        if  type == ShapeType.CIRCLE:
            return Circle()
        elif type == ShapeType.SQUARE:
            return Square()
        else:
            assert 0, 'Bad shape creation' + type

class Circle(Shape):
    def draw(self): print 'Circle.draw'
    def erase(self): print 'Circle.erase'

class Square(Shape):
    def draw(self): print 'Square.draw'
    def erase(self): print 'Square.erase'

def generateShapeName(n):
    types = Shape.__subclasses__()
    for i in xrange(n):
        yield random.choice(types).__name__

shapes = [Shape.factory(name) for name in generateShapeName(7)]

for shape in shapes:
    shape.draw()
    shape.erase()
    print
