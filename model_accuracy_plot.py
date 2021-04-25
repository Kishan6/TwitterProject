# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 07:51:26 2021

@author: Kishan Pani
"""

from matplotlib import pyplot as plt

percentage_removed = [0, 50, 66.67, 75, 80, 83.33, 100]
nb1 = [97.17, 83.54, 76.70, 75.49, 75.08, 74.84, 72.43]
nb2 = [84.58, 82.34, 77.14, 77.09, 76.78, 76.73, 74.72]
lr = [98.58, 89.12, 79.63, 78.99, 78.65, 78.48, 77.05]
svm = [98.87, 89.38, 79.66, 78.62, 78.30, 78.10, 76.40]
rf = [98.42, 87.81, 76.47, 75.73, 75.07, 74.84, 72.53]

plt.plot(percentage_removed, nb1, color = 'magenta', label = 'Naive Bayes (One hot)', marker = 'o')
plt.plot(percentage_removed, nb2, color = 'red', label = 'Naive Bayes (TF-IDF)', marker = 'o')
plt.plot(percentage_removed, lr, color = 'blue', label = 'Logistic regression', marker = 'o')
plt.plot(percentage_removed, svm, color = 'green', label = 'Support Vector Machines', marker = 'o')
plt.plot(percentage_removed, rf, color = 'cyan', label = 'Random forest', marker = 'o')

plt.ylim([70, 100])
plt.xlabel('Percentage of keywords removed')
plt.ylabel('Accuracy of model')
plt.title('Accuracy of different models')
plt.legend(loc ="lower left")
# plt.show

plt.savefig('accuracies.png', dpi=300)