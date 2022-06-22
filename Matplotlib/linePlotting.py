import matplotlib.pyplot as plt
import numpy as np

#plotting a line between 2 points
x_points = np.array([2,7])
y_points = np.array([9,200])

plt.plot(x_points, y_points)
plt.show()

#plotting line without the line
plt.plot(x_points,y_points,'o')
plt.show()

#plottting multiple points
x_points = np.array([1,2,3,4,5,6])
y_points = np.array([5,9,2,4,1,8])

plt.plot(x_points,y_points)
plt.show()

#if only one array is speciefied, it is taken as the y_axis and x_axis get default values 0,1,2,3,4,5
plt.plot(y_points)
plt.show()

#using linestyle ls function
plt.plot(y_points, ls='dotted') #returns dotted line
plt.show()

#it can also be done using a shorter syntax of ':'
plt.plot(y_points, ':')
plt.show()

#dashed line
plt.plot(y_points, '--')
plt.show()

#set line color
plt.plot(y_points, c='r')
plt.show()

plt.plot(y_points, 'g')
plt.show()

plt.plot(y_points, 'hotpink')
plt.show()

#linewidth 
plt.plot(y_points, lw=20)
plt.show()

#multiple lines plotting
y1 = np.array([3,7,8,3,9])
y2 = np.array([2,6,3,7,7])

plt.plot(y1)
plt.plot(y2)

plt.show()

#another way of plotting multiple lines
x1 = np.array([1,2,3,4,5])
x2 = np.array([0,2,4,5,7])

plt.plot(x1,y1,x2,y2)
plt.show()