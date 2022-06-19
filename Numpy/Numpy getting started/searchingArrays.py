import numpy

array2D = numpy.array([[1,2,3,4,5,6],[9,8,7,6,5,4]])

#find number 4
findElementFour = numpy.where(array2D==4)

print(findElementFour)

#find even numbers
findEven = numpy.where(array2D%2==0)

print(findEven)

#searchsorted() returns the index where the number will be placed to maintain search order
array1D = numpy.array([2,4,5,6,7])
searchSort = numpy.searchsorted(array1D, 3)

print(searchSort)

#searchsorted() multiple items
searchSort = numpy.searchsorted(array1D, (3,5,6))

print(searchSort)