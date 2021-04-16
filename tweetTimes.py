# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:02:15 2021

@author: Kishan Pani
"""

hours = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, ]
dep_time = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dep_time_percent = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
con_time_percent = [4.20, 3.54, 3.03, 2.73, 2.52, 2.48, 2.55, 2.98, 3.58, 4.37, 4.57, 5.01, 5.40, 5.44, 5.31, 5.19, 4.93, 4.77, 4.51, 4.42, 4.38, 4.66, 4.72, 4.70]

fn = open('happy_user.txt', 'r')

cont = fn.readlines() 
type(cont)
#for i in range(0, 100, 11):
for i in range(0, len(cont), 9):
    time = cont[i + 7]
    hr = time[12:14]
    dep_time[int(hr)] += 1
    
fn.close()

sum = 0
for i in range (24):
    sum += dep_time[i]
    
for i in range (24):
    dep_time_percent[i] = round((100*dep_time[i]/sum), 2)
    
print (dep_time_percent)
print ('\n\n')
print (con_time_percent)