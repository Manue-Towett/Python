import numpy

#iterating 1D array
array1D = numpy.array([1,2,3,4])

for number in array1D:
    print(number)

#iterating 2D array
array2D = numpy.array([[1,2,3,4],[5,6,7,8]])

for element in array2D:
    for number in element:
        print(number)

#iterating 3D array
array3D = numpy.array([[[1,2,3],[4,5,6]],[[1,1,1],[2,2,2]],[[3,3,4],[6,6,7]]])

for array2d in array3D:
    for element in array2d:
        for number in element:
            print(number)

#iterating using nditer() function
print('easy iteration')
iteration = numpy.nditer(array3D)

for number in iteration:
    print(number)

#iterating array with different datatypes
#op_dtypes function is used to convert array to specific datatype
#flags=buffered creates a space for the operation to be performed
iteration = numpy.nditer(array2D, flags=['buffered'], op_dtypes='S')

for number in iteration:
    print(number)

#iterating with different step size
iteration = numpy.nditer(array2D[:,::2], flags=['buffered'], op_dtypes='S')

for number in iteration:
    print(number)

#enumerated iteration using ndenumerate
iteration = numpy.ndenumerate(array2D)

for idx, number in iteration:
    print(idx, number)