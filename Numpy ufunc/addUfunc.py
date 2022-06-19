import numpy

array1, array2, arrayResult = [1,2,3],[4,5,6],[]

#To sum them using iterating functions, we do as follows
for elementInArray1, elementInArray2 in zip(array1,array2):
    arrayResult.append(elementInArray1+elementInArray2)

print(arrayResult)

#summing using ufuncs
arrayResult = numpy.add(array1,array2)

print(arrayResult)