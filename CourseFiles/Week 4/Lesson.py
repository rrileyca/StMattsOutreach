# This is a comment
# Any line starting with a "#" (hashtag) character will not run


# print("This will not print")
# The above print statement didn't work. Try un-commenting it (remove the "#) and run it again!


# This "import" statement brings a useful "package" into our program for us to use.
# A package contains someone elses code that they worked hard so we don't have to!
# This "time" package lets us use the "time.sleep(10)" function, where the number 10 is the number of seconds to sleep!
# Sleeping makes the program stop running for a certain period of time.
# The "time" package brings in other functions too, but we will only use "sleep" for now.

import time


# This import only imports 1 single function (the "randint" function) from the "random" package.
# The "randint" function allows us to generate random numbers!

from random import randint


# Variables are named values we can use later. Variables can be Strings, Integers, or other values.
# The name of a variable doesn't matter - it's whatever you'd like, with some rules on some special characters not being allowed.
stringVariable = "Hello World!"
integerVariable = 10

# Now we can re-use the variables below:
print(stringVariable)
print(10)

# NOTICE! Some variables have quotation marks, and some do not
# A number without a quotation mark is an Integer, but a number in quotation marks is a string!

print(10 + 10)  # This will print 20

print(integerVariable + 15) # This will print 25, because "integerVariable" is a number

print(stringVariable + " How are you today?")  # This will print "Hello World! How are you today?"\

# This statement below will cause an ERROR! Why? Because you cannot added a number plus a string.
# Think about it: "What is 1 plus an apple?". That doesn't make sense
print(integerVariable + stringVariable) # ERROR!


# These two lines are setting up variables - specifically, 2 variables that are of the type "array".
# An array keeps a bunch of "items" inside, like a bunch of Strings or Integers.
# We can use these later in our program!

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# A for loop will go through an array, and do *something* for each item
# This for loop will print out each letter on a new line.
for l in letters:
    print(l)

# This for loop will go through each number (from the number array above) and print the number +10 on a new line.
for number in numbers:
    print(number + 10)


# A for loop! It will go through each item in the "letters" array, set that item to the variable "l", and do something (below).
for l in letters:
    # A "nested for loop"! For each item in letters (above), we will iterate through each item in "numbers"
    for n in numbers:
        # And print out which letter and number we are on!
        print(l, n)


# A simple print statement to print out the dashses. Helps us visually divide what is happening.
print("--------------------- SECTION 1---------------------------")


# This index is being set to the RESULT of the "range" method on the right
# The range method returns an array starting at 0, that is 10 items long. So: [0,1,2,3,4,5,6,7,8,9]
# So! This statement is the same as saying "index = [0,1,2,3,4,5,6,7,8,9]"

index = range(0, 10)


# In this for loop, we have used the time.sleep(1) method
# This allows us to slow down the "print" statements by putting a second in between each "print"!
# Sort of like "print(1)... mississippi... print(2)... mississippi... print(3)... mississippi..."
for i in index:
    print(letters[i], numbers[i])
    # time.sleep(1)

print("--------------------- SECTION 2---------------------------")


# Do you remember what range does? What does the 0 stand for? What does the 20 stand for?
for i in range(0, 20):
    # This print statement has 4 values separated by commas. It means (all on the same line of output):
    # print the string "x="
    # print the result of randint(0,10)
    # print the string "y="
    # print the result of randint(0,10)

    print("x=", randint(0, 10), "y=", randint(0, 10))


print("--------------------- SECTION 3---------------------------")

# Here we are "def"-ining our own function that we can use over-and-over again.
# The name of the function is "logxy"
# It takes in exactly 2 arguments, which are variables called "x" and "y"
# Then, what the function DOES is the print statement inside of it


def logxy(x, y):
    print("x=", x, "y=", y)


print("--------------------- SECTION 4---------------------------")

# This uses our function we "def"-ined above. What do you think it will do?
logxy(1, 2)


print("--------------------- SECTION 5---------------------------")

# This is a for loop that uses our function above. What do you think it will do?
for i in index:
    logxy(letters[i], numbers[i])
