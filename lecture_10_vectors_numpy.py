
# coding: utf-8

# # Array Computing

# ## Terminology
# 
# #### List
# 
# * A sequence of values that can vary in length.
# * The values can be different data types.
# * The values can be modified (mutable).
# 
# 
# #### Tuple
# 
# * A sequence of values with a fixed length.
# * The values can be different data types.
# * The values cannot be modified (immutable).
# 
# #### Array
# 
# * A sequence of values with a fixed length.
# * The values cannot be different data types.
# * The values can be modified (mutable).
# 
# #### Vector:  A 1 dimensional (1D) array.
# 
# #### Matrix: - A 2 dimensional (2D) array.

# Arrays are like lists but less flexible and more 
# efficient for lengthy calculations (one data type, 
# stored in the same location in memory).
# 
# But first:  
# 
# ## VECTORS -- very simple arrays
# 
# Vectors can have an arbitrary number of components,
# existing in an n-dimensional space.
#  
#     (x1, x2, x3, ... xn)
#  
# Or 
# 
#     (x0, x1, x2, ... x(n-1)) for Python...
# 
# In Python, vectors are represented by lists or tuples:
# 
# #### Lists:

# In[ ]:

x = 2
y = 3

myList = [x, y]
myList


# #### Tuples:

# In[ ]:

myTuple = (-4, 7)
myTuple


# ### Mathematical Operations on Vectors
# 
# Review of vector operations: textbook sections 5.1.2 & 5.1.3
# 
# In computing:
# 
#     Applying a mathematical function to a vector 
#     means applying it to each element in the vector.
#     (you may hear me use the phrase "element-wise,"
#     which means "performing some operation one element
#     at a time")
# 
# **However, this is not true of lists and tuples**

# #### Q. What do these yield?

# In[ ]:

numList  = [0.0, 1.0, 2.0]
numTuple = (0.0, 1.0, 2.0)


# In[ ]:

2 * numList


# In[ ]:

2 * numTuple


# In[ ]:

2.0 * numList


# ### Vectors in Python programming

# Our current solution: 
# * using lists for collecting function data
# * convert to NumPy arrays for doing math with them.
# 
# As an example, a falling object in Earth's gravity:

# In[ ]:

def distance(t, a = 9.8):
    '''Calculate the distance given a time and acceleration.
       
       Input:  time in seconds <int> or <float>,
               acceleration in m/s^2 <int> or <float>
       Output: distance in m <float>
    '''
    return 0.5 * a * t**2

numPoints = 6                       # number of points
delta     = 1.0 / (numPoints - 1)   # time interval between points

# Q. What do the two lines below do?  

timeList = [index * delta for index in range(numPoints)]
distList = [distance(t) for t in timeList]


# In[ ]:

print("Time List:    ", timeList)
print("Distance List:", distList)


# #### Repeat on your own: stitching results together:

# In[ ]:

timeDistList = []
for index in range(numPoints):
    timeDistList.append([timeList[index], distList[index]])

for element in timeDistList:
    print element


# Or using zip, we did this already before:

# In[ ]:

timeDistList2 = [[time, dist] for time, dist in zip(timeList, distList)]

for element in timeDistList2:
    print(element)

What zip does:
# In[ ]:

daveList = range(5)
for element in zip(timeList, distList):
    print(element)
list(zip(timeList, distList, daveList))


# When to use lists and arrays?
# 
# In general, we'll use lists instead of arrays when elements have to be added (e.g., we don't know how the number of elements ahead of time, and must use methods like append and extend) or their types are heterogeneous.
# 
# Otherwise we'll use arrays for numerical calculations.

# ### Basics of numpy arrays

# Characteristics of numpy arrays:
# 
#   1. Elements are all the same type
# 
#   2. Number of elements known when array is created
# 
#   3. Numerical Python (numpy) must be imported to 
#      manipulate arrays.
# 
#   4. **All array elements are operated on by numpy,
#      which eliminates loops and makes programs
#      much faster.**
# 
#   5. Arrays with one index are sometimes called vectors 
#      (or 1D arrays). Arrays with two indices are
#      sometimes called matrices (or 2D arrays).
Some numpy functionality and standard usage:
# In[ ]:

import numpy as np


# To convert a list to an array use the array method:

# In[ ]:

myList  = [1, 2, 3]
myArray = np.array(myList)

print(type(myArray))
myArray


# Note the type!

# To create an array of length n filled with zeros (to be filled later):

# In[ ]:

get_ipython().magic('pinfo np.zeros')


# In[ ]:

myArray = np.zeros(10)
myArray


# #### To create arrays with elements of a type other than the default float, use a second argument:

# In[ ]:

myArray = np.zeros(5, dtype=int)
myArray


# We often want array elements equally spaced by some interval (delta).  
# 
# numpy.linspace(start, end, number of elements) does this:
# 
# #### NOTE ####  HERE,  THE "end" VALUE IS NOT (end - 1)  #### NOTE ####

# In[ ]:

zArray = np.linspace(0, 5, 6)
zArray


# #### Q. What will that do?

# Array elements are accessed with square brackets, the same as lists:

# In[ ]:

zArray[3]


# Slicing can also be done on arrays:

# #### Q. What does this give us?

# In[ ]:

yArray = zArray[1:4]
yArray


# For reference below:

# In[ ]:

zArray


# Let's edit one of the values in the z array

# In[ ]:

zArray[3] = 10.0
zArray


# Now let's look at the y array again

# In[ ]:

yArray


# The variable yArray is a **reference** (or **`view`** in Numpy lingo) to three elements (a slice) from zArray: element indices 1, 2, and 3.
# 
# Here is a blog post which discusses this issue nicely:
# 
# http://nedbatchelder.com/text/names.html
# 
# Reason this is of course memory efficiency: Why copy data if not necessary?

# In[ ]:

lList = [6, 7, 8, 9, 10, 11]
mList = lList[1:3]

print(mList)
lList[1] = 10
mList


# > Do not forget this -- check your array values frequently if you are unsure!

# ### Computing coordinates and function values
# 
# Here's the distance function we did previously:

# In[ ]:

def distance(t, a = 9.8):
    '''Calculate the distance given a time and acceleration.
       
       Input:  time in seconds <int> or <float>,
               acceleration in m/s^2 <int> or <float>
       Output: distance in m <float>
    '''
    return 0.5 * a * t**2

numPoints = 6                       # number of points
delta     = 1.0 / (numPoints - 1)   # time interval between points

timeList = [index * delta for index in range(numPoints)]   # Create the time list
distList = [distance(t) for t in timeList]                 # Create the distance list


# We could convert timeList and distList from lists to arrays:

# In[ ]:

timeArray = np.array(timeList)
distArray = np.array(distList)

print(type(timeArray), timeArray)
print(type(distArray), distArray)


# We can do this directly by creating arrays (without converting from a list) with np.linspace
# to create timeArray and np.zeros to create distArray.
# 
# (This is merely a demonstration, not superior to the above code for this simple example.)

# In[ ]:

def distance(t, a = 9.8):
    '''Calculate the distance given a time and acceleration.
       
       Input:  time in seconds <int> or <float>,
               acceleration in m/s^2 <int> or <float>
       Output: distance in m <float>
    '''
    return 0.5 * a * t**2

numPoints = 6                       # number of points

timeArray = np.linspace(0, 1, numPoints)   # Create the time array
distArray = np.zeros(numPoints)            # Create the distance array populated with 0's

print("Time Array:          ", type(timeArray), timeArray)
print("Dist Array Zeros:    ", type(distArray), distArray)

for index in range(numPoints):
    distArray[index] = distance(timeArray[index])   # Populate the distance array with calculated values

print("Dist Array Populated:", type(distArray), distArray)


# ### Vectorization -- one of the great powers of arrays

# The examples above are great, but they doesn't use the computation power of arrays by operating on all the elements simultaneously!
# 
# Loops are slow. 
# Operating on the elements simultaneously is much faster (and simpler!).
# 
# "Vectorization" is replacing a loop with vector or array expressions.

# In[ ]:

def distance(t, a = 9.8):
    '''Calculate the distance given a time and acceleration.
       
       Input:  time(s) in seconds <int> or <float> or <np.array>,
               acceleration in m/s^2 <int> or <float>
       Output: distance in m <float>
    '''
    return 0.5 * a * t**2

numPoints = 6                              # number of points

timeArray = np.linspace(0, 1, numPoints)   # Create the time array
distArray = distance(timeArray)            # Create and populate the distance array using vectorization

print("Time Array:", type(timeArray), timeArray)
print("Dist Array:", type(distArray), distArray)


# What just happened?
# 
# Let's look at what the function "distance" is doing to the values in timeArray

# In[ ]:

numPoints = 6   # Number of points
a = 9.8         # Acceleration in m/s^2

timeArray = np.linspace(0, 1, numPoints)  # The values a created like before
print("Original ", timeArray)

timeArray = timeArray**2                  # Once in the function, they are first squared
print("Squared  ", timeArray)
print(distArray)

timeArray = timeArray * 0.5               # Next they are multiplied by 0.5
print("Times 0.5", timeArray)

timeArray = timeArray * a                 # Finally, they are multiplied by a and the entire modified
print("Times a  ", timeArray)                # array is returned


# Caution: numpy has its own math functions, such as sin, cos, pi, exp, and some of these are slightly different from Python's math module.
# 
# Also, the math module does not accept numpy array as arguments, i.e. it is **NOT** vectorized.
# 
# Conclusiong: Use numpy built in math whenever dealing with arrays, but be aware that if you repeatedly (in a loop) calculate only 1 value at a time, the `math` library would be faster (because numpy has some overhead costs to do autmatically element-wise math).
# 
# So, do this for single calculations:

# In[ ]:

import math
math.sin(0.5)


# but do this for arrays:

# In[ ]:

np.sin([0.1, 0.2, 0.3, 0.4, 0.5])


# Extras:
# 
# Python names and references:
# 
# http://nedbatchelder.com/text/names.html
# 
# Generators:
# 
# https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
# 

# In[ ]:



