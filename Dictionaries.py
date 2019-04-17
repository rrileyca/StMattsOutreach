#DICTIONARIES:
#What are dictionaries?

#Dictionaries are a way to store information that is connected in some way. Dictionaries store information in key-value pairs, #so that any one piece of information in a dictionary is connected to at least one other piece of information.

#Dictionaries do not store their information in any particular order, so you may not get your information back in the same order #you entered it.
#General Syntax

#A general dictionary in Python looks something like this:

#dictionary_name = {key_1: value_1, key_2: value_2, key_3: value_3}

#Since the keys and values in dictionaries can be long, we often write just one key-value pair on a line. You might see #dictionaries that look more like this:

#dictionary_name = {key_1: value_1,
#                   key_2: value_2,
#                   key_3: value_3,
#                   }

#This is a bit easier to read, especially if the values are long.

phonebook = {"John" : 6135555555,
             "Jack" : 6135551111,
             "Jill" : 6131234567,
             }
print(phonebook)
