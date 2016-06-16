
# coding: utf-8

# ## Numerical Differentiation

# In[ ]:

get_ipython().magic('matplotlib inline')


# In[ ]:

import numpy as np
import matplotlib.pyplot as pl


# Applications:
# 
# 1. Derivative difficult to compute analytically
# 2. Rate of change in a dataset
#  - You have position data but you want to know velocity
# 3. Finding extrema
#  - Important for fitting models to data (**ASTR 3800**)
#  - Maximum likelihood methods
#  - Topology: finding peaks and valleys (place where slope is zero)

# ### Topology Example: South Pole Aitken Basin (lunar farside)

# Interesting:
#     
# 1. Oldest impact basin in the solar system
#   - Important for studies of solar system formation
# 2. Permananently shadowed craters
#   - High concentration of hydrogen (e.g., LCROSS mission)!
#   - Good place for an observatory (e.g., the Lunar Radio Array concept)!

# In[ ]:

from IPython.display import Image


# In[ ]:

Image(url='http://wordlesstech.com/wp-content/uploads/2011/11/New-Map-of-the-Moon-2.jpg')


# ### Question
# > Image you're planning a mission to the South Pole Aitken Basin and want to explore some permanently shadowed craters. What factors might you consider in planning out your rover's landing site and route?

# #### Most rovers can tolerate grades up to about 20%, For reference, the grade on I-70 near Eisenhower Tunnel is about 6%.

# ## Differentiation Review
Chalkboard!
# ### Numerical Derivatives on a Grid (Text Appendix B.2)
This function and the one below will calculate derivatives between pairs of points.
# In[ ]:

def forwardDifference(f, x, h):
    """
    A first order differentiation technique.
    
    Parameters
    ----------
    f : function to be differentiated
    x : point of interest
    h : step-size to use in approximation
    """
    return (f(x + h) - f(x)) / h   # From our notes

Beware of trying to calculate differences at the edges of arrays and creating index errors!

Second-order numerical derivative:
# In[ ]:

def centralDifference(f, x, h):
    """
    A second order differentiation technique.
    
    Also known as `symmetric difference quotient.
    
    Parameters
    ----------
    f : function to be differentiated
    x : point of interest
    h : step-size to use in approximation

    """
    return (f(x + h) - f(x - h)) / (2.0 * h)  # From our notes

This function will calculate the derivative of functions on a uniformly spaced grid using either the first or second-order derivative functions (i.e., either forwardDifference or centralDifference).
# In[ ]:

np.linspace(1,10,100).shape


# In[ ]:

def derivative(formula, func, xLower, xUpper, n):  
    """
    Differentiate func(x) at all points from xLower
    to xUpper with n *equally spaced* points.
    
    The differentiation formula is given by 
    formula(func, x, h).
    """
    h = (xUpper - xLower) / float(n)                 # Calculate the derivative step size
    xArray = np.linspace(xLower, xUpper, n)          # Create an array of x values
    derivArray = np.zeros(n)               # Create an empty array for the derivative values
    
    for index in range(1, n - 1):                   # xrange(start, stop, [step])
        derivArray[index] = formula(func, xArray[index], h)    # Calculate the derivative for the current
                                                               # x value using the formula passed in

    return (xArray[1:-1], derivArray[1:-1])    # This returns TWO things:
                                               # x values and the derivative values


# #### Notice that we don't calculate the derivative at the end points because there are no points beyond them to difference with.

# #### Q. So, what would happen without the [1:-1] in the return statement?

# In[ ]:

def derivative2(formula, func, xLower, xUpper, n):  
    """
    Differentiate func(x) at all points from xLower
    to xUpper with n+1 *equally spaced* points.
    The differentiation formula is given by 
    formula(func, x, h).
    """
    h = (xUpper - xLower) / float(n)                 # Calculate the derivative step size
    xArray = np.linspace(xLower, xUpper, n)          # Create an array of x values
    derivArray = np.zeros(n)               # Create an empty array for the derivative values
    
    for index in range(0, n):                       # xrange(start, stop, [step])
        derivArray[index] = formula(func, xArray[index], h)    # Calculate the derivative for the current
                                                               # x value using the formula passed in

    return (xArray, derivArray)    # This returns TWO things:
                                               # x values and the derivative values


# ### Example: Differentiate $\sin(x)$

# We know the answer:
# 
# $$\frac{d}{dx} \left[\sin(x)\right] = \cos(x)$$
Let's see if we reproduce this result numerically:
# In[ ]:

tau = 2*np.pi

x = np.linspace(0, tau, 100)

# Plot sin and cos
pl.plot(x, np.sin(x), color='k');
pl.plot(x, np.cos(x), color='b');

# Compute derivative using central difference formula
xder, yder = derivative2(centralDifference, np.sin, 0, tau, 10) 

# Plot numerical derivative as scatter plot
pl.scatter(xder, yder, color='g', s=100, marker='+', lw=2);
# s controls marker size (experiment with it)
# lw = "linewidth" in pixels


# #### Notice that the points miss the curve.

# #### Q. How can we improve the accuracy of our numerical derivative?

# In[ ]:

# Plot sin and cos
pl.plot(x, np.sin(x), color='k')
pl.plot(x, np.cos(x), color='b')

# Compute derivative using central difference formula
xder, yder = derivative2(centralDifference, np.sin, 0, tau, 100) 

# Plot numerical derivative as scatter plot
pl.scatter(xder, yder, color='g', s=100, marker='*', lw=2)  


# ### Example: Traversing A 1-D landscape
Altitude vs. position along some predetermined route.

Here, I've constructed a model 1-D landscape assuming 5 craters, with Gaussian shapes (of random width and amplitude) and random positions.
# Gaussian Equation: 
# 
# $$f(x)=A * e^{-\frac{(x-\mu)^2}{2*\sigma}}$$

# In[ ]:

numCraters = 5       # number of craters
widthMax   = 1.0     # maximal width of Gaussian crater
heightMin  = -1.0    # maximal depth of craters / valleys
heightMax  = 2.0     # maximal height of hills / mountains

# 1-D Gaussian
def gaussian(x, A, mu, sigma):
    return A * np.exp(-(x - mu)**2 / 2.0 / sigma**2)

# 1-D Gaussian (same thing using lambda)
#gaussian = lambda x, A, mu, sigma: A * np.exp(-(x - mu)**2 / 2. / sigma**2) 

# Create an array of linearly spaced x values
xArray = np.linspace(0, 10, 500)  # km

# Create an array of initially flat landscape (aka filled with 0's)
yArray = np.zeros_like(xArray)

# Add craters / mountains to landscape
for _ in range(numCraters):    # '_' is the so called dummy variable
    
    # Amplitude between heightMin and heightMax
    A = np.random.rand() * (heightMax - heightMin) + heightMin
    
    # Center location of the crater
    center = np.random.rand() * xArray.max()
    
    # Width of the crater
    sigma = np.random.rand() * widthMax
    
    # Add crater to landscape!
    yArray += gaussian(xArray, A=A, mu=center, sigma=sigma)

Plot our 1-D landscape:
# In[ ]:

pl.plot(xArray, yArray, color='k')
pl.xlabel('position [km]')
pl.ylabel('altitutde [km]')


# #### Q. Where should our spacecraft land? What areas seem accessible?

# #### Q. How do we find the lowest point? Highest? How could we determine how many "mountains" and "craters" there are?

















# In[ ]:

dydx = np.diff(yArray) / np.diff(xArray)


# #### Q. What do you think "diff" does?

# In[ ]:

arr = np.array([1,4,10, 12,5, 7])


# In[ ]:

np.diff(arr)



















# #### Q. What type of differentiation scheme does this formula represent? How is this different than our "derivative" function from earlier?

# In[ ]:

pl.plot(xArray[0:-1], dydx, color='r', label='slope')
pl.plot(xArray, yArray, color='k', label='data')

pl.xlabel('position [km]')
pl.ylabel('slope')
pl.plot([xArray.min(), xArray.max()], [0,0], color='k', ls=':')
#pl.ylim(-4, 4)
pl.legend(loc='best')


# #### Q. How many hills and craters are there?

# #### Q. Why did we use x[0:-1] in the above plot instead of x?
Imagine our rover can at best handle a slope of 0.5.
# In[ ]:

slopeTolerance = 0.5


# #### Q. Using the slope, how could we determine which places we could reach and which we couldn't?












How about some boolean logic?First a review:
# In[ ]:

myArray = np.array([0, 1, 2, 3, 4])                  # Create an array

tfArray = np.logical_and(myArray < 2, myArray != 0)  # Use boolean logic on array

print (myArray)               # Print original array
print (tfArray)               # Print the True/False array (from boolean logic)
print (myArray[tfArray])      # Print the original array using True/False array to limit values

Now back to the show
# In[ ]:

reachable = np.logical_and(dydx < slopeTolerance, dydx > -slopeTolerance)
unreachable = np.logical_not(reachable)


# In[ ]:

pl.plot(xArray, yArray, color='k')
pl.scatter(xArray[:-1][unreachable], yArray[:-1][unreachable], color='r', label='bad')
pl.scatter(xArray[:-1][reachable], yArray[:-1][reachable], color='g', label='good')

pl.legend(loc='best')
pl.xlabel('position [km]')
pl.ylabel('altitude [km]')


# ### Summary
1) Forward difference vs. central difference
2) Differentiating functions vs. differentiating discrete values
3) Using differences to find peaks and troughs in data.
# In[ ]:



