################
# IF STATEMENT #
################

# if-statements are used to execute some code IF a certain condition is met
# In the code below, we bring in a random number (x) and check out what its value is.
 
# START SCRIPT ########################################
from random import randint

x = randint(1,10) # A random number from 1-10

# If the number is greater than 5:
if x > 5:
  print("The random number is above 5")

# Else if the number is less than 5:
elif x < 5:
  print("The random number is less than 5")

# Otherwise, if none of the above, do this!
else:
  print("The random number must be 5!")

# END SCRIPT ##########################################




################
# FLOW CONTROL #
################

# Flow Control is important! Using the "break" and "continue"
# BREAK - stops the entire loop
# CONTINUE - stops the current iteration, not the whole loop
# IMPORTANT: Loops are WHILE and FOR. The IF is a STATEMENT, not a loop.

# START SCRIPT ########################################
from random import randint

randomNumber = randint(1,10) # A random number from 1-10
guess = 0

print("Psst: The secret random number is: " + str(randomNumber))

while True:
  if guess == randomNumber:
    print("The random number was " + str(guess))
    break # Break out of the WHILE loop
  else:
    print("The random number was NOT " + str(guess))
    guess += 1 # Add 1 to the current "guess" integer.


# END SCRIPT ##########################################


##############
# USER INPUT #
##############
# Use the input() function to accept input from the keyboard!

# START SCRIPT ########################################
from random import randint

secretNumber = randint(1,10)

while True:
  userGuess = input("Guess what the number is: ")
  if userGuess == str(secretNumber): # NOTE! The str() function turns a number into a String!
    print("That's correct! YOU WIN!")
    break


# END SCRIPT ##########################################
