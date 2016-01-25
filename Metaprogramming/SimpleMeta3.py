# Metaprogramming/SimpleMeta3.py

class SimpleMeta3(object):
    def __metaclass__(name, bases, nmspc):
        cls = type(name, bases, nmspc)
        cls.uses_metaclass = lambda self: 'Yes!'
        return cls

simple = SimpleMeta3()
print simple.uses_metaclass()