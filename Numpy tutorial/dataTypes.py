import numpy

arrayNum = numpy.array([1,2,3,4])
arrayStr = numpy.array(['apple', 'orange', 'banana'])

#checking data type
print(arrayNum.dtype)
print(arrayStr.dtype)

#creating an array with a specified datatype
arrayNum2 = numpy.array([1,3,4], dtype='S')

print(arrayNum2)
print(arrayNum2.dtype)

#creating an array with 4bytes integer
arrayNum3 = numpy.array([1,2,3,4], dtype='i4')

print(arrayNum3)
print(arrayNum3.dtype)

#changing datatype from float to integer
arrayFloat = numpy.array([1.2,3.2,4.6])

arrayFloatToInt = arrayFloat.astype('i')

print(arrayFloatToInt)
print (arrayFloatToInt.dtype)

#changing datatype form integer to boolean
arrayInt = numpy.array([1,2,0,0])

arrayIntToBool = arrayInt.astype(bool)

print(arrayIntToBool)

print(arrayIntToBool.dtype)