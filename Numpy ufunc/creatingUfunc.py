import numpy

#normal python function
def name(firstName, lastName):
    return (firstName, lastName)

#converting to a ufunc
sayName = numpy.frompyfunc(name, 2, 1)

print(sayName('Manue', 'Towett'))

print(type(sayName))