import numpy

array1D =  numpy.array([5,3,8,6])

#filtering 5 and 6
filterOrder = [True, False, False, True]

filteredArray = array1D[filterOrder]

print(filteredArray)

#filtering even numbers
filterOrder = []

for element in array1D:
    if element % 2 == 0:
        filterOrder.append(True)
    else:
        filterOrder.append(False)

filteredArray = array1D[filterOrder]

print(filteredArray)

#creating filter array directly
filterOrder = array1D>4

filteredArray = array1D[filterOrder]

print(filteredArray)