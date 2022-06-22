import matplotlib.pyplot as plt
import numpy as np

portions = np.random.randint(100, size=(6))

plt.pie(portions)
plt.show()

#plotting pie charts with labels
fruitLabels = np.array(['Oranges','Pineaples','Apples','Bananas','Cheries'])

plt.pie(portions[:5], labels=fruitLabels)
plt.show()

#starting at angle 90 degrees
plt.pie(portions[:5], labels=fruitLabels, startangle=90)
plt.show()

#pull one wedge from the center by 0.2
explodedWedge = [0.2,0,0,0,0]

plt.pie(portions[:5], labels=fruitLabels, explode=explodedWedge)
plt.show()

#exploding all the wedges
explodedWedge = [0.1,0.1,0.1,0.1,0.1]

plt.pie(portions[:5], labels=fruitLabels, explode=explodedWedge)
plt.show()

#introduce a shadow
explodedWedge = [0.2,0,0,0,0]

plt.pie(portions[:5], labels=fruitLabels, explode=explodedWedge, shadow=True)
plt.show()

#add a legend
plt.pie(portions[:5], labels=fruitLabels)
plt.legend()
plt.show()