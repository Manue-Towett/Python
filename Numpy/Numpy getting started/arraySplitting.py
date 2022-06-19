import numpy

array1D = numpy.array([1,2,3,4,5,6,])

#splitting array into 3 parts
newArray = numpy.array_split(array1D, 3)

print(newArray)

#array splitting into 4 parts. it adjust accordingly
newArray = numpy.array_split(array1D, 4)

print(newArray)

#splitting 2D arrays
array2D = numpy.array([[1,2,3],[4,5,6],[7,8,9],[2,4,7]])

newArray = numpy.array_split(array2D, 2)

print(newArray)

#alternate solution for splitting
#newArray = numpy.hsplit(array2D, 2)

print(newArray)