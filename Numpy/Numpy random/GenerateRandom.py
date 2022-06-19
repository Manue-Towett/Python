from numpy import random

#generate random integer
randomNum =  random.randint(10)

print(randomNum)

#generate random float between 0 and 1
randomFloat = random.rand()

print(randomFloat)

#generate a 1D array of random integers of size 3
randomIntArray = random.randint(10, size=3)

print(randomIntArray)

#generate a 1D array of random floats of size 4
randomFloatArray = random.rand(4)

print(randomFloatArray)

#generate a 2D array of integers of size 4 with 3 rows
randomIntArray = random.randint(10, size=(3,4))

print(randomIntArray)

#generate 2D array of floats containing 4 rows and 5 floats each
randomFloatArray = random.rand(4,5)

print(randomFloatArray)

#generate random number from an array
randomNum = random.choice([7,8,9,4,5])

print(randomNum)

#generate 2D array from an array
randomArray = random.choice([3,4,5,6,7,2], size=(4,5))

print(randomArray)