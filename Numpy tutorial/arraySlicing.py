import numpy

arrayFive = numpy.array([1,2,3,4,5,6])

#slice from index 3 to the end
print(arrayFive[3:])

#slice from index 0 to 3
print(arrayFive[:4])

#slice from index 2 to 3
print(arrayFive[2:4])

#negative indexing
print(arrayFive[-4:-1])

#using 
#JUMP 3 STEPS
print(arrayFive[1:5:3])

#slicing 2-D arrays
arrayTwoDim = numpy.array([[1,2,3,4],[5,6,7,8]])

#slicing from element 1
print(arrayTwoDim[1,:2])

#from both elements, return index 3
print(arrayTwoDim[0:4, 3])

#slice both elements
print(arrayTwoDim[0:3, 1:])