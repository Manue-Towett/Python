from numpy import random
import matplotlib.pyplot as plt
import seaborn

#generate rayleigh distribution
rayleighDist = random.rayleigh(scale=3, size=(3,4))

print(rayleighDist)

seaborn.distplot(rayleighDist)

plt.show()