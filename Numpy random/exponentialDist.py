from numpy import random
import matplotlib.pyplot as plt
import seaborn

#Generate an exponential distribution
exponentialDist = random.exponential(scale=2, size=(3,4))

print(exponentialDist)

seaborn.distplot(exponentialDist)

plt.show()