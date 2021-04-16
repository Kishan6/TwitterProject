# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 22:39:16 2021

@author: Kishan Pani
"""

from matplotlib import pyplot as plt
hours = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5]
depressed = [4.75, 5.00, 4.74, 4.67, 4.28, 3.17, 2.70, 2.65, 2.37, 2.44, 2.43, 2.65, 3.14, 3.65, 4.29, 4.61, 5.02, 5.43, 5.59, 5.51, 5.42, 5.21, 5.24, 5.03]
controlled = [4.20, 3.54, 3.03, 2.73, 2.52, 2.48, 2.55, 2.98, 3.58, 4.37, 4.57, 5.01, 5.40, 5.44, 5.31, 5.19, 4.93, 4.77, 4.51, 4.42, 4.38, 4.66, 4.72, 4.70]
plt.plot(hours, depressed, color = 'red', label = 'Depressed')
plt.plot(hours, controlled, color = 'blue', label = 'Normal')
plt.xlabel('Hour')
plt.ylabel('Percentage')
plt.title('Usage')
plt.legend(loc ="lower right")
plt.show