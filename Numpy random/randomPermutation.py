from numpy import random
import numpy

#create an array
array1D = numpy.array([2,3,4,1,6,7])

#Permutation using shuffle method
random.shuffle(array1D)

print(array1D) #shuffle performs permutation on original array

#permutation using permutation method
permutedArray = random.permutation(array1D)

print(permutedArray)
print(array1D)