import numpy

num1 = 68
num2 = 96

#finding LCM
lcmNum = numpy.lcm(num1,num2)

print(lcmNum)

#using reduce() function to find lcm of arrays
array1 = numpy.arange(1,8)

lcmArray = numpy.lcm.reduce(array1)

print(lcmArray)