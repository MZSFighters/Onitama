from matplotlib import pyplot
from numpy.random import random
matrix = random((5,5))

from matplotlib import cm
pyplot.imshow(matrix, interpolation='nearest', cmap=cm.Blues)
pyplot.scatter([6,8], [10,7], color='red', s=40)
pyplot.show()