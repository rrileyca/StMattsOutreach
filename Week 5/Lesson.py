# Import the libraries for the Unicorn HAT.
# The "as" keyword means to import the Unicorn HAT package as the variable "unicorn"
import unicornhat as unicorn

# Setting up the Unicorn HAT
# NOTE: If only half of the screen lights up, changes "unicorn.AUTO" to "unicorn.HAT"
unicorn.set_layout(unicorn.AUTO)

# This sets the rotation of the LED's. We shouldn't need to change this much, but try setting it to 90, 180, -90, or -180.
unicorn.rotation(0)

# This sets the brightness of the LED lights, from 0.0 to 1.0 MAX.
unicorn.brightness(0.5)

# This sets two variables at once -- "width" and "height" -- to the same value. In this case, the value of "get_shape".
# Don't worry too much about what "get_shape()" does. It comes from "unicorn", which is our Unicorn HAT package.
# Someone else wrote this code so we don't have to!
width,height=unicorn.get_shape()

# So! Near the top of every script, you should have something like this:
import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

# Let's turn the LED at the top-left corner on. This corner has the coordinates of x=0 and y=x.
# The "unicorn.set_pixel" command helps us set a pixel to be a certain color. It takes 5 arguments in this order:
# set_pixel(x,y,r,g,b)
# Where x is the x-axis; y is the y-axis; and r, g, and b represent "red", "green", and "blue" - the 3 colors in every pixel.
# r, g, and b are all integers between 0-255 so you can mix how much of each color is present to make a bunch of different colors!

# This sets the pixel at x=0,y=0 to be white.
unicorn.set_pixel(0,0,255,255,255)

# This sets the pixel at x=0,y=0 to be red.
unicorn.set_pixel(0,0,255,0,0)

# This sets the pixel at x=0,y=0 to be green.
unicorn.set_pixel(0,0,0,255,0)

# This sets the pixel at x=0,y=0 to be blue.
unicorn.set_pixel(0,0,0,0,255)

# You will notice that none of the above commands work when you run them. That is because they only set the pixel to a color.
# They do not show them! Computers do exactly what you tell them to do - nothing more!
# To "show" a pixel, use the show command from the Unicorn HAT package! It does not need any arguments.
unicorn.show()

# And of course the opposite is to shut it off!
unicorn.off()

# Notice when you turn on an LED, and you try to change it, it doesn't change. You have to run show every time!
# You can enter these one after another in a Python prompt to change the colors:
unicorn.set_pixel(0,0,255,255,255)
unicorn.show() # Now it's white!
unicorn.set_pixel(0,0,255,0,0)
unicorn.show() # Now it's red!
unicorn.set_pixel(0,0,0,255,0)
unicorn.show() # Now it's green!
unicorn.set_pixel(0,0,0,0,255)
unicorn.show() # Now it's blue!








############################################################################################
# Now let's get doing some cooler stuff! ###################################################
############################################################################################

############################################################################################
# The For Loop #############################################################################
############################################################################################ 
# We can light up a whole row of LEDs like this:
# Make an array variable, containing 8 numbers (including 0!) that represent x coordinates
xCoords = [0,1,2,3,4,5,6,7]

# Loop through each coordinate, setting the x to that number in the set_pixel()
for x in xCoords:
  unicorn.set_pixel(x,0,255,255,255)

# Don't forget to turn the lights on!
unicorn.show()

############################################################################################
# Picking random LEDs ######################################################################
############################################################################################
# Import the randint function from the random package. randint allows us to generate random numbers.
from random import randint

# Now let's set the variable "x" to a random number between 0-7. This will be our x coordinate.
x = randint(0,7)

# Now let's set the variable "y" to a random number between 0-7. This will be our y coordinate.
y = randint(0,7)

# Now let's see which LED we picked!
unicorn.set_pixel(x,y,255,255,255)
unicorn.show()

# When you're ready, run the above again to see which LED turns on!
# If you're lucky, an LED will NOT turn on - that's because it chose an LED that is already on.

# If we want to "clear the board", we have to either run unicorn.clear() and unicorn.show() - or just use unicorn.off()!
# But where should you put it?
# If you put it at the end, the computer will run the script so fast you won't really see your LED turn on.
# But if you put it near the top - it will run first, then show your "new" LED so you can see it!
# Here's the complete script (try copy+pasting this over and over again):

from random import randint

unicorn.off()

x = randint(0,7)
y = randint(0,7)

unicorn.set_pixel(x,y,255,255,255)
unicorn.show()


############################################################################################
# The Sleep function #######################################################################
############################################################################################
# The sleep function tells the computer to wait for a certain number of seconds.
# First we import it from the time package:
import time

# Now we tell the computer to wait 5 seconds. You can change the 5 to any integer (above 0 - we aren't time travelling).
time.sleep(5)

# You'll notice your prompt will disappear for a while, then come back. Boring, but it works - and we'll use it a lot later!

############################################################################################
# Comparison Operators and Boolean Values ##################################################
############################################################################################
# "True" and "False" are called Boolean values
# For example, type "1 == 1" in your interpreter - it will say "True" back to you because 1 does equal 1.
# Now try to trick your computer! Enter in "1 == 2"... False!

# Check all these out!
1 == 1 # True! 1 does equal 1
1 < 5 # True! 1 is less than 5
10 > 4 # True! 10 is greater than 4
10 >= 10 # True! 10 is greater than or equal to 10
10 >= 9 # True! 10 is greater than or equal to 9
10 <= 10 # True! 10 is less than or equal to 10
10 <= 11 # True! 10 is less than or equal to 11
(2 + 2) == 4 # True! 2 plus 2 is 4
(3 * 3) == 9 # True! 3 times 3 is 9
(9 / 3) == 3 # True! 9 divided by 3 is 3
(4 ** 2) == 16 # True! 4 to the power of 2 -- also said is 4 squared -- is 16 

# Now try lying!
(1 + 1) == 3 # False! 1+1 isn't 3
5 <= 3 # False! 5 is not less than or equal to 3

# You can get pretty complicated! Don't forget BEDMAS!
((2 + 2)*4 + (7-3)*3) / 5 == 5 # True!

# You can explicitly use the values "True" and "False" as well!
(2 == 2) == True
((1 + 1) == 3) == False # True! 1 plus 1 is 3... is False... which is True!
True == True # True!
True == False # False!

############################################################################################
# The While Loop ###########################################################################
############################################################################################
# The while loop does SOMETHING, like our for-loop, WHILE a CONDITION is True!
# Let's take a look at one and then review it:
while 1 + 1 == 2:
  print("It's true!")
  time.sleep(1)

# What the above command does it EVALUATES the CONDITION. In this case, 1 + 1 is 2 -- so it is TRUE
# 1. WHILE the CONDITION is True, constantly execute the SOMETHING (called a function block) below
# 2. print "It's True" and wait a second
# 3. Now that the function block is over, re-evaluate the CONDITION
# 4. If it's still true (which it is! 1+1 is always 2), run the function block again!
# 5. print "It's True" and wait a second
# 6. Now that the function block is over, re-evaluate the CONDITION
# 7. If it's still true (which it is! 1+1 is always 2), run the function block again!
# ...
# ...
# And on and on and on!

# What about this one?
x = 1
while x < 10:
  print(x)
  x += 1

# What is "x += 1"? It means increment "x" by 1!
# So this script starts with x at 1
# Then it runs the while loop
# x is currently less than 1, so it executes the function block
# The function block prints x, then increments it by 1.
# Now x is 2, so it is less than 10 still, and runs the function block again.
# When will the while loop stop?
# When it's at 10, of course! "10 > 10" would be False, so the while loop would stop executing.

############################################################################################
# Putting it all together - Random lights! #################################################
############################################################################################
# What does this script do? Try to read it out loud before you run it.
# And when you do run it - press the Ctrl+C buttons on your keyboard to stop it.

############### BEGIN SCRIPT ####################
# Import our packages
import unicornhat as unicorn
import time
from random import randint

# Setup the Unicorn HAT
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

# Where the magic happens!
while(True):
  x = randint(0,7)
  y = randint(0,7)
  unicorn.off()
  unicorn.set_pixel(x,y,255,255,255)
  unicorn.show()
  time.sleep(1)

############### END SCRIPT ####################
  