#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 21:01:10 2018

@author: payeldas
"""


"""import os
#import csv
import pandas as pd 
#import numpy as np

#csvpath = os.path.join('..', 'Resources', 'accounting.csv')

#video = input("what show you are looking for? ")
"""
"""print(video)
csvpath=os.path.join('/Users/payeldas/Desktop/PythonStuff/RUTSOM201807DATA5/Monday-Wednesday/03-Python/1-Class-Content/1.2/08-Stu_ReadNetFlix','resources','netflix_ratings.csv')
#print(os.path)
#print (csvpath)
found = False

df1 = pd.read_csv(csvpath)
print(df1.head(2))



"""
"""with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    
    for value in csvreader:
        if value[0].upper() == video.upper():
            
            print(value[0] + "is rated"+ value[1] + " with a rating of " + value[5])
            found = True
            break
        if found == False:
            print("the show doesn't found...Ooops!!")
            
 """           
 print("my name is Payel")
 
 