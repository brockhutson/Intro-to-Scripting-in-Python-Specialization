# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:14:10 2019

@author: Brock
"""

def mile_to_feet(miles):
    feet = miles * 5280
    return feet

def seconds():
    hours = input("Enter numer of hours: ")
    minutes = input("Enter number of minutess: ")
    seconds = input("Enter number of seconds: ")
    time = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    return time

def rec_per(w, h):
    """
    Takes in the width (w) and height(h) of a rectangle 
    and calulates the perimeter. 
    """
    perim = 2*w + 2*h
    print (perim)
    

def twopdist(x0, y0, x1, y1):
    dist = ((x0 - x1)**2 + (y0-y1)**2)**0.5
    print(dist)
    
############################3
    ## Datetime Module
#########################
    
#import datetime

# Create some dates
#print("Creating Dates")
#print('==============')
#
#date1 = datetime.date(1999, 12, 31)
#date2 = datetime.date(2000, 1, 1)
#date3 = datetime.date(2016, 4, 15)
#date4  = datetime.date(2012, 8 , 32)

# Todays Date
#today = datetime.date.today()
#print(date1)
#print(date2)
#print(date3)
#print(today)

#print((today - date2).days)

def checkfile(filename):
    """
    Read and print the contents of the file name
    """
    datafile = open(filename, "rt")
    data = datafile.read()
    datafile.close()
    print(data)

# Write
outputfile = open("output.txt", "wt")
outputfile.writelines(["first line\n", "secondline\n"])
outputfile.write("third line\nfourth line\n")
outputfile.close()

print("Initial file contents:")
checkfile("output.txt")
    