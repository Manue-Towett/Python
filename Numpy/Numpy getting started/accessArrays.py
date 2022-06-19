import numpy

#accessing 1-D arrays
arrayOne = numpy.array([1,2,3])

print(arrayOne[2])

print(arrayOne[0]+arrayOne[2])

#accessing 2-D arrays
arrayTwo = numpy.array([[1,2,3],[3,4,5]])

print(arrayTwo[0, 2])

print(arrayTwo[1,0]+arrayTwo[1,2])

#accessing 3-D arrays
arrayThree = numpy.array([[[1,2,3],[4,5,6]],[[7,8,9],[4,7,6]]])

print(arrayThree[1,0,2])

print(arrayThree[0,0,2] + arrayThree[1,1,1])

#using negative indexing to access the last element
print(arrayThree[1,0,-1])