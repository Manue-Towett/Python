from numpy import random
import matplotlib.pyplot as plt
import seaborn

#create uniform distribution (low = lower bound and high = upperbound)
uniformDist = random.uniform(low=2.0, high=4.0, size=(100))

print(uniformDist)

seaborn.distplot(uniformDist)

plt.show()