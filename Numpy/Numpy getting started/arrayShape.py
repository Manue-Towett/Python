import numpy

array2D = numpy.array([[4,4,4,6,6,7,7],[3,3,4,4,4,45,5]])

#get the shape of 2D array
print(array2D.shape)

array5D = numpy.array([1,2,3,4], ndmin=5)

#get shape of 5D array
print(array5D.shape)

#change the shape of an array from 1D to 2D
newArray = array5D.reshape(2,2)

print(newArray.shape)
print(newArray)

#chaneg the shape of an array from 2D to 1D
oneDimArray = array2D.reshape(-1)

print(oneDimArray)
print(oneDimArray.shape)

#reshaping 1D to 3D
array1D = numpy.array([1,2,3,4,5,6,7,8,9,10,11,12])

array3D = array1D.reshape(2,3,-1) #negative one is for unknown dimension to allow python to autocalculate

print(array3D)

#check if it is a copy or view array
print(array3D.base) #it's a view array