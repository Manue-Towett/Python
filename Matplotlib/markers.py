import matplotlib.pyplot as plt
import numpy as np

#plottting multiple points
x_points = np.array([1,2,3,4,5,6])
y_points = np.array([5,9,2,4,1,8])

#emphasizing points with a specified marker
plt.plot(x_points,y_points,marker='o')
plt.show()

'''
other markers that can be used are format strings
: dotted line
-- dashed line
- solid line
-. dashed/dotted line
also color references can be used to specify the color of the line
eg r = red, g=green, c=cyan, b = blue, m = magenta, k = black, y = yellow, w = white
'''
plt.plot(y_points, 'o:c') #dotted cyan line with specified o marker for points
plt.show()

plt.plot(y_points, '--y') #dashed yellow line
plt.show()

plt.plot(y_points, '*-.g') #dashed/dotted green line with * marker for points
plt.show()

#set marker size
plt.plot(y_points, marker = 'o', ms = 20)
plt.show()

#set marker edge color
plt.plot(y_points, marker = 'o', mec = 'r', ms=20)
plt.show()

#set marker color inside the edges
plt.plot(y_points, marker='o', mfc='r', ms=20)
plt.show()