from math import log
import numpy

#arrange function below returns an array starting for 2 to 6 
arrayNum = numpy.arange(2,7)

#finding log to base 10
arrayLog = numpy.log10(arrayNum)

print(arrayLog)

#log to base 2
arrayLog2 = numpy.log2(arrayNum)

print(arrayLog2)

#Natural logs
arrayNaturalLog = numpy.log(arrayNum)

print(arrayNaturalLog)

#log to any base
arrayLog3 = numpy.frompyfunc(log, 2, 1)

print(arrayLog3(arrayNum, 3))