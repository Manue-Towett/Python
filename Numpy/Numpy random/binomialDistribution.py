from numpy import random
import matplotlib.pyplot as plt
import seaborn

#generate binomial distributin
binomialDist = random.binomial(n=4, p=0.4, size=(100))

print(binomialDist)

seaborn.distplot(binomialDist, hist=True, kde=False)

plt.show()