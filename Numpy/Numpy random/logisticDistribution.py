from numpy import random
import matplotlib.pyplot as plt
import seaborn

#generate a logistic distribution (loc = mean, scale = standard deviation, size = shape of the array)
logisticDist = random.logistic(loc=2.3, scale=3.4, size=(2,3))

print(logisticDist)

#plot graph
seaborn.distplot(logisticDist)

plt.show()