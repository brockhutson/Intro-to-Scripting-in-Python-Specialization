# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 10:38:27 2019

@author: Brock
"""

def parse_cereal(csvfilename):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a list of lists.
    """
    table = []
    with open(csvfilename, "r") as csvfile:
        for line in csvfile:
            line = line.rstrip()
            columns = line.split(';')
            table.append(columns)
    return table


def print_table(table):
    """
    Print out table, which must be a list
    of lists, in a nicely formatted way.
    """
    for row in table:
        # Header column left justified
        print("{:<19}".format(row[0]), end='')
        # Remaining columns right justified
        for col in row[1:]:
            print("{:>4}".format(col), end='')
        print("", end='\n')