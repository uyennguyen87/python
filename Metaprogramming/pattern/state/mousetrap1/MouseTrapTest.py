# StateMachine/MouseTrap1/MouseTrapTest.py
# State Machine pattern using 'if' statements
# to determine the next state
import string
import sys

sys.path += ['../state', '../mouse']

from Metaprogramming.pattern.state import State, StateMachine
from Metaprogramming.pattern.state.mouse import MouseAction


# A different subclass for each state:
class Waiting(State):
    def run(self):
        print 'Waiting: Broadcasting cheese smell'

    def next(self, input):
        if input == MouseAction.appears:
            return MouseTrap.luring
        return MouseTrap.waiting

class Luring(State):
    def run(self):
        print 'Lurring: Presenting Cheese, door open'

    def next(self, input):
        if input == MouseAction.runsAway:
            return MouseTrap.waiting
        elif input == MouseAction.enters:
            return MouseTrap.trapping
        else:
            return MouseTrap.luring

class Trapping(State):
    def run(self):
        print 'Trapping: Closing door'

    def next(self, input):
        if input == MouseAction.escapes:
            return MouseTrap.waiting
        elif input == MouseAction.trapped:
            return MouseTrap.holding
        else:
            return MouseAction.trapping

class Holding(State):
    def run(self):
        print 'Holding: Mouse caught'

    def next(self, input):
        if input == MouseAction.removed:
            return MouseTrap.waiting
        return MouseTrap.holding

class MouseTrap(StateMachine):
    def __init__(self):
        super(StateMachine, self).__init__(self, MouseTrap.waiting)


# Static variable initialization
MouseTrap.waiting = Waiting()
MouseTrap.luring = Luring()
MouseTrap.trapping = Trapping()
MouseTrap.holding = Holding()

moves = map(string.strip,
            open("../Mouse/MouseMoves.txt").readlines())

MouseTrap().runAll(map(MouseAction, moves))