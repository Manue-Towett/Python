import numpy

array1 = numpy.arange(1,7)

#Discrete differences
arrayDiff = numpy.diff(array1)

print(arrayDiff)

#Discrete differences calculation twice
array1 = numpy.array([20,25,49,67])
arrayDiffTwice = numpy.diff(array1, n=2)

print(arrayDiffTwice)