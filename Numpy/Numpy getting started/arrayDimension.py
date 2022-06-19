import numpy

zeroDimension = numpy.array(42)
oneDimension = numpy.array([1,2,3])
twoDimension = numpy.array([[1,2,3],[4,5,6]])
threeDimesion = numpy.array([[[1,2,2],[4,5,5]],[[7,8,9],[3,4,5]]])

print(zeroDimension)
print(oneDimension)
print(twoDimension)
print(threeDimesion)

#checking number of dimensions
print(oneDimension.ndim)
print(zeroDimension.ndim)
print(twoDimension.ndim)
print(threeDimesion.ndim)

#Higher dimensional arrays
arrayHigherDimension = numpy.array([1,2,3], ndmin=5)

print(arrayHigherDimension)

print(arrayHigherDimension.ndim)