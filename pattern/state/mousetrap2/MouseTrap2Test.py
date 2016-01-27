# A better mousetrap using tables
import string

from pattern.state.State import State
from pattern.state.StateMachine import StateMachine
from pattern.state.mouse.MouseAction import MouseAction


class StateT(State):
    def __init__(self):
        self.transitions = None

    def next(self, input):
        if input in self.transitions:
            return self.transitions[input]
        else:
            raise "input not supported for current state"

class Waiting(StateT):
    def run(self):
        print "Waiting: Broadcasting cheese smell"

    def next(self, input):
        # Lazy initialization
        if not self.transitions:
            self.transitions = {
                MouseAction.appears: MouseTrap.luring
            }
        return StateT.next(self, input)

class Luring(StateT):
    def run(self):
        print 'Luring: Presenting Cheese, door open'

    def next(self, input):
        # Lazy initialization:
        if not self.transitions:
            self.transitions = {
                MouseAction.enters: MouseTrap.trapping,
                MouseAction.runsAway: MouseTrap.waiting
            }

        return StateT.next(self, input)

class Trapping(StateT):
    def run(self):
        print "Trapping: Closing door"

    def next(self, input):
        if not self.transitions:
            self.transitions = {
                MouseAction.escapes: MouseTrap.waiting,
                MouseAction.trapped: MouseTrap.holding
            }
        return StateT.next(self, input)


class Holding(StateT):
    def run(self):
        print 'Holding: Mouse caught'
    def next(self, input):
        if not self.transitions:
            self.transitions = {
                MouseAction.removed: MouseTrap.waiting
            }
        return StateT.next(self, input)

class MouseTrap(StateMachine):
    def __init__(self):
        StateMachine.__init__(self, MouseTrap.waiting)


MouseTrap.waiting = Waiting()
MouseTrap.luring = Luring()
MouseTrap.trapping = Trapping()
MouseTrap.holding = Holding()

with open('../mouse/MouseMoves.txt') as file:
    moves = map(string.strip, file.readlines())
    mouse_actions = map(MouseAction, moves)
    MouseTrap().runAll(mouse_actions)
