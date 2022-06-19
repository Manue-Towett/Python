from numpy import random
import matplotlib.pyplot as plt
import seaborn

#generate zipf distribution
zipfDist = random.zipf(a=3.4, size=(2,3))

print(zipfDist)

seaborn.distplot(zipfDist)

plt.show()