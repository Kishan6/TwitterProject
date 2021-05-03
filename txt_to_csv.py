# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import random

counter = 0

fn = open('control.txt', 'r')

df1 = pd.DataFrame(columns= ['Tweet ID', 'tweet', 'Location', 'statuses', 'followers', 'friends', 'favourites', 'Date-time', 'class'])

cont = fn.readlines() 
type(cont)
#for i in range(0, 100, 11):
for i in range(0, len(cont), 11):
    zero = cont[i]
    one = cont[i + 1]
    
    temp = ""
    for j in range(0, len(one)):
        if (one[j] == 'A'):
            temp += 'a'
        if (one[j] == 'B'):
            temp += 'b'
        if (one[j] == 'C'):
            temp += 'c'
        if (one[j] == 'D'):
            temp += 'd'
        if (one[j] == 'E'):
            temp += 'e'
        if (one[j] == 'F'):
            temp += 'f'
        if (one[j] == 'G'):
            temp += 'g'
        if (one[j] == 'H'):
            temp += 'h'
        if (one[j] == 'I'):
            temp += 'i'
        if (one[j] == 'J'):
            temp += 'j'
        if (one[j] == 'K'):
            temp += 'k'
        if (one[j] == 'L'):
            temp += 'l'
        if (one[j] == 'M'):
            temp += 'm'
        if (one[j] == 'N'):
            temp += 'n'
        if (one[j] == 'O'):
            temp += 'o'
        if (one[j] == 'P'):
            temp += 'p'
        if (one[j] == 'Q'):
            temp += 'q'
        if (one[j] == 'R'):
            temp += 'r'
        if (one[j] == 'S'):
            temp += 's'
        if (one[j] == 'T'):
            temp += 't'
        if (one[j] == 'U'):
            temp += 'u'
        if (one[j] == 'V'):
            temp += 'v'
        if (one[j] == 'W'):
            temp += 'w'
        if (one[j] == 'X'):
            temp += 'x'
        if (one[j] == 'Y'):
            temp += 'y'
        if (one[j] == 'Z'):
            temp += 'z'
            

        if (one[j] == 'a' or one[j] == 'b' or one[j] == 'c' or one[j] == 'd' or one[j] == 'e' or one[j] == 'f' or one[j] == 'g' or one[j] == 'h' or one[j] == 'i' or one[j] == 'j' or one[j] == 'k' or one[j] == 'l' or one[j] == 'm' or one[j] == 'n' or one[j] == 'o' or one[j] == 'p' or one[j] == 'q' or one[j] == 'r' or one[j] == 's' or one[j] == 't' or one[j] == 'u' or one[j] == 'v' or one[j] == 'w' or one[j] == 'x' or one[j] == 'y' or one[j] == 'z' or one[j] == '0' or one[j] == '1' or one[j] == '2' or one[j] == '3' or one[j] == '4' or one[j] == '5' or one[j] == '6' or one[j] == '7' or one[j] == '8' or one[j] == '9' or one[j] == '\\' or one[j] == ' '):
            temp += one[j]
            
        if ((j < (len(one) - 1)) and (j > 1)):
            if ((one[j-1] == '\\') and (one[j] == 'n') and (one[j+1] != ' ')):
                temp += ' '
    
    #r1 = random.randint(0, 10)
    #r1 = 1
    #if (r1 < 3):
    temp = temp.replace(" fuck ", " ")
    temp = temp.replace(" fucking ", " ")
    temp = temp.replace(" n ", " ")
    temp = temp.replace(" u ", " ")
    one = temp
    
    three = cont[i + 3]
    five = int(cont[i + 5])
    six = int(cont[i + 6])
    seven = int(cont[i + 7])
    eight = int(cont[i + 8])
    nine = cont[i + 9]

    #df.append({'Tweet ID' : zero, 'tweet' : one, 'Location' : three, 'statuses' : five, 'followers' : six, 'friends' : seven, 'favourites' : eight, 'Date-time' : nine, 'class' : 'depressed'}, ignore_index = True)
    
    df1.loc[int(i/11)] = (zero, one, three, five, six, seven, eight, nine, 'depressed')
    
    if (i%11000 == 0):
        print (str(i) + " lines processed")
        
    counter = int((i/11)+1)
        
fn.close()

df1["statuses"] = pd.to_numeric(df1["statuses"])
df1["followers"] = pd.to_numeric(df1["followers"])
df1["friends"] = pd.to_numeric(df1["friends"])
df1["favourites"] = pd.to_numeric(df1["favourites"])



df1.to_csv('control_tweets.csv')