# Metaprogramming/NewVSInit.py
from pprint import pprint


class Tag1: pass
class Tag2: pass
class Tag3:
    def tag3_method(self): pass

class MetaBase(type):
    def __new__(cls, name, bases, namespace):
        print 'MetaBase.__new__\n'
        return super(MetaBase, cls).__new__(cls, name, bases, namespace)

    def __init__(cls, name, bases, namespace):
        print 'MetaBase.__init__\n'
        super(MetaBase, cls).__init__(name, bases, namespace)

class MetaNewVSInit(MetaBase):
    def __new__(cls, name, bases, namespace):
        # First argument is the metaclass: ``MetaNewVSInit``
        print 'MetaNewVsInit.__new__'
        for x in (cls, name, bases, namespace):
            pprint(x)
        print ''

        # These all work because the class hasn't been created yet
        if 'foo' in namespace: namespace.pop('foo')

        name += '_x'
        bases += (Tag1,)
        namespace['baz'] = 42

        return super(MetaNewVSInit, cls).__new__(cls, name, bases, namespace)

    def __init__(cls, name, bases, namespace):
        # First argument is the class being initialized
        print 'MetaNewVSInit.__init__'
        for x in (cls, name, bases, namespace): print(x)
        print ''

        if 'bar' in namespace: namespace.pop('bar') # No effect

        name += '_y' # No effect
        bases += (Tag2, ) # No effect
        namespace['pi'] = 3.14159 # No effect

        super(MetaNewVSInit, cls).__init__(name, bases, namespace)

        # There do work because they operate on the class object:
        cls.__name__ += 'z'
        cls.__bases__ += (Tag3,)
        cls.e = 2.718

class Test(object):
    __metaclass__ = MetaNewVSInit
    def __init__(self):
        print 'Test.__init__'
    def foo(self): print 'foo still here'
    def bar(self): print 'bar still here'

t = Test()
print 'class name: %s' % Test.__name__
print 'base classes:', [c.__name__ for c in Test.__bases__]
print [m for m in dir(t) if not m.startswith('__')]
t.bar()
print t.e