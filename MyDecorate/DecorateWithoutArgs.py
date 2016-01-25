from MyUtils import PrintUtils

class decorate_without_arguments(object):
    def __init__(self, f):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        PrintUtils.green("Inside __init__()")
        self.f = f

    def __call__(self, *args):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        print
        PrintUtils.green("Inside __call__()")
        self.f(*args)
        PrintUtils.green("After self.f(*args)")
        print

@decorate_without_arguments
def sayHello(a1, a2, a3, a4):
    print 'say Hello arguments: ', a1, a2, a3, a4


PrintUtils.blue('After decoration')
print

PrintUtils.blue('Preparing to call sayHello()')
sayHello('say', 'hello', 'argument', 'list')

PrintUtils.blue('After first sayHello() call')
sayHello('a', 'different','set of', 'arguments')

print
PrintUtils.blue('After second sayHello() call')
