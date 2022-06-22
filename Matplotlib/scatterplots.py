import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([23,25,12,29,19])

#plotting a scatter graph
plt.scatter(x,y)
plt.show()

#compare two scatter plots
plt.scatter(x,y)

x1 = np.array([2,4,6,7,9])
y1 = np.array([12,23,15,24,6])

plt.scatter(x1,y1)

plt.show()

#set own colors for each plot
plt.scatter(x,y, c="red")

plt.scatter(x1,y1, c="cyan")

plt.show()

#color each dot
colors = np.array(['red','orange','yellow','lightgreen','darkgreen'])

plt.scatter(x,y, c=colors)
plt.show()

#using builtin color maps
colors = np.array([10,20,30,40,50])

plt.scatter(x,y, c=colors, cmap='viridis')
plt.show()

#including the colormap in the plot
plt.scatter(x,y, c=colors, cmap="viridis")
plt.colorbar()

plt.show()

#changing the size of the dots
sizes = np.array([120,170,110,25,190])

plt.scatter(x,y, s=sizes)
plt.show()

#changing the transparency of the dots
plt.scatter(x,y, s=sizes, alpha=0.5)
plt.show()

#combining color,size and alpha
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = np.random.randint(100, size=(100))

plt.scatter(x,y, c=colors, s=sizes, alpha=0.5)
plt.show()