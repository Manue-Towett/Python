import numpy

#defining two numpy arrays
array1 = numpy.array([2,3,4,5,6,7])
array2 = numpy.array([3,5,7,8,2,5])

#addition in ufuncs
arraySum = numpy.add(array1,array2)

print(arraySum)

#subtraction in ufuncs
arrayDifference = numpy.subtract(array1,array2)

print(arrayDifference)

#multiplication in ufuncs
arrayProduct = numpy.multiply(array1,array2)

print(arrayProduct)

#Division in ufuncs
arrayDiv = numpy.divide(array1,array2)

print(arrayDiv)

#Raising the first array to the power of the second array
arrayRaisedToPower = numpy.power(array1,array2)

print(arrayRaisedToPower)

#returning remainders of division as arrays
arrayRemainder = numpy.remainder(array1,array2)
arrayRemain = numpy.mod(array1, array2)

print(arrayRemain, arrayRemainder)

#Quotient and mod
arrayDivMod = numpy.divmod(array1, array2)

print(arrayDivMod) #returns two arrays: first for integers and second for remainders resulting from division

#absolute values
arrayAbsolute = numpy.absolute(arrayDifference)
arrayAbs = numpy.abs(arrayDifference) #both functions return absolute value arrays

print(arrayAbs, arrayAbsolute)