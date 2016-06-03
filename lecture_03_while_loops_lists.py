
# coding: utf-8

# ### Could not find kernel error?
# 
# If you ever see a "could not find a kernel for this notebook" error message, it will offer you a pull down menu for you to pick a fitting kernel.
# 
# Remember, `kernels` are the notebook's way to find the correct interpretor for the code you write into notebook cells. And these days this can be `R`, `Julia`, `Python` and several other things (Find the available kernels list [here](https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages)).

# ### Review on your own time:  A few "last" things about types
We did some examples last class which illustrated the difference between integers and floats. 

Let's do one more using the conversion between Fahrenheit and Celsius as a test case.

Recall the conversion formula:
# $T_C = \frac{5}{9} \left(T_F - 32 \right)$

# In[ ]:

tempF = 212.0
tempC = (5 / 9) * (tempF - 32.0)
tempC


# #### Q. What will be printed?
Depending on Python version!















# #### Q. What went wrong?
Nothing in Python 3, yay! ;)
# ### You can force variables to be certain types

# In[ ]:

x = 45
type(x)  #  Gives (returns) the type of variable


# In[ ]:

x = float(x)
print(type(x))
x


# #### Q. What will this produce?

# In[ ]:

x = 26.9
int(x)


# ### Review continued:  One "last" note on modules

# In[ ]:

from math import *
import math
print(sqrt(2))
math.sqrt(2)


# It's using the exact same library twice, you just told Python 2 different ways to get to it.
# And there's even a way to prove it: With the `id()` function:

# In[ ]:

id(sqrt)


# In[ ]:

id(math.sqrt)


# As you can see it's the same memory address (but this number is not necessarily the same on your computer), meaning the Python interpreter uses the exact same object twice, you just gave it 2 different names.
















# Another syntax is available to import modules:

# In[ ]:

#  Import math module and give it a new name
import math as m               #  Note the use of "as", a reserved word
m.sqrt(2)


# or specific functions within a module:

# In[ ]:

#  Import sqrt from math and give it a new name
from math import sqrt as sq
from math import pi as PIE
sq(2)

Recap of importing styles:

from module import function    
from module import *           
import module
import module as mod
from module import function as func
# # Today: Loops & Lists

# The point of loops is to compactly code repetitive tasks.
# For example, computing the gravitational force for multiple planetary masses.
#  
# Loops are an essential programming tool (this is why we program!).

# Python supports two types of loops:
# 
#   1. while loops
#   2. for loops

# ### While Loops (Section 2.1.2 in the book)

# #### Basic While Loop
# 
# <Talk about how Python knows what's in the loop>

# In[ ]:

x = 0                               # Initialize the variable x to 0

while(x != 3):                      # While (as long as) x is not equal to 3
    print("The value of x is", x)    # Print this to the screen
    x += 1                          # Increment x by 1 (add 1 to x)
    #  REPEAT!!!


# In[ ]:

print(x)

#  What is the value of x?


# #### Without a while loop

# In[ ]:

x = 0                          # Initialize the variable x to 0

print("The value of x is", x)   # Print this to the screen
x += 1                         # Increment x by 1 (add 1 to x)

print("The value of x is", x)   # Print this to the screen
x += 1                         # Increment x by 1 (add 1 to x)

print("The value of x is", x)   # Print this to the screen
x += 1                         # Increment x by 1 (add 1 to x)


# Recall the Gravitational Force Equation

# $$F(r) = G \frac{m_1 m_2}{r^2}$$

# In[ ]:

print('# Table of Gravitational Forces for Multiple Planet Masses\n')

#  Initialize variables - use meters and kilograms for units
G           = 6.67e-11         # Gravitational constant
mass_earth   = 5.97e24          # Earth mass
mass_person  = 70               # Person mass 
radius_earth = 6.37e6           # Earth radius

#  Begin calculation
mass1 = mass_earth

#  Print a header
print('# mass1/mass_earth  Force')

#  The loop ends when conditional mass1 <= (10.0 * massEarth) is no longer true
while(mass1 <= (10.0 * mass_earth)):                   #  Note the colon!
    force = G * mass1 * mass_person / radius_earth**2   #  All lines in the loop must be indented by
                                                      #  the same amount (iPython does it automatically)
#     print(str(mass1 / mass_earth) + " " + str(force))
    print("{mass_ratio}\t{force:7.2f}".format(mass_ratio=mass1 / mass_earth,
                                              force=force))
    mass1 = mass1 + mass_earth                         # Increment by Earth's mass

# No indent!  This line is executed after the loop is done
print('# Done')


# #### Q. What will this loop do ("trace" it)?















# The increment could have been done in shorthand

# In[ ]:

# Note that I have to reset mass1 here!!
mass1 = mass_earth

print('# mass1/mass_earth  Force')

while(mass1 <= (10.0 * mass_earth)):
    force = G * mass1 * mass_person / radius_earth**2
    
    print("{:18.1f} {:7.2f}".format(mass1 / mass_earth, force))
    
    #  mass1 = mass1 + mass_earth
    mass1 += mass_earth      #  Shorthand version of the line above.

'# Done'


# #### Q. What about this one? Can you predict any problems it may cause?
#  Example 1
x = 0
while(True):
    x = x + 1

#  Example 2
x = 0
while(x >= -1):
    x = x + 1

















NEVER, EVER DO THIS!! (well, not EXACTLY like this...)
# ### Infinite loops
If you create a while loop and the conditional never becomes false, you have just made yourself an infinite loop!

If you accidentally make an infinite loop in iPython notebook, go to "Kernel" then "Interrupt" in the toolbar above, then go to "Kernel" then "Restart".
# In[ ]:

#  How to prevent an infinite loop

maxCount = 10      #  A number that is more than your loop should ever do
count = 0          #  The current number your loop is on

#  Adding "and < maxCount" to the end of your conditional prevents infinite loops
while(True and count < maxCount):
    print("Loop count: " + str(count))
    count += 1     #  Increment your current loop count


# #### Q. How does this work?
Remember the basic structure of a while loop:

while <conditional statement>:
    <commands indented by 1 tab (usually 3 or 4 spaces)>
    <more commands>
    <more commands>
    <...>

<eventually exit loop and return to no indent>

*The <conditional statement> must evaluate to True or False.*
# ### INTERLUDE:  Boolean (logic) expressions (Section 2.1.3)

# Boolean expressions are conditional statements.  There are only 
# two possible values:  True or False
# 
# I've capitalized True and False because these are reserved words in Python.
#
x == y      # Is x equal to y?  (remember, a single = symbol is used to assign values)
#
x != y      # Is x not equal to y?
#
x >= y      # Is x greater than or equal to y?
#
x <= y      # Is x less than or equal to y?
#
x < y       # Is x less than y?
#
x > y       # Is x greater than y?
# #### Q. What is the value of this?

# In[ ]:

5 <= 10


# #### Q. What is the value of this?

# In[ ]:

5 >= 10

The reserved word "not" can be inserted in front of boolean expressions to change the value
to its opposite
# In[ ]:

not 5 >= 10


# #### Q. What is the value of this?

# See how readable Python is?

# Boolean expressions can be combined with "and", "or" and "not" to form compound conditional expressions.

# In[ ]:

5 <= 10 and 5 >= 10


# #### Q. How about this?

# In[ ]:

5 <= 10 or 5 >= 10


# ### Back to while loops
While loops are good to use when you don't know exactly how many times you need your loop to run.

They are very useful when asking the user for input.
# #### Example - User Input

# In[ ]:

import random

minNumber = 1
maxNumber = 10

#  Get a random number between 1 and 10
randomNumber = random.randint(minNumber, maxNumber)

userGuess = -1

while(userGuess != randomNumber):
    userPrompt = "Guess a number between " + str(minNumber) + " and " + str(maxNumber) + ": "
    
    userGuess = input(userPrompt)      #  Prompt the user
    
    userGuess = int(userGuess)

print("You have guessed the correct number! " + str(userGuess))


# #### Q. What happens if you enter a letter instead of a number?

# ### Lists (Section 2.2)
Lists are sequences of objects (which can be of different types) in a given order.

To define a list of mass ratios with ten elements
    ** (and indices running from 0 to 9): **

Referring to our previous gravitational force example:
# In[ ]:

massRatio = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
massRatio

We can access an element of the list by supplying its 
index in SQUARE BRACKETS (not parentheses or braces):
# In[ ]:

massRatio[3]


# #### Q. What will this print?

# In[ ]:

type(massRatio[3])


# Lesson learned: Python is zero-index based

# ### Modifying lists
We can append an element to the end of a list
using the append "method":
# In[ ]:

massRatio.append(11.0)
massRatio

Note the syntax "object.method(argument)"

Append acts like a function, but it is reached through an object.
That object (which we created) is a list called massRatio.We can insert a new element at a specific location too:
# In[ ]:

# This inserts 4.5 into index 4 of the list:
massRatio.insert(4, 4.5)

massRatio

We can delete an element:
# In[ ]:

del massRatio[4]


# #### Q. What will the next line produce?

# In[ ]:

massRatio


# ### List operations

# In[ ]:

# We can find out its length with len(object)
len(massRatio)

# Python uses [] to access elements and () to perform a function on an object.

Lists can be added:
# In[ ]:

massRatio = massRatio + [12.0, 13.0, 14.0]
massRatio

which is equivalent to using the method "extend":
# In[ ]:

massRatio.extend([15.0, 16.0, 17.0])
print("Extend", massRatio)

massRatio.append([18.0, 19.0, 20.0])
print("Append", massRatio)
print(massRatio[17][1])

The "index" function returns the index of the first appearance of a value
# #### Q. What will this produce?

# In[ ]:

massRatio.index(12.0)


# In[ ]:

#  And, this fails
massRatio.index(20.0)

The "in" keyword:
# In[ ]:

#  We can check if there is an element in a list.  The result of the check
#  is boolean:  True or False.

14.0 in massRatio


# In[ ]:

99.0 in massRatio


# In[ ]:

massRatio

Negative indices:
# In[ ]:

#  Negative indices start counting from the right (the end) of a list:
massRatio[-4]


# #### Q. What will this give us?

# ### Creating lists with while loops
We can create lists using a while loop.

Again, this is useful when you don't know how many elements
are going to be put in the list.
# In[ ]:

# Initializations first
massRatio      = []       #  Creates an empty list
massRatioValue = 1.0      #  For the conditional
massRatioMax   = 5.0      #  Also for the conditional

userInput = "BIG NOPE"

# And the while loop
while(userInput != "N" and massRatioValue <= massRatioMax):   #  Remember the colon!
    #  Remember to indent!
    massRatio.append(massRatioValue)
    massRatioValue += 1.0
    
    userInput = input("Add another mass ratio value? ")
    userInput = userInput.upper()

print("Finished creating the list massRatio!")


# #### Q. What is massRatio?

# In[ ]:

massRatio


# In[ ]:



