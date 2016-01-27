# StateMachine/MouseTrap1/MouseTrapTest.py
# State Machine pattern using 'if' statements
# to determine the next state
import string

from pattern.state.State import State
from pattern.state.StateMachine import StateMachine
from pattern.state.mouse.MouseAction import MouseAction


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
        StateMachine.__init__(self, MouseTrap.waiting)


# Static variable initialization
MouseTrap.waiting = Waiting()
MouseTrap.luring = Luring()
MouseTrap.trapping = Trapping()
MouseTrap.holding = Holding()


with open("../mouse/MouseMoves.txt") as file:
    moves = map(string.strip, file.readlines())
    mouse_actions = map(MouseAction, moves)
    MouseTrap().runAll(mouse_actions)
