import numpy

array1 = numpy.arange(1,4)
array2 = numpy.arange(4,7)

#finding products over both arrays
arrayProduct = numpy.prod([array1,array2])

print(arrayProduct)

#finding products of each array
arrayProducts = numpy.prod([array1,array2], axis=1)

print(arrayProducts)

#finding cumulative products
arrayCumProduct = numpy.cumprod([array1,array2])

print(arrayCumProduct)