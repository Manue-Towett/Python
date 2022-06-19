from numpy import random
import matplotlib.pyplot as plt
import seaborn

#generate pareto distribution
paretoDist = random.pareto(a=3.4, size=(3,4))

print(paretoDist)

seaborn.distplot(paretoDist)

plt.show()