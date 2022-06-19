import numpy

arrayNum = numpy.array([-3.2455, 9.8765, 5.4567])

#truncation removes all decimals
arrayTruncated = numpy.trunc(arrayNum)

print(arrayTruncated)

#Fixing: same as trunc
arrayFixed = numpy.fix(arrayNum)

print(arrayFixed)

#Rounding: if second argument is not supplied it rounds off to the nearest integer
arrayRounded = numpy.around(arrayNum,1)

print(arrayRounded)

#Floor and ceiling functions
arrayFloor = numpy.floor(arrayNum)
arrayCeil = numpy.ceil(arrayNum)

print(arrayCeil, arrayFloor)