from numpy import random
import matplotlib.pyplot as plt
import seaborn

#generate normal distribution
normalDist = random.normal(size=(2,3))

print(normalDist)

#generate random normal distribution with mean at 2 and standard deviation 4
normalDist = random.normal(loc=3, scale=4, size=(5,6))

print(normalDist)

seaborn.distplot(normalDist)

plt.show()