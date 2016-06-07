
# coding: utf-8

# # Some meta comments
# 
# * My teaching feedback
#  * References to the future are mostly just abstract without a mental map.
#  * Same is true with references to other programming languages if you are not
#  familiar with them.
#  * Focus on one teaching object at a time.
# * Devices in class room
# * Why tutorials?

# ### Recap: while loops and lists

# #### What does it do?

# In[ ]:

count = 0
while count < 100:
    count += 1
count


# #### Q. What would this program print?

# Rather than type in long lists, we can use while loops:

# In[ ]:

#
# Initializations first
#
massRatioList = []         # Creates an empty list
massRatioValue = 1   # For the conditional
massRatioMax = 15   # Also for the conditional
#
# And the while loop:
# 
while massRatioValue <= massRatioMax:  # Note the colon!
    massRatioList.append(massRatioValue)   # Note the indentation!
    massRatioValue += 1


# In[ ]:

print(massRatioList)
print(massRatioValue)


# ## Today: for loops and lists, list comprehensions, tuples

# For loops operate on elements in a list.

# Basic structure:
# 
# ```python
# for <element> in <list>:
#     <do something with element>
# ```    
# <element> will be a variable name assigned to 
# individual elements in <list>
#     
# as opposed to while loops:
# 
# ```python
# while <condition is True>:
#     <do something>
# ```

# In[ ]:

for massRatio in massRatioList:  # Note the colon!
    print(massRatio) # Note the indent!

massRatio


# In[ ]:

for massRatio in massRatioList:  # Note the colon!
    print('massRatioList element = {}'.format(massRatio)) # Note the indent!

print('\nmassRatioList has {} elements!'.format(len(massRatioList)))
massRatio


# Note that you do _**not**_ have to 
# * know the length of the list
# * define a walking index.

# Let's use a for loop to make a table of mass ratios and gravitational forces:

# In[ ]:

# First, initialize variables
G       = 6.67e-11           # Grav. const.
mEarth  = 5.97e24            # Earth mass
mPerson = 70                 # Person mass 
radius  = 6.37e6             # Earth radius

massRatioList  = []          # Creates an empty list
massRatioValue = 1           # First mass ratio value
massRatioMax   = 15          # Last mass ratio value

# Create a list of mass ratios using a for loop
for massRatioValue in range(massRatioValue, massRatioMax + 1):   # Note the "+ 1"
    massRatioList.append(massRatioValue)

# Make a header for the table
print("# Mass-Ratio\tForce")

# Calculate the force for each mass ratio
for massRatio in massRatioList:
    force = G * massRatio * mEarth * mPerson / radius**2  

    # print contents of table line-by-line
    print("{}\t\t{:.2f}".format(massRatio, force))


# Note, how the force value automatically became a float, how it should be.
# 
# ### While loop implementation of a for loop
# 
# A simple for loop:

# In[ ]:

for massRatio in massRatioList:
    print(massRatio)


# Can also be implemented as a while loop:

# In[ ]:

index = 0   # Remember that the index starts with zero!
while index < len(massRatioList):
    print(massRatioList[index])
    index += 1


# This is a little less compact, but very intuitive.
# 
# #### Q. What is the value of index at the end (trace it!)?

# In[ ]:

index


# #### Interlude: make print work `side-ways`
# 
# #### Q. How could I learn about the ability's of print?
# 
# ### The built-in help system
# IPython and therefore its kernel here in Jupyter has a built-in help system.
# It depends on code author to fill in these docstrings (I show you how later.)
# 
# Enter help system by calling `object?`. In Jupyter a sub-window appears. When done reading you leave it by pressing `q` or clickin the `x` in the upper right corner.
# 
# Example: Learn how to make `print` print `side-ways`.

# In[ ]:

get_ipython().magic('pinfo print')


# In[ ]:

index = 0   # Remember that the index starts with zero!
while index < len(massRatioList):
    print(massRatioList[index], end=' ')
    index += 1


# ### The "range" function
# 
# An easy way to populate lists!
# 
# (In case you haven't noticed, there are already Python
# functions to do most things!)
# 
# Syntax:  range(n)
#   generates integers 0, 1, 2, ... n-1
# 
# Syntax: range (start, stop, step) 
#   generates from start to stop-1 with stepsize = step
#   If step is not specified, it is assumed to be 1.
#   
# #### Python 3 to 2 difference:
# Python 3 returns a generator for the list, not the list itself.
# 
# That means, if you want to see the list, it needs to be fully generated. To enforce this, convert the generator with the list funcion:

# In[ ]:

mygenerator = range(10)  # note how the print out also shows the default 0 starting value.
print(mygenerator)
mylist = list(mygenerator)
mylist


# In[ ]:

get_ipython().magic('pinfo range')


# #### Q. What does this generate?

# In[ ]:

print(list(range(-10, 2, 2)))
print(list(range(-5)))


# #### Q. Why is the last list empty?

















# #### A. Because the default values don't match.
# 
# Calling range() with only 1 value means it is intepreted as STOP value, with START assumed to be 0 and STEP to be +1. 
# 
# So, 
# ```python
# range(-5)
# ``` 
# is the same as 
# ```python
# range(0,-5,1)
# ```
# See why the list is empty?
# 
# Does this work?

# In[ ]:

list(range(0, -5))


# No, because the last default value is -1!
# We wanted:

# In[ ]:

list(range(0, -5, -1))


# For fun: using a function as an argument:

# In[ ]:

print(list(range(-10, 0, 2)))
len(range(-10, 0, 2))


# For our mass ratio list example:

# In[ ]:

massRatioList = []
for massRatio in range(1, 11, 1):
    massRatioList.append(massRatio)
massRatioList


# #### Q. What could we simplify now, knowing about the range function?

















# Use `range()` for the massRatioList itself!

# In[ ]:

massRatioList = list(range(1,11))
massRatioList


# ### The "enumerate" function

# Often, you'll want the indices and the list element values, to steer or access other values in other lists. Python has a short-cut function for this sort of thing: `enumerate`
# 
# Note: This is better Python style than to create your index yourself and use that to access elements in the array.
# So, this is bad(-ish):

# In[ ]:

for i in range(len(massRatioList)):
    print(i, massRatioList[i])


# This is better:

# In[ ]:

for i, massRatio in enumerate(massRatioList):  # enumerate returns both the index and the item
    print(i, massRatio)


# In[ ]:

# Equivalently (but not exactly the same):

for stuff in enumerate(massRatioList):
   print(stuff[0], stuff[1])


# Python tries to be helpful here! As learned above, `enumerate` returns both the index and the current item for the loop.
# 
# It could have thrown you an error, because you only `catch` one value. Instead, in Python, it stores `too many items` in a new compound item:

# In[ ]:

# Notice the parentheses.
# What kind of variable type is stuff?

type(stuff)


# In[ ]:

print(stuff)


# Tuples are the so called immutable versions of lists. Useful if you want to make sure you don't accidently change them while using them:

# In[ ]:

a = [1,2]
a


# In[ ]:

a[0] = 3
a


# In[ ]:

a = tuple(a)
a


# In[ ]:

print(t[0])


# In[ ]:

t[0] = 8


# ### Processing lists simultaneously with for loops

# The following construction is a bit lengthy (with 3 loops),
# but it shows how multiple lists (massRatioList and forceList) 
# can be processed simultaneously with for loops

# Good mnemonic for lists: Use PLURAL!

# In[ ]:

massRatios = range(5)


# In[ ]:

for massRatio in massRatios:
    print(massRatio, end=' ')


# In[ ]:

massRatios  = []        # Initialize.Why? If it's not there, can't append!
numElements    = 10        # Number of elements
massRatioMin   = 1      # Minimum mass ratio
massRatioMax   = 10      # Maximum mass ratio
massRatioDelta = (massRatioMax - massRatioMin) / (numElements - 1)   # Mass ratio increment

Now, construct massRatios:
# In[ ]:

for index in range(0, numElements):
    massRatio = massRatioMin + index * massRatioDelta
    massRatios.append(massRatio)
    print(index, massRatio)


# Now, calculate the forces using massRatios:

# In[ ]:

G         = 6.67e-11         # Gravitational constant
mEarth    = 5.97e24          # Earth mass
mPerson   = 70               # Person mass 
radius    = 6.37e6           # Earth radius
forces = []               # Empty list -- I don't have to specify its length

for massRatio in massRatios:
    force = massRatio * G * mEarth * mPerson / radius**2  
    forces.append(force)

Finally, to print the table:
(demonstrating processing lists simultaneously)
# In[ ]:

print("Index\tM_Ratio\tForce")  # note how special characters are tightly embedded into the string

#for index in range(min(len(massRatioList), len(forceList))):
for index in range(len(massRatios)):
    massRatio = massRatios[index]
    force = forces[index]
    print('{}\t{:.1f}\t{:.2f}'.format(index, massRatio, force))


# In[ ]:

a = range(1,11)
b = range(21,31 )


# In[ ]:

list(a)


# In[ ]:

list(b)


# In[ ]:

for itema, itemb in zip(a,b):
    print(itema, itemb)


# Above the index is not used for calculations, therefore there is a better way to do it: Use zip to combine lists in a 'zipper' like fashion.
# 
# > The automatic unpacking of tuples can never have too many receivers, but it can too few!

# In[ ]:

print("Index\tm_Ratio\tForce")  # note how special characters are tightly embedded into the string

#for index in range(min(len(massRatioList), len(forceList))):
for i, massRatio, force in enumerate(zip(massRatios, forces)):
    print('{}\t{:.1f}\t{:.2f}'.format(i, massRatio, force))


# In[ ]:

print("Index\tm_Ratio\tForce")  # note how special characters are tightly embedded into the string

#for index in range(min(len(massRatioList), len(forceList))):
for i in enumerate(zip(massRatios, forces)):
    print('{}\t{:.1f}\t{:.2f}'.format(i, massRatio, force))


# In[ ]:

print("Index\tm_Ratio\tForce")  # note how special characters are tightly embedded into the string

#for index in range(min(len(massRatioList), len(forceList))):
for i, (massRatio, force) in enumerate(zip(massRatios, forces)):
    print('{}\t{:.1f}\t{:.2f}'.format(i, massRatio, force))


# ### List comprehension
Really, really compact way of populating lists:
# In[ ]:

mylist = []
for i in range(10):
    mylist.append(i)
mylist


# can be written as:

# In[ ]:

mylist = [i**2 for i in range(10)]
mylist


# In[ ]:

numElements = 10

massRatios = [1.0 + index for index in range(numElements)]          # list comprehension!
forces     = [massRatio * G * mEarth * mPerson / radius**2              for massRatio in massRatios]


# Wow, that is compact!  Two lines!  Did it work?

# In[ ]:

print("Mass Ratio\tForce")  # note that "Mass Ratio" is so long, it swallows one \t from below.

for massRatio,force in zip(massRatios, forces):
    print('{:.1f}\t\t{:.2f}'.format(massRatio, force))


# ### Learn how fast your code works

# In[ ]:

get_ipython().run_cell_magic('timeit', ' # this is called "IPython magic"', 'massRatios = [0] * numElements\nforces     = [0] * numElements\n\n#  Using a single for loop, populate the two lists\nfor index in range(len(massRatios)):\n    #  Calculate the mass ratio\n    massRatios[index] = massRatioMin + index * massRatioDelta\n\n    #  Calculate the force\n    forces[index] = massRatioList[index] * G * mEarth * mPerson / radius**2')


# In[ ]:

get_ipython().magic('pinfo %%timeit')


# In[ ]:

get_ipython().run_cell_magic('timeit', '', 'numElements = 10\n\nmassRatios = [1.0 + index for index in range(numElements)]          # list comprehension!\nforces     = [massRatio * G * mEarth * mPerson / radius**2 for massRatio in massRatioList]')


# In Python 2 the shorter version was 26% faster, in Python 3 not much.
# 
# While writing compact code is elegant, it may come at the cost of readability. 
# 
# Use with caution! 
# 
# Advice: err on the side of easily comprehensible code.

# #### Q. When might you use a while loop instead of a for loop?

















# #### Q. When might you use a for loop instead of a while loop?

















# If you don't have a tidy data structure to iterate through, or you don't have a generator function (like `range()`) that drives your processing, you must use `while`.

# In[ ]:



