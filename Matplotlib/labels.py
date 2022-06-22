from turtle import left
import matplotlib.pyplot as plt
import numpy as np

x = np.array([70,75,80,85,90,95])
y = np.array([180,220,260,300,340,380])

plt.plot(x,y, marker='o')

#creating x and y labels
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Bumage")

plt.show()

#creating title label
plt.plot(x,y, marker='o')
plt.title("Sports Watch Data")
plt.show()

#font properties of the title and labels
fontTitle = {"family":"serif","color":"blue","size":20}
fontLabel = {'family':'serif','color':'darkred','size':15}

plt.plot(x,y)

plt.title("Sports Watch Data", fontdict=fontTitle)
plt.xlabel("Average Pulse", fontdict=fontLabel)
plt.ylabel("Calorie Bumage", fontdict=fontLabel)

plt.show()

#position the title
plt.plot(x,y)

plt.title("Sports Watch Data", fontdict=fontTitle, loc='left')

plt.show()