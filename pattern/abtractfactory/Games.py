'''
Created on Jan 28, 2016

@author: ncuyen
'''
class Obstacle:
    def action(self): pass

class Character:
    def interact_with(self, obstacle): pass

class Kitty(Character):
    def interact_with(self, obstacle):
        print 'Kitty has encountered a',
        obstacle.action()

class KungFuGuy(Character):
    def interact_with(self, obstacle):
        print 'KungFuGuy now battles a',
        obstacle.action()

class Puzzle(Obstacle):
    def action(self):
        print 'Puzzle'

class NastyWeapon(Obstacle):
    def action(self):
        print 'NastyWeapon'

# Abstract factory
class GameElementFacotry:
    def makeCharacter(self): pass
    def makeObstacle(self): pass

# Concrete factories
class KititesAndPuzzles(GameElementFacotry):
    def makeCharacter(self): return Kitty()
    def makeObstacle(self): return Puzzle()

class KillAndDismember(GameElementFacotry):
    def makeCharacter(self): return KungFuGuy()
    def makeObstacle(self): return NastyWeapon()

class GameEnvirontment:
    def __init__(self, factory):
        self.factory = factory
        self.character = factory.makeCharacter()
        self.obstacle = factory.makeObstacle()
    
    def play(self):
        self.character.interact_with(self.obstacle)

if __name__ == '__main__':
    game1 = GameEnvirontment(KititesAndPuzzles())
    game2 = GameEnvirontment(KillAndDismember())
    
    game1.play()
    game2.play()