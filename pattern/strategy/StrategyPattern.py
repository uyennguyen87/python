'''
Created on Jan 28, 2016

@author: ncuyen
'''
# strategy pattern interface
class FindMinima:
    def algorithm(self, line):
        assert 0, 'not implemented yet'

class LeastSquares(FindMinima):
    def algorithm(self, line):
        return [1.1, 2.2]

class NewtonsMethod(FindMinima):
    def algorithm(self, line):
        return [3.3, 4.4]

class Bisection(FindMinima):
    def algorithm(self, line):
        return [5.5, 6.6]

class ConjugateGradient(FindMinima):
    def algorithm(self, line):
        return [3.3, 4.4]

# The "context" controls the strategy:
class MinimalSolver:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def minima(self, line):
        return self.strategy.algorithm(line)
    
    def change_algorithm(self, new_algorithm):
        self.strategy = new_algorithm

if __name__ == '__main__':
    line = [1.0, 2.0, 1.0, 2.0, 1.0, 3.0, 4.0, 5.0, 4.0]

    solver = MinimalSolver(LeastSquares())
    print solver.minima(line)
    
    solver.change_algorithm(Bisection())
    print solver.minima(line)
