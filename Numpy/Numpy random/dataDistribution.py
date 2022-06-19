from numpy import random

#generate 1D array based on probability of occurrence
randomArray = random.choice([3,4,5,6], p=[0.2, 0.4, 0.3, 0.1], size = (100))

print(randomArray)

#generate 2D array based on probability of occurrence
randomArray = random.choice([3,4,5,6], p=[0.3,0.2,0.4,0.1],size=(3,4))

print(randomArray)