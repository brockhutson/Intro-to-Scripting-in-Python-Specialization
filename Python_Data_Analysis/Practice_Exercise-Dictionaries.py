"""Practice Exercises for Dictionaries
Solve each of the practice exercises below. Each problem includes two CodeSkulptor3 links: one for a 
template that you should use as a starting point for your solution and one to our solution to the exercise.
"""

"""
1.  Write an expression that initializes the dictionary \color{red}{\verb|my_dict|}my_dict to be the empty 
    dictionary. Empty dictionary template --- Empty dictionary solution
"""
my_dict = dict()
my_dict2 = {}

"""
2.  Write an expression that initializes the dictionary \color{red}{\verb|my_dict|}my_dict to contain 
    two key/value pairs: \color{red}{\verb|"Joe" : 1|}"Joe":1 and \color{red}{\verb|"Scott" : 2|}"Scott":2. 
    Two key dictionary template --- Two key dictionary solution
"""
my_dict = {"Joe" : 1, "Scott" : 2}

"""
3.  Given the dictionary \color{red}{\verb|my_dict|}my_dict from the previous question, write a Python 
    statement that adds the key/value pair \color{red}{\verb|"John" : 3|}"John":3 to this dictionary. 
    Add key/value template --- Add key/value solution
"""
my_dict["John"] = 3


"""
4.  Given the dictionary \color{red}{\verb|my_dict|}my_dict from the previous question, write three 
    expressions that return \color{red}{\verb|True|}True if the dictionary \color{red}{\verb|my_dict|}my_dict 
    whether the keys \color{red}{\verb|"Joe"|}"Joe" , \color{red}{\verb|"Scott"|}"Scott" , 
    and \color{red}{\verb|"John"|}"John", respectively, and \color{red}{\verb|False|}False otherwise . 
    Contains key template --- Contains key solution
"""
print("John" in my_dict)
print("Joe" in my_dict)
print("Stephen" in my_dict)

"""
5.  Write a function \color{red}{\verb|is_empty(my_dict)|}is_empty(my_dict) that takes a dictionary 
    \color{red}{\verb|my_dict|}my_dict and returns \color{red}{\verb|True|}True 
    if \color{red}{\verb|my_dict|}my_dict is empty and \color{red}{\verb|False|}False otherwise. Is empty 
    template --- Is empty solution
"""
def is_empty(my_dict):
    if len(my_dict) == 0:
        return True
    else:
        return False
    
"""
6.  Write a function \color{red}{\verb| value_sum(my_dict)|}value_sum(my_dict) that returns the sum of the 
    values in the dictionary \color{red}{\verb|my_dict|}my_dict. (You may assume that the values in the 
    dictionary are numbers). Value sum template --- Value sum solution
"""
def value_sum(my_dict):
    """
    Calculates the sum for all values in a dictionary
    """
    
    value_sum = 0
    for key in my_dict:
        value_sum += my_dict[key]
    return(value_sum)
"""
7.  Write a function \color{red}{\verb|make_dict(key_value_list) |}make_dict(key_value_list) that takes a 
    list of tuples \color{red}{\verb|key_value_list |}key_value_list where each tuple is of the form (key, value) 
    and returns a dictionary with these keys and corresponding values. Make dictionary template --- Make dictionary solution
"""
def make_dict(key_value_list):
    """
    Takes a LIST of TUPLES and returns them in the form of a dictionary
    """
    my_new_dict = dict(key_value_list)
    return my_new_dict

"""
8.  A simple substitution cipher is an encryption scheme where each letter in an alphabet to replaced by a 
    different letter in the same alphabet with the restriction that each letter's replacement is unique. 
    The template for this question contains an example of a substitution cipher represented a 
    dictionary \color{red}{\verb|CIPHER_DICTIONARY|}CIPHER_DICTIONARY. Your task is to write a 
    function \color{red}{\verb|encrypt(phrase, cipher_dict)|}encrypt(phrase,cipher_dict) that takes a 
    string \color{red}{\verb|phrase|}phrase and a dictionary \color{red}{\verb|cipher_dict|}cipher_dict 
    and returns the results of replacing each character in \color{red}{\verb|phrase|}phrase by its 
    corresponding value in \color{red}{\verb|cipher_dict|}cipher_dict. Encrypt template --- Encrypt solution
"""
def encrypt(phrase, cipher_dict):
    """
    Takes in a phrase, as a string, and a dictionary containing the cipher
    and returns a string encryped by the cipher dictionary.
    """
    
    encrypted_word = ''
    for char in phrase:
        encrypted_word += cipher_dict[char]
    return encrypted_word

"""
9.  Challenge: Write a function \color{red}{\verb|make_decipher_dict(cipher_dict)|}make_decipher_dict(cipher_dict) 
    that takes a cipher dictionary \color{red}{\verb|cipher_dict|}cipher_dict and returns a new 
    dictionary \color{red}{\verb|decipher_dict|}decipher_dict with the property that 
    applying \color{red}{\verb|decipher_dict|}decipher_dict to a phrase encrypted using 
    \color{red}{\verb|cipher_dict|}cipher_dict returns the original phrase. 
    Make decipher template --- Make decipher solution
"""
def make_decipher_dict(cipher_dict):
    """
    Takes in a dictionary containing a cipher and returns
    a cipher "key", in the form of a dictionary with the opposite key, value pairs.
    """
    
    decipher_dict = {}
    for key,value in cipher_dict.items():
        decipher_dict[value] = key
    return decipher_dict
"""
10. Challenge: Write a function \color{red}{\verb|make_cipher_dict(alphabet)|}make_cipher_dict(alphabet) 
    that takes a string of unique characters and returns a randomly-generated cipher dictionary for the 
    characters in \color{red}{\verb|alphabet|}alphabet . You should use the \color{red}{\verb|shuffle()|}shuffle() 
    method in the \color{red}{\verb|random|}random module to ensure that your returned cipher dictionary is random.
    Make cipher template --- Make cipher solution
"""
def make_cipher_dict(alphabet):
    """
    Takes in a string, shuffles the letters in the string around in order to create
    a cipher using the same letters.
    """
    
    import random
    letters = list(alphabet)
    shuffled_letters = random.shuffle(list(alphabet))
    
    
    cipher_dict = {}
    for index in range(len(alphabet)):
        letter = letters[index]
        shuffled_letter = shuffled_letters[index]
        cipher_dict[letter] = shuffled_letter
    return cipher_dict