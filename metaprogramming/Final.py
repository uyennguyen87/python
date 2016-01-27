# Metaprogramming/Final.py
# Emulating Java's 'final'

class final(type):
    def __init__(cls, name, bases, namespace):
        super(final, cls).__init__(name, bases, namespace)
        for _class in bases:
            if isinstance(_class, final):
                raise TypeError(str(_class.__name__) + " is final")

class A(object):
    pass

class B(A):
    __metaclass__ = final

print B.__base__
print isinstance(B, final)


# Produces compile-time error:
class C(B):
    pass