import numpy

#joining 1D arrays
array1 = numpy.array([1,2,3])
array2 = numpy.array([4,5,5])
array3 = numpy.array([7,8,9])

finalArray = numpy.concatenate((array1, array2, array3))

print(finalArray)

#joining 2D  along rows
array2D1 = numpy.array([[1,2],[3,4]])
array2D2 = numpy.array([[5,6],[7,8]])

final2Darray = numpy.concatenate((array2D1,array2D2), axis=1)

print(final2Darray)

#joining arrays using stack() function axis=0
stackedArray = numpy.stack((array1,array2))

print(stackedArray)

#axis=1
stackedArray = numpy.stack((array2,array3), axis=1)

print(stackedArray)

#stacking along rows hstack()
stackedArray = numpy.hstack((array1,array2))

print(stackedArray)

#stacking along columns
stackedArray = numpy.vstack((array1, array2))

print(stackedArray)

#stacking along height
stackedArray = numpy.dstack((array1, array2))

print(stackedArray)