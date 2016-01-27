from __future__ import generators
from pyatspi.enum import Enum
import random
import threading

def synchronized(func):
    func.__lock__ = threading.Lock()

    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return synced_func



class Action(object):
    def act(self): assert 0, 'not implemented yet'

class Draw(Action):
    def act(self):
        print self.__class__.__name__ + '.draw()'

class Erase(Action):
    def act(self):
        print self.__class__.__name__ + '.erase()'

class ShapeType(Enum):
    CIRCLE = 'Circle'
    SQUARE = 'Square'

class Shape(object):
    def draw(self): assert 0, 'not implemented yet'
    def erase(self): assert 0, 'not implemented yet'


class Circle(Shape, Draw, Erase):
    def draw(self):
        Draw.act(self)

    def erase(self):
        Erase.act(self)

class Square(Shape, Draw, Erase):
    def draw(self):
        Draw.act(self)

    def erase(self):
        Erase.act(self)


class ShapeFactory:
    shape_cache = {}

    @staticmethod
    def __create_shape(name):
        if ShapeType.CIRCLE == name:
            return Circle()
        elif ShapeType.SQUARE == name:
            return Square()
        else:
            raise name + 'is not supported'

    @staticmethod
    @synchronized
    def create_shape(shape_name):
        if not shape_name in ShapeFactory.shape_cache:
            shape = ShapeFactory.__create_shape(shape_name)
            ShapeFactory.shape_cache[shape_name] = shape

        return ShapeFactory.shape_cache[shape_name]


def generateShapeName(n):
    types = Shape.__subclasses__()
    for i in xrange(n):
        yield random.choice(types).__name__

shapes = [ShapeFactory.create_shape(name) \
          for name in generateShapeName(7)]

for shape in shapes:
    shape.draw()
    shape.erase()
    print
