# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:38:21 2019

@author: Brock
"""

"""
Dictionary lookup and update.
"""


print("Dictionary Lookup")
print("=================")

cipher = {'p': 'o', 'y': 'h', 't': 'n',
          'h': 't', 'o': 'y', 'n': 'p'} 
#print(cipher)

# Use indexing with keys to access values
#print(cipher['t'])
#print(cipher['n'])

#def encrypt(cipher, word):
#    """encrypt word using cipher"""
#    encrypted = ""
#    for char in word:
#        encrypted += cipher[char]
#    return encrypted
#
#python = "python"
#enc = encrypt(cipher, python)
#print(python, enc)
#
## It is an error to use a non-existent key
## print(cipher[1])
#
## Use .get when you are unsure if the key exists
#print(cipher.get('t'))
#print(cipher.get(1))
#print(cipher.get(1, 'z'))
#
#print("")
#print("Dictionary Update")
#print("=================")
#
#print(cipher)
#
## Modify an existing key->value mapping
#cipher['p'] = 'q'
#print(cipher)
#
## Create a new key->value mapping
#cipher['r'] = 'z'
#print(cipher)
#
#enc2 = encrypt(cipher, python)
#print(python, enc, enc2)


map = [(1, 5), (8, -3), (7, 22), (4, 13), (22, 17)]
mapping = dict(map)
keys = [8, 14, 22, 25]
for key in keys:
    if key in mapping:
            print(key, mapping[key])
    else:
        print("{} not in mapping".format(key))
        