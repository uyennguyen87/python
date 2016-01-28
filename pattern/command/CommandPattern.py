'''
Created on Jan 28, 2016

@author: ncuyen
'''
class Command:
    def execute(self): pass

class Loony(Command):
    def execute(self):
        print "You're a loony."

class NewBrain(Command):
    def execute(self):
        print "You might even need a new brain."

class Afford(Command):
    def execute(self):
        print "I couldn't afford a whole new brain."

# A object that holds commands:
class Macro:
    def __init__(self):
        self.commands = []
        
    def add(self, command):
        self.commands.append(command)
    
    def run(self):
        for command in self.commands:
            command.execute()

if __name__ == '__main__':
    macro = Macro()
    macro.add(Loony())
    macro.add(NewBrain())
    macro.add(Afford())
    macro.run()
