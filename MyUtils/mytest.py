from itertools import izip

fruits = [('orange','green'), ('lemon', 'yellow'), ('apple', 'red')]
weights = [1.5, 1.3, 1.7, 2.0]

for ((fruit, color), weight) in izip(fruits, weights):
    print 'a', color, fruit, 'has weight: ', weight, 'g'