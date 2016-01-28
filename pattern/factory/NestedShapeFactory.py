from __future__ import generators
from pyatspi.enum import Enum
import random

class ShapeType(Enum):
    CIRCLE = 'Circle'
    SQUARE = 'Square'

class Shape(object):
    def draw(self): print 'not implemented yet'
    def erase(self): print 'not implemented yet'

def factory(shape_type):
    class Circle(Shape):
        def draw(self): print 'Circle.draw'
        def erase(self): print 'Circle.erase'

    class Square(Shape):
        def draw(self): print 'Square.draw'
        def erase(self): print 'Square.erase'

    if  shape_type == ShapeType.CIRCLE:
        return Circle()
    elif shape_type == ShapeType.SQUARE:
        return Square()
    else:
        assert 0, 'Bad shape creation' + shape_type


def generateShapeName(n):
    all_shape_names = ['Circle', 'Square']
    for i in xrange(n):
        yield random.choice(all_shape_names)

shapes = [factory(name) for name in generateShapeName(7)]

for shape in shapes:
    shape.draw()
    shape.erase()
    print