import numpy

array1 = numpy.array([10,15,20])

#finding the gcd of elements in the array
numGCD = numpy.gcd(array1[0], array1[1])

print(numGCD)

#finding the gcd of an array
arrayGCD = numpy.gcd.reduce(array1)

print(arrayGCD)