import matplotlib.pyplot as plt
from numpy import random

#normal distribution
y = random.normal(loc=170,scale=10,size=250)

plt.hist(y)
plt.show()

#binomial distribution
y = random.binomial(n=12, p=0.7, size=300)

plt.hist(y)
plt.show()

#chisquare distribution
y = random.chisquare(df=100, size=300)

plt.hist(y)
plt.show()