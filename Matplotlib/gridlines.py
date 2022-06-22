import matplotlib.pyplot as plt
import numpy as np

x = np.array([70,75,80,85,90,95])
y = np.array([200,240,280,320,360,400])

fontTitle = {'family':'serif','color':'blue','size':20}
fontLabel = {'family':'serif','color':'darkred','size':15}

plt.plot(x,y)

plt.title("Sports Watch Data", fontdict=fontTitle)
plt.xlabel("Average Pulse", fontdict=fontLabel)
plt.ylabel("Calorie Bumage", fontdict=fontLabel)

#show gridlines
plt.grid()

plt.show()

#specifying the grid lines to show
plt.plot(x,y)

plt.title("Sports Watch Data", fontdict=fontTitle)
plt.xlabel("Average Pulse", fontdict=fontLabel)
plt.ylabel("Calorie Bumage", fontdict=fontLabel)

#show x gridlines
plt.grid(axis='x')

plt.show()

#show y gridlines
plt.plot(x,y)

plt.title("Sports Watch Data", fontdict=fontTitle)
plt.xlabel("Average Pulse", fontdict=fontLabel)
plt.ylabel("Calorie Bumage", fontdict=fontLabel)

plt.grid(axis='y')

plt.show()

#set line properties for the grid
plt.plot(x,y)

plt.title("Sports Watch Data", fontdict=fontTitle)
plt.xlabel("Average Pulse", fontdict=fontLabel)
plt.ylabel("Calorie Bumage", fontdict=fontLabel)

#c for color and ls for linestyle
plt.grid(c='grey',ls='--')

plt.show()