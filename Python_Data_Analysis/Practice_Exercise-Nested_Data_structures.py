# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:44:19 2019

@author: Brock

Practice Exercises for Nested Data Structures
"""

# Problem 1
nested_list = [[],[],[],[],[]]

#Problem 2
nested_list = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[7,0,0]]

#Problem 3
zero_list = [0 for x in range(3)]
#print(zero_list)

nested_list_comp = [[0 for x in range(3)] for x in range(5)]
nested_list = ([[col + 3 * row for col in range(3)] for row in range(5)])
#print(nested_list_comp)

print("")
print("")
print("=============== Problem 4 ==================")
print("")

print(nested_list[2][1])

#Problem 5
zero_list = [0, 2, 0]
nested_list = []
for dummy_idx in range(5):
#    nested_list.append(zero_list) #should be nested_list.append(list(zero_list))
    nested_list.append(list(zero_list))
#print(nested_list)

# Update an entry to be non-zero
#nested_list[2][1] = 7

#print(nested_list)

print("")
print("")
print("=============== Problem 6 ==================")
print("")

list_dicts = [{} for x in range(5)]
print(list_dicts)

#print("")
#print("")
#print("=============== Problem 7 ==================")
#print("")

def dict_copies(my_dict, num_copies):
    """
    Takes dictionary my_dict and an integer num_copies and 
    returns a list consisting of num_copies of my_dict
#    """
#    lists = []
#    for num in range(num_copies):
#        lists.append(dict(my_dict))
#    return lists

    # list-comprehension form
    dict_copy_list = [dict(my_dict) for num in range(num_copies)]
    return(dict_copy_list)
#print("")
#print("")
#print("=============== Problem 8 ==================")
#print("")
def make_dict_lists(length):
    """
    Takes an integer length and returns a dictionary whose keys are in range(length)
    and whose corresponding values are lsits of zeros whose length match the key
    """
    my_dict = {}
    for keys in range(length):
        values = [0 for x in range(keys)]
        my_dict.update({keys:values})
    return my_dict
    
#    list_dicts={}
#    for idx in range(length):
#        list_dicts[idx] = [0] * idx
#    return list_dicts
print("")
print("")
print("=============== Problem 9 ==================")
print("")

grade_table = {'Names'    : ['Joe', 'Scott', 'John'],
               'Assign#1' : [100, 75, 86],
               'Assign#2' : [98, 59, 84],
               'Assign#3' : [100, 89, 91],
               'Assign#4' : [13, 77, 78]
               }
format_string = "{:<8}  {:>5}  {:>5}  {:>5}  {:>5}"

headers = grade_table.keys()
#print(list(headers))
header_row = format_string.format(*headers)
print(header_row)
print('-' * len(header_row))

#print(grade_table['Assign#1'][0])
#print(grade_table['Names'][2])
#for values in range(3):
for values in range(len(grade_table['Names'])):
    row = "{:<8}  {:>7}  {:>7}  {:>7}  {:>7}".format(
            grade_table['Names'][values],
            grade_table['Assign#1'][values],
            grade_table['Assign#2'][values],
            grade_table['Assign#3'][values],
            grade_table['Assign#4'][values])
    print(row)
    
    
print("")
print("")
print("=============== Problem 10 ==================")
print("")

def make_grade_table(name_list, grades_list):
    """
    Takes a list of names -- names_list
    and a list of grades -- grades_list
    and returns a dict whose keys corresponds to names in name_list
    and whose corresponding values are the items grades_list
    """
    grade_table = dict(zip(name_list, grades_list))
    return grade_table
    
name_list = ['Brock', 'Cole', 'Jasmine']

grades_list = [[97,87,37], [34,54,67],[56,67,87]]
print(make_grade_table(name_list, grades_list))    
    