
# coding: utf-8

# ## Today: More on functions

# Final project posted.
# 
# Poll: When do you want Homework deadline? Friday lunch, to enable discussing HW on Friday? Or end of Friday?
Refresher:
# In[ ]:

from math import exp

# Could avoid this by using our constants.py module!
h = 6.626e-34  # MKS
k = 1.38e-23
c = 3.00e8

def intensity(wave, temp, mydefault=0):
    wavelength = wave / 1e10
    B = 2 * h * c**2 / (wavelength**5 * (exp(h * c / (wavelength * k * temp)) - 1))
    return B


# #### Q. Is the following call sequence acceptable?

# In[ ]:

mywave = 5000


# In[ ]:

intensity(mywave, temp=5800.0)














# No! The following are all OK!

# In[ ]:

print(intensity(5000.0, temp=5800.0))
print(intensity(wave=5000.0, temp=5800.0))
print(intensity(5000.0, 5800.0))

This runs, but gives the wrong result:
(assuming we want 5800 K blackbody, wavelength of 5000 A)

Q. Why?
# In[ ]:

intensity(5800.0, 5000.0)


# ### Keyword arguments
Function arguments can be given default values so that 
the arguments can be left out of the function call.
# In[ ]:

def testFunc(arg1, arg2, kwarg1=True, kwarg2=4.2):
    print(arg1, arg2, kwarg1, kwarg2)


# The first two arguments in this case are "positional arguments."
# 
# The second two are named "keyword arguments".
# 
# Keyword arguments must follow positional arguments in function calls.

# #### Q. What will this do?

# In[ ]:

testFunc(1.0, 2.0)
testFunc(1.0, 2.0, 3.0)  # NOTE! I do not HAVE TO use the keyword access!

Let's practice using an example from the book:
# $$f(t)=A \cdot e^{-at} \cdot \sin({\omega \cdot t})$$

# In[ ]:

from math import pi, exp, sin
tau = 2*pi

# t is positional argument, others are keyword arguments
def f(t, A=1, a=1, omega=tau):
    return A * exp(-a * t) * sin(omega * t)

v1 = f(0.01)  # Only the time is specified
v1


# #### Q. What will this yield? 

# In[ ]:

v1 = f(A=2, t=0.01)
v1

Here is a nice example from the book demonstrating
using a while loop, a function, and a TOLERANCE to sum an
infinite series to the needed precision. This is similar 
to our example with the sine curve from last week.
# $$e^x = \sum_{i=0}^{\infty} \frac{x^i}{i!}$$
i.e., approximate with N terms as:
# $$e^x \approx \sum_{i=0}^{N} \frac{x^i}{i!}$$

# In[ ]:

import math

def exponential(x, epsilon=1e-6):
    total = 1.0
    i = 1
    term = (x**i) / math.factorial(i)
    
    while abs(term) > epsilon:
        term = x**i / math.factorial(i)
        total += term
        i += 1
    
    return total, i

Notice how instead of comparing neighboring estimates of the sum as we did for the sine function last time (i.e., estimates using N and N+1 terms), we just look at how big the Nth term is.
# In[ ]:

total, i = exponential(2.4, epsilon=1e-2)
print(exponential(2.4, epsilon=1e-4))
print(exponential(2.4))
print(math.exp(2.4))

OK, we've now seen lots of examples of functions. 
# #### Q. What's missing? Have there been ambiguities in the functions we've written?
Consider our Planck function example:
# In[ ]:

from math import exp

h = 6.626e-34  # MKS
k = 1.38e-23
c = 3.00e8

def intensity(wave, temp):
    wavelength = wave / 1e10
    inten = 2 * h * c**2 / (wavelength**5 * (exp(h * c / (wavelength * k * temp)) - 1))
    return inten













# ### Doc-strings (review)
Document strings are inserted right below the function header
(def line) to describe the purpose of the function and what the 
arguments and return values are.  

Triple quotes allow the descriptions to span several lines.

Doc strings should include a description of the function,
a list of arguments, and an example.
# In[ ]:

import math
def exponential(x, epsilon=1e-6):  
    """
    This function calculates exp(x) to a tolerance
    of epsilon.

    Parameters
    ----------
    x :  exponent
    epsilon :  tolerance
    returns :  exp(x), number of terms include (after 1.0)

    Example from interactive shell:
    >>> sum, i = exponential(0.15)
    >>> print i-1, sum
    5, 1.16183422656
    """
    total = 1.0
    i = 1
    term = (x**i) / math.factorial(i)
    
    while abs(term) > epsilon:
        term = x**i / math.factorial(i)
        total += term
        i += 1
    
    return total, i


# In[ ]:

total, i = exponential(0.15)
i - 1, total


# #### Q. So, what should doc strings contain in general?
Python can extract the doc string to read:
(Must run above cell before this next one)
# In[ ]:

print(exponential.__doc__)

# How handy!!


# In[ ]:

expontential.

or:
# In[ ]:

help(exponential)

Nomenclature:

Function arguments/parameters are input
Returned objects are outputLet's fix-up our Planck function:
# In[ ]:

from math import exp

h = 6.626e-34  # MKS
k = 1.38e-23
c = 3.00e8

def intensity(wave, temp):
    """
    Compute the value of the Planck function.

    Parameters
    ----------
    wave : int, float
        Wavelength at which to compute Planck function, in Angstroms.
    T : int, float
        Temperature of blackbody, in Kelvin.

    Example
    -------
    Radiance at 5000 Angstrom, 5800 K blackbody:
    >>> radiance = I(wave=5000., T=5800.) 

    Returns
    -------
    Radiance of blackbody in W / sr / m^3.
    """
    
    wavelength = wave / 1e10
    inten = 2 * h * c**2 / (wavelength**5 * (exp(h * c / (wavelength * k * temp)) - 1))
    return inten


# ### Functions as arguments to other functions
Python can use functions as arguments of other functions.

The text has a numerical second derivative in an
example of a function calling a function:
# $$\frac{df(x)}{dx} \approx \frac{f(x-h) + f(x+h) - 2f(x)}{h^2}$$

# In[ ]:

def diff2(f, x, h=1e-6):
    """
    Calculates a second derivative.
    f:  the function (of one variable) to be differentiated
    x:  value at which the function is evaluated
    h:  small difference in x 
    """
    r = (f(x-h) + f(x + h) - 2.0 * f(x)) / float(h**2)
    return r

Now let's use it.
# We'll work with the following function:
# 
# $g(t) = t^2$

# In[ ]:

def g(t):
    return t**2


# In[ ]:

t = 3.0
gPrimePrime = diff2(g, t)


# #### Q. What should this yield?

# In[ ]:

print("Second derivative of g=t^4 evaluated at t=%g" % t)
"g(%f)=%.8g" % (t, gPrimePrime)


# ### Lambda functions
Functions can be defined in one line (which is convenient 
if they are short!) using the Python lambda function.
# In[ ]:

g = lambda t: t**2
print(g)
g(2.0)


# In[ ]:

def g(t):
    return t**2

This can also be done for multiple arguments.Syntax:

g = lambda arg1, arg2, arg, ...: expression

It lends itself nicely to function calls to functions:
# In[ ]:

# This simply calculates the second derivative of t^2 evaluated at t=1.
test = diff2(lambda t: t**2, 56) 
# Recall the first argument to diff2 was the function

test


# In[ ]:

def cubed(x):
    return x**3


# In[ ]:

cubed(2)


# In[ ]:

y = lambda x: x**3


# In[ ]:

y(2)


# In[ ]:

s = 'hans_gruber'


# In[ ]:

s.split('_')


# In[ ]:

df.sort().groupby().do_stuff(lambda x: x.split('-')[0])

