import numpy

array1 = numpy.arange(3,7)
array2 = numpy. arange(8,12)

#using sum function returns the sum of all elements
arraySum = numpy.sum([array1,array2])

print(arraySum)

#summing each array independently
arraySum = numpy.sum([array1,array2],axis=1)

print(arraySum)

#cumulative sums over both arrays
arrayCumSum = numpy.cumsum([array1, array2])

print(arrayCumSum)

#cummulative sums across each array
arrayCumSum = numpy.cumsum([array1, array2],axis=1)

print(arrayCumSum)