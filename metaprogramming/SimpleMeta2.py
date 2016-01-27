# Metaprogramming/SimpleMeta2.py

class SimpleMeta2(object):
    class __metaclass__(type):
        def __init__(cls, name, bases, nmspc):
            type.__init__(cls, name, bases, nmspc)
            cls.uses_metaclass = lambda self: 'Yes!'

simple = SimpleMeta2()
print simple.uses_metaclass()

