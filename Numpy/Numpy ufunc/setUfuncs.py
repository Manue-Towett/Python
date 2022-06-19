import numpy

arrayNum = numpy.array([2,2,3,5,5,5,6,7,7,8])

#set consists of unique elements, these can be extracted as follows
arraySet = numpy.unique(arrayNum)

print(arraySet)

#finding the unique values of two arrays
arrayNum2 = numpy.array([1,2,3,4,4,6,9,9,10,11])

arraySet2 = numpy.union1d(arrayNum,arrayNum2)

print(arraySet2)

#Returning only the values that are present in both arrays
arraySet3 = numpy.intersect1d(arrayNum,arrayNum2)

print(arraySet3)

#finding the values that are in the first set but not in the second set
arraySet4 = numpy.setdiff1d(arrayNum, arrayNum2)

print(arraySet4)

#finding values that are not present in both sets
arraySet5 = numpy.setxor1d(arrayNum, arrayNum2)

print(arraySet5)