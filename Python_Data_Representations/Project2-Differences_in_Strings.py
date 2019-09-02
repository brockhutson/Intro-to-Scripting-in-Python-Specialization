# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:25:26 2019

@author: Brock

Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    
#    len1 = len(line1)
#    len2 = len(line2)
#    
#    if len1 == len2:
#        if line1 == line2:
#            return IDENTICAL
#        elif line1 != line2:
#            for letter in range(min(len1, len2)):
#                if line1[letter] != line2[letter]:
#                    return letter
#                
#    if len1 != len2:
#        for ind in range(min(len1, len2)):
#            if line1[ind] != line2[ind]:
#                return ind
##        for ind in range(min(len1, len2)):
#            if line1[ind] == line2[ind]:
#                return min(len1, len2)
    
    if len(line1) < len(line2):
        shortline = line1
        longline = line2
    elif len(line2) < len(line1):
        shortline = line2
        longline = line1
    

#    shortlen = len(shortline)
    
    if line1 == line2:
        return IDENTICAL
    
    if shortline == longline[:len(shortline)]:
        return len(shortline)
        
    count = 0
    for char in shortline:
        if char != longline[count]:
            return count
        elif char == longline[count]:
            count += 1

        
            
        
     


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    
    if "\n" in line1 or "\r" in line1:
#        print("line1 is not a single line string")
        return ""
    elif "\n" in line2 or "\r" in line2:
#        print("line2 is not a single lin string")
        return ""
    
    if singleline_diff(line1, line2) != idx:  
        return ""
    
    else:
        idx = singleline_diff(line1, line2)
    
        line_index = "=" * (idx) + "^"
        answer = line1 + "\n" + line_index + "\n" + line2 + "\n"
        return answer
    



def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
      
      lines1 = ['string11', 'string12']
      lines2 = ['string21', 'string22']
    """
#    first_diff = 0
#    for strings1 in lines1:
#        if len(strings1) > first_diff:
#            first_diff = strings1
#        for strings2 in lines2:
#            if len(strings2) > first_diff:
#                first_diff = strings2
#            if singleline_diff(strings1, strings2) != -1:
                  
    
    sld00 = singleline_diff(lines1[0], lines2[0])
    sld10 = singleline_diff(lines1[1], lines2[0])
    sld01 = singleline_diff(lines1[0], lines2[1])
    sld11 = singleline_diff(lines1[1], lines2[1])    
    
    if sld00 != -1:
        return (0, sld00)
        
    if sld01 != -1:
        if sld10 != -1:
            return(0, min(sld01, sld10))
        if sld10 == -1:
            return(0, sld01)
         
    if sld11 != -1:
        return (1, sld11) 
    
    if lines1 == lines2:
        return (IDENTICAL, IDENTICAL)    


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    
    fhand = open(filename).readlines()
    
    newlist = list()
    for line in fhand:
        line = line.strip()
        newlist.append(line)

    return newlist


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    
    fhand1 = get_file_lines(filename1)
    fhand2 = get_file_lines(filename2)
    
    mdiff = multiline_diff(fhand1, fhand2)
    print(mdiff)
    
    
    
    
    ans1 = "Line " + str(mdiff[0]) + ":\n"
    ans2 = fhand1[1] + "\n"
    ans3 = "=" * (mdiff[1]) + "^\n"
    ans4 = fhand2[1] + "\n"
    answer = ans1 + ans2 + ans3 + ans4
    
    return answer
     
    if filename1 == filename2:
        return ""