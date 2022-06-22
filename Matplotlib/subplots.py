import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([1,2,3,4,5])
x2 = np.array([1,3,4,6,8])

y1 = np.array([32,36,38,40,42])
y2 = np.array([40,38,36,34,32])

#Two plots side by side
#subplot 1
plt.subplot(1,2,1) #row 1, columns 2, plot 1
plt.plot(x1,y1)

#subplot 2
plt.subplot(1,2,2) #1 row, 2 colums, plot 2
plt.plot(x2,y2)

plt.show()

#Two plots on top of each other
#subplot1
plt.subplot(2,1,1) #two rows, 1 column, plot 1
plt.plot(x1,y1)

#subplot 2
plt.subplot(2,1,2)
plt.plot(x2,y2)

plt.show()

#four plots in one graph
plt.subplot(2,2,1)
plt.plot(x1,y1)

plt.subplot(2,2,2)
plt.plot(x2,y2)

plt.subplot(2,2,3)
plt.plot(x2,y1)

plt.subplot(2,2,4)
plt.plot(x1,y2)

plt.show()

#Titles and super titles
plt.subplot(2,2,1)
plt.plot(x1,y1)
plt.title("Orders")

plt.subplot(2,2,2)
plt.plot(x2,y2)
plt.title('Sales')

plt.subplot(2,2,3)
plt.plot(x2,y1)
plt.title("Customer traffic")

plt.subplot(2,2,4)
plt.plot(x1,y2)
plt.title('Working hours')

plt.suptitle("My Business")
plt.show()
