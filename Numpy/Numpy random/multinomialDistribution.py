from numpy import random
import matplotlib.pyplot as plt
import seaborn

#generate multinomial distribution of dice roll
multinomialDist = random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6], size=(100))

print(multinomialDist)

seaborn.distplot(multinomialDist)

plt.show()