from turtle import color
import matplotlib.pyplot as plt
import numpy as np

y = np.random.randint(100, size=(10))
x = np.array(['A','B','C','D','E','F','G','H','I','J'])

#vertical bars
plt.bar(x,y)
plt.show()

#horizontal bars
plt.barh(x,y)
plt.show()

#changing the color
plt.bar(x,y, color='red')
plt.show()

#width of the bars
plt.bar(x,y, color='darkred', width=0.2)
plt.show()

#height manipulation (width of horizontal bars)
plt.subplot(1,2,1)
plt.barh(x,y, height=0.1)

plt.subplot(1,2,2)
plt.barh(x,y)

plt.show()