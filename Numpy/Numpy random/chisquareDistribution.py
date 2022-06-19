from numpy import random
import matplotlib.pyplot as plt
import seaborn

#generate chi square distribution
chisquareDist = random.chisquare(df=4, size=(2,3))

print(chisquareDist)

seaborn.distplot(chisquareDist)

plt.show()