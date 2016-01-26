# Metaprogramming/SingletonDecorator.py

def singleton(_class):
    "Simple replacement of object creation operation"
    def get_instance(*args, **kwargs):
        if not hasattr(_class, 'instance'):
            _class.instance = _class(*args, **kwargs)
        return _class.instance
    return get_instance


def singleton(_class):
    """
    More powerful approach: Change the behavior
    of the instances AND the class object
    """
    class Decorated(_class):
        def __init__(self, *args, **kwargs):
            if hasattr(_class, '__init__'):
                _class.__init__(self, *args, **kwargs)

        def __repr__(self): return _class.__name__ + " obj"

        __str__ = __repr__

    Decorated.__name__ = _class.__name__

    class ClassObject:
        def __init__(cls):
            cls.instance = None

        def __repr__(cls):
            return _class.__name__

        __str__ = __repr__

        def __call__(cls, *args, **kwargs):
            print str(cls) + " __call__"

            if not cls.instance:
                cls.instance = Decorated(*args, **kwargs)

            return cls.instance

    return ClassObject()


@singleton
class ASingleton: pass

a = ASingleton()
b = ASingleton()
print a, b
print a.__class__.__name__
print ASingleton
assert a is b

@singleton
class BSingleton:
    def __init__(self, x):
        self.x =  x

c = BSingleton(11)
d = BSingleton(12)
assert c is d
assert c is not a
