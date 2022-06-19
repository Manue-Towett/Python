import numpy

arrayOriginal = numpy.array([2,2,2,2,2])

#copy
copiedArray = arrayOriginal.copy()
arrayOriginal[2] = 5

print(copiedArray)#changes to original array doesn't affect copied array
print(arrayOriginal)

#view
viewArray = arrayOriginal.view()
arrayOriginal[0] = 7

print(arrayOriginal)
print(viewArray) #changes to original array affects the view array

#checking if an array owns its data
print(arrayOriginal.base)
print(copiedArray.base)
print(viewArray.base)