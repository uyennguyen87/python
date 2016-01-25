from functools import wraps

from MyUtils import PrintUtils

class decorator_with_arguments(object):
    def __init__(self, arg1, arg2, arg3):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        PrintUtils.green("Inside __init__()")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        PrintUtils.green("Inside __call__()")

        @wraps(f)
        def wrapped_f(*args):
            PrintUtils.green("Inside wrapped_f()")
            print 'Decorator arguments: ', self.arg1, self.arg2, self.arg3
            f(*args)
            PrintUtils.green("After f(*args)")
        return wrapped_f

@decorator_with_arguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print 'sayHello arguments', a1, a2, a3, a4

PrintUtils.blue('After decorator')
print

PrintUtils.blue('Preaparing to call sayHello()')
sayHello("say", "hello", "argument", "list")
print

PrintUtils.blue('after first sayHello() call')
sayHello("a", "different", "set of", "arguments")
print

PrintUtils.blue("after second sayHello() call")

# more simple
def decorator_function_with_arguments(arg1, arg2, arg3):
    def wrap(f):
        print("Inside wrap()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", arg1, arg2, arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f
    return wrap

@decorator_function_with_arguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print 'sayHello arguments', a1, a2, a3, a4

PrintUtils.blue('After decorator')
print

PrintUtils.blue('Preaparing to call sayHello()')
sayHello("say", "hello", "argument", "list")
print

PrintUtils.blue('after first sayHello() call')
sayHello("a", "different", "set of", "arguments")
print

PrintUtils.blue("after second sayHello() call")