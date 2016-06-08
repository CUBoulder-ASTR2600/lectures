
# coding: utf-8

# # quick recap
# 
# You now have both `while` loop and `for` loop in your toolset.
# Let's look quickly at yesterday's last tutorial task.
# However, I also will also upload general solution notebook files later today)

# In[ ]:

for fIndex, y in enumerate(range(2, 5)):
    
    countdown = y
    yFactorial = 1
    
    wIndex = 0
    while countdown > 1:
        yFactorial *= countdown
        
        ##### CHECKPOINT! #####
        
        countdown -= 1
        wIndex += 1
    
    print("RESULT: %d! = %d" % (y, yFactorial))


# In[ ]:

# Question 3

print("%s %s %s %s %s" % ("fIndex", "y", "wIndex", "countdown", "yFactorial"))

for fIndex, y in enumerate(range(2, 5)):
    
    countdown = y
    yFactorial = 1
    
    wIndex = 0
    while countdown > 1:
        yFactorial *= countdown
        
        print("%-6i %1i %6i %9i %10i" % (fIndex, y, wIndex, countdown, yFactorial))
        
        countdown -= 1
        wIndex += 1
    
    #print "RESULT: %d! = %d" % (y, yFactorial)


# # Today
# 
# * Sublists
# * nested lists
# * Functions (the most fun object in Python in my mind)
# * global vs local variables
# * docstrings

# ## Extracting Sublists
# 
# Sometimes we want to operate on only parts of lists.
# The syntax for this is particularly simple:

# In[ ]:

# create our favorite massRatios:
massRatios = list(range(10))
massRatios


# In[ ]:

massRatios[2:7]


# This is called `slicing` and the 2 parameters required are separated by a colon `:`.
# 
# Similar to the parameters for the `range()` function, the starting number is `inclusive` while the ending number is `exclusive`.
# 
# When the 1st parameter is left out, the slice starts at the beginning of the list, when the last parameter is left out it goes until the end:

# In[ ]:

print(massRatios[:4])
print(massRatios[4:])


# Note how in the first case, the length returned is the same as the value of the index you provide, thanks to 0-based indexing.
# 
# Note, also, that thanks to the asymmetry of `inclusivity` for the start parameter vs `exclusivity` for the end parameter, you can use the same number twice to get both ends of a list, thisk creates easier to read code as well.

# In[ ]:

i = 5
print(massRatios[:i])
print(massRatios[i:])


# ## Nested lists
# 
# Python allows for nesting lists. This allows for finer substructure of data storage.
# For example, storing vectors in a list:

# In[ ]:

v1 = [0,1,2]
v2 = [7,8,9]


# In[ ]:

vectors = [v1, v2]
vectors


# When accessing elements, you can also just nest the indexing:

# In[ ]:

vectors[0][1]


# In[ ]:

vectors[1][-1]


# ## Functions
Functions are useful because they allow us to perform operations many times without
repeating code snippets, keeping programs shorter, more managable, and more organized.
 
We will start with the Planck function,
# $B_{\lambda}(T) = \frac{2 h c^2}{\lambda^5 \left[\exp\left(\frac{h c}{\lambda k T}\right) - 1 \right]}$

# where $h$ is Planck's constant, $c$ is the speed of light, 
# $k$ is Boltzmann's constant, $T$ is the blackbody temperature, and
# $\lambda$ is the wavelength.

# In[ ]:

# First, define the physical constants:
h = 6.626e-34  # J s, Planck's constant
k = 1.38e-23   # J K^-1, Boltzmann constant
c = 3.00e8     # m s^-1, speed of light
 
# Conversion between angstroms and meters
angPerM = 1e10
    
# The Planck function is a function of two variables;
# for now, we'll set T = 5,800 K, the photospheric temperature of the Sun
# and allow the wavelength to vary.
temp = 5800.0  

from math import exp

# Define the function using def:
 
def intensity1(waveAng):               # Function header
    waveM = waveAng / angPerM    # Will convert Angstroms to meters
    
    B = 2 * h * c**2 / (waveM**5 * (exp(h * c / (waveM * k * temp)) - 1))
    
    return B

# Units will be W / m^2 / m / ster

The above statement comprises the function body & return to the main program.
# In[ ]:

print('%e' % intensity1(5000.0))  # note the %e formatting string for exponent notation

Basic structure:

def function_name(argument):
    <do some stuff>
    ...
    
    <return stuff>
    
Notice especially: def, colon, indent    
Optional: argument (or "input": you'll hear people say both), return statement

NOTE: Without a return statement, the function will still return None. More on None to come!
# In[ ]:

def funcNoReturn(x):
    print("Answer:", x + 5)
    return x+5

y = funcNoReturn(6)
print("y =", y)

Next we'll create a list of wavelengths at which to evaluate the Planck function:
# In[ ]:

waveList = [3000 + 100 * i for i in range(41)]


# #### Q. What did the above command do?

# In[ ]:

waveList

Now, we'll create an intensity list using another list comprehension:
# In[ ]:

intensityList = [intensity1(wave) for wave in waveList]  
intensityList


# #### Q. What should the output of "intensityList" be?
For a nice print-out, make use of a for loop and the range function:
# In[ ]:

for index in range(len(waveList)):
    print('wavelength (Angstrom) = {}      Intensity (W m^-3 ster^-1) = {:.2e}'          .format(waveList[index], intensityList[index]))


# #### Q. What will the output look like?

# ### Local and Global variables
When I define a function in the following manner,
# In[ ]:

def intensity1(waveAng):                # Function header
    waveM = waveAng / angPerM    # Will convert Angstroms to meters
    
    B = 2 * h * c**2 / (waveM**5 * (exp(h * c / (waveM * k * temp)) - 1))
    
    return B

B is a local variable -- it only exists in the function IntensitySo this fails:
# In[ ]:

B

so does:
# In[ ]:

waveM

In contrast, h, k, c, and temp are global variables (defined above) and can 
be accessed anywhere in the program or notebook.

Notes on global and local variables:

  * Avoid local and global variables with the same name. (Works, but can be confusing)
  
  * When there are variables of the same name, Python first looks for a local variable,
    then a global variable, then a built-in function of that name.

  * Avoid changing global variables in functions, although Python has a utility
    for doing so:  the global function.
# #### Q. What will this print?

# In[ ]:

g = 10

def f(x):
    g = 11
    return x + g

f(5), g

But:
# In[ ]:

g = 10

def f(x):
    global g       # Now "g" inside the function references the global variable
    g = 11         # Give that variable a new value
    return x + g

f(5), g

Use of "global" is generally frowned upon (dangerous), but here it is for completeness.
# ### Functions with multiple arguments
The Planck function is a function of wavelength AND temperature.
# In[ ]:

def intensity2(waveAng, temp):   # 2nd version of function Intensity
    waveM = waveAng / angPerM
    B = 2 * h * c**2 / (waveM**5 * (exp(h * c / (waveM * k * temp)) - 1))
    return B


# In[ ]:

intensity2(5000.0, 5800.0)

"call sequence" simple, nothing fancy! Just comma-separated values to supply multiple arguments.But, you could also call the function with names for arguments:
# In[ ]:

intensity2(temp=5800.0, waveAng=5000.0)

or
# In[ ]:

intensity2(waveAng=5000.0, temp=5800.0)


# #### Q. Will this work (produce the same result)? 

# In[ ]:

intensity2(5800.0, 5000.0)

Functions are useful beyond just evaluating equations.

Here's another example (albeit another mathematical one).

We needed a wavelength list for the previous example with the Planck function; 
let's write a function to make that for us.
# In[ ]:

def waveListGen(minWave, maxWave, delta):
    waveList = []
    
    wave = minWave
    
    while wave <= maxWave:
        waveList.append(wave)
        wave += delta
    
    return waveList


# #### Q. What will this do?

# In[ ]:

waveList = waveListGen(3000, 5000, 200)
waveList

Note that the waveListGen function we just wrote is more flexible than our previous approach,

wavelengthList = [3000.0 + 100.0 * i for i in range(41)]

since we can easily modify the start, stop, and wavelength spacing.

On the other hand, we could just use range:
# In[ ]:

list(range(3000, 5001, 200))


# ### Functions with multiple return values
Given a wavelength, we can return the frequency and the
value of the Planck function at that frequency:
# In[ ]:

# (Defined h, c, k above and imported math)

def intensity3(waveAng, temp):   # 3rd version of function Intensity
    waveM = waveAng / angPerM
    
    B = 2 * h * c**2 / (waveM**5 * (exp(h * c / (waveM * k * temp)) - 1))
    
    return (waveAng, B)


# In[ ]:

temp = 10000.0  # Hot A star or cool B star; brighter than a G star

waveAng, intensity = intensity3(6000.0, temp=temp)
waveAng, intensity   # notice the automatic packing of Python again

There must be two variables on the left-hand side of the assignment operator since
the function will return two variables, or else if there is only only variable it
will contain both values as a tuple (see cell below).

This is yet another instance of "unpacking," which we saw while using the "enumerate" 
function, and when working with tuples.
# In[ ]:

result = intensity3(6000.0, 10000.0)

print(result)
type(result)

We've already seen how to make nice table outputs, so let's do it here:
# In[ ]:

for wave in waveListGen(3e3, 4e3, 100):
    print('Wavelength (Angstroms) = %-10i Intensity (W m^-3 ster^-1) = %.2e'          % intensity3(wave, 1e4))

The %-10i prints real numbers with ten spaces, left justified.
By default (i.e., no minus sign), columns are right justified.Notice how compact that for loop is!

We initialized the list of wavelengths right in the for loop, then, passed the 
results of the calculation (using the function Intensity3) directly to string formatting.
This is possible because the Intensity3 returns a tuple!
# # Doc Strings:

# Doc strings are used to document functions.  They generally include:
# 
# * A description of the functionality of the function
# 
# * A list of arguments
# 
# * A description of outputs (returned values)
# 
# And, they serve as the help documentation!
# 
# They go right after the function header and are enclosed within triple quotes.

# In[ ]:

def force(mass1, mass2, radius):
    """
    Compute the gravitational force between two bodies.
    
    Parameters
    ----------
    mass1 : int, float
        Mass of the first body, in kilograms.
    mass2 : int, float
        Mass of the second body, in kilograms.
    radius : int, float
        Separation of the bodies, in meters.

    Example
    -------
    To compute force between Earth and the Sun:
    >>> F = force(5.97e24, 1.99e30, 1.5e11)

    Returns
    -------
    Force in Newtons : float
    """
    G = 6.67e-11
    
    return G * mass1 * mass2 / radius**2


# In[ ]:

result = force(5.97e24, 2.00e30, 1.5e11)
result


# In[ ]:

# To see the documentation for a function, use help:

help(force)


# or with the subwindow:

# In[ ]:

get_ipython().magic('pinfo force')


# ## Some important functionality review

# In[ ]:

# a = []          initialize an empty list
# a = [1., 2]     initialize a list
# a.append(elem)  add the elem object to the end of the list
# a + [5, 4]      concatenate (join) two lists
# a.insert(i, e)  insert element e at index i
# a[5]            acess the value of the element at index 5
# a[-1]           get the last list element value
# a[4:7]          slice list a
# del a[i]        delete list element with index i
# a.remove(e)     remove list element with value e (not index e)
# a.index('test') find the index where the element has the value 'test'
# 4 in a          find out whether 4 is in a
# a.count(4)      count how many times 4 is in a
# len(a)          return the number of elements in a
# min(a)          return the smallest element in a
# max(a)          return the largest element in a
# sum(a)          add all the elements in a
# sorted(a)       return a sorted version of list a
# reversed(a)     return a reversed version of list a
# a[1][0][4]      nested list indexing (3 dimensional list in this case)

