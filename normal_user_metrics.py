# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 21:57:50 2021

@author: Kishan Pani
"""

users = []

false_count = 0
dep_count = 0
dep_statuses = 0
dep_followers = 0
dep_friends = 0
dep_favourites = 0
dep_verified = 0
dep_unverified = 0

fn1 = open('normal_user.txt', 'r')

cont1 = fn1.readlines() 
type(cont1)
#for i in range(0, 100, 9):
for i in range(0, len(cont1), 9):
    if cont1[i] in users:
        pass
    else:
        users.append(cont1[i])
        dep_count += 1
        dep_statuses += int(cont1[i + 3])
        dep_followers += int(cont1[i + 4])
        dep_friends += int(cont1[i + 5])
        dep_favourites += int(cont1[i + 6])
        if (cont1[i+1] == 'false\n'):
            dep_unverified += 1
        if (cont1[i+1] == 'true\n'):
            dep_verified += 1
        
    false_count += 1
    
    if (i % 45000 == 0):
        print (i)
    
fn1.close()

print ('\n\n')
print ("Total tweets = ", false_count)
print ("Non-duplicate user accounts = ", dep_count)
print ("Duplicates = ", (false_count - dep_count))
print ("No. of verified accounts = ", dep_verified)
print ("No. of unverified accounts = ", dep_unverified)
print ("Percentage of verified accounts = ", (100*dep_verified/(dep_verified + dep_unverified)))
print ("Percentage of unverified accounts = ", (100*dep_unverified/(dep_verified + dep_unverified)))
print ("Average statuses for normal = ", (dep_statuses/dep_count))
print ("Average followers for normal = ", (dep_followers/dep_count))
print ("Average friends for normal = ", (dep_friends/dep_count))
print ("Average favourites for normal = ", (dep_favourites/dep_count))
print ('\n\n')