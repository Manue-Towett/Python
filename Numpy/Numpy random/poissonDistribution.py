from numpy import random
import matplotlib.pyplot as plt
import seaborn

#create poisson distribution
poissonDist = random.poisson(lam=3.0, size=(100))

print(poissonDist)

#plot the graph
seaborn.distplot(poissonDist)

plt.show()