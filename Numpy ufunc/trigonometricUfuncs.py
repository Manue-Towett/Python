import numpy

#sine iof a number
sineNum = numpy.sin(numpy.pi/2)
sineNum2 = numpy.sin(3/2)

print(sineNum, sineNum2)

#array of sine
arrayNum = numpy.array([0.52359878, 1.04719755, 1.57079633, 2.0943951])

arrayDeg = numpy.rad2deg(arrayNum)

arraySine = numpy.sin(arrayNum)

print(arraySine, arrayDeg)

#Cosine of a number
cosNum = numpy.cos(60*numpy.pi/180) #cosine of 90 degrees

print(cosNum)

#Cosine of an array
arrayNum = numpy.array([0,30,60,90,120,150,180])

arrayRad = numpy.deg2rad(arrayNum)

cosArray = numpy.cos(arrayRad)

print(cosArray)

#tan of an array
tanArray = numpy.tan(arrayRad)

print(tanArray)

#finding angles from a sines, cosines and tangents in radians
angleRadTan = numpy.arctan(tanArray)
angleRadCos = numpy.arccos(cosArray)
angleRadSin = numpy.arcsin(arraySine)

print(angleRadCos, angleRadSin, angleRadTan)

#converting radians to degrees
angleDegCos = numpy.rad2deg(angleRadCos)
angleDegTan = numpy.rad2deg(angleRadTan)
angleDegSin = numpy.rad2deg(angleRadSin)

print(angleDegSin, angleDegCos, angleDegTan)

#finding hypotenuse
baseNum = 6
height = 12

hypotenuse = numpy.hypot(baseNum, height)

print(hypotenuse)