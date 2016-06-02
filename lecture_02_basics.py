
# coding: utf-8

# ### Saving your iPython notebook

# > File -> Save and Checkpoint
# 
# Can change the name also in that menu. But also possible via clicking the name above.
# 
# Talk about command mode and edit mode of cells. And the help window.

# ### Data Types:  Integers vs. Floats

# In[ ]:

10 / 3 # We provide integers

#  What will the output be?


# A float. 
# Note, that Python just automatically converts the result of division to floats, to be more correct.
# 
# Those kind of automatic data type changes were a problem in the old times, which is why older systems would rather insist on returning the same kind of data type as the user provided.
# These days, the focus has shifted on rather doing the math correct and let the system deal with the overhead for this implicit data type change.

# In[ ]:

1 / 10 + 2.0  # all fine here as well


# In[ ]:

4 / 2 # even so, mathematically not required, Python returns a float here as well.


# In[ ]:

4 // 2   # But if you need an integer to be returned, force it with //


# The reason why this automatic type conversion is even possible within Python is because it is a so called "dynamically typed" programming languages.
# 
# As opposed to "statically typed" ones like C(++) and Java.
# 
# Meaning, in Python this is possible:

# In[ ]:

a = 5
a


# In[ ]:

a = 'astring'
a


# I just changed the datatype of `a` without deleting it first. It was just changed to whatever I need it to be.
# 
# # But remember:

# In[ ]:

from IPython.display import YouTubeVideo
YouTubeVideo('b23wrRfy7SM')


# (read [here](http://nbviewer.jupyter.org/github/ipython/ipython/blob/1.x/examples/notebooks/Part%205%20-%20Rich%20Display%20System.ipynb), if you are interested in all the multi-media display capabilities of the Jupyter notebook.)
# 
# ### A note about names and values

# In[ ]:

x = 10
y = 2 * x
x = 25

y

#  What is the value of y? If you are surprised, please discuss it.


# Nice (lengthy / thorough) discussion of this:
# 
# http://nedbatchelder.com/text/names.html
# 
# *We haven't yet covered some of the concepts that appear in this blog post so don't panic if something looks unfamiliar.*

# ## Today: More practice with IPython & a simple formula

# Recall that to start an Jupyter notebook, simply type (in your Linux shell):
# 
#     $> jupyter notebook
# 
# or to open a specific file and keep the terminal session free:
# 
#     $> jupyter notebook filename.ipynb &
# 
# Note: Discuss cell types Code vs Markdown vs raw NB convert briefly

# ### Law of gravitation equation

# $F(r) = G \frac{m_1 m_2}{r^2}$

# $G = 6.67 \times 10^{-11} \frac{\text{m}^3}{\text{kg} \cdot \text{s}^2}$ (the gravitational constant)

# $m_1$ is the mass of the first body in kilograms (kg)

# $m_2$ is the mass of the second body in kilograms (kg)

# $r$ is the distance between the centers of the two bodies in meters (m)

# ### Example 1 - Find the force of a person standing on earth

# For a person of mass 70 kg standing on the surface of the Earth (mass $5.97 \times 10^{24}$ kg, radius 6370 km ([Earth fact sheet](http://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html))) the force will be (in units of Newtons, 1 N = 0.225 lbs):

# $$F(6.37 \times 10^{6}) = 6.67 \times 10^{-11} \cdot \frac{5.97 \times 10^{24} \cdot 70}{(6.37 \times 10^{6})^2}$$

# In[ ]:

6.67e-11 * 5.97e24 * 70 / (6.37e6)**2  
# remember: the return of the last line in any cell will be automatically printed


# Notice that I put spaces on either side of each mathematical operator. This isn't required, but enhances clarity. Consider the alternative:

# In[ ]:

6.67e-11*5.97e24*70/(6.37e6)**2


# ### Example 2 - Find the acceleration due to Earth's gravity (the g in F = mg)

# Using the gravitation equation above, set $m_2 = 1$ kg

# $$F(6.37 \times 10^{6}) = 6.67 \times 10^{-11} \cdot \frac{5.97 \times 10^{24} \cdot 1}{(6.37 \times 10^{6})^2}$$

# In[ ]:

6.67e-11 * 5.97e24 * 1 / (6.37e6)**2


# #### Q. Why would the above $F(r)$ implementation be inconvenient if we had to do this computation many times, say for different masses?

# #### Q. How could we improve this?

# In[ ]:

G = 55


# In[ ]:

G  = 6.67e-11
m1 = 5.97e24 
m2 = 70
r  = 6.37e6

F = G * m1 * m2 / r**2  #  white-space for clarity!

F  # remember: no print needed for the last item of a cell.


# #### Q. What do the "x = y" statements do?
Using descriptive names (good programming practice!):
# In[ ]:

G          = 6.67e-11
mass_earth  = 5.97e24
mass_object = 70
radius     = 6.37e6

force = G * mass_earth * mass_object / radius**2

force


# #### Q. Can you imagine a downside to descriptive variable names?

# ### Dealing with long lines of code

# Split long lines with a backslash (with no space after it, just carriage return):

# In[ ]:

force2 = G * massEarth *          massObject / radius**2


# In[ ]:

force2


# ### Reserved Words

# Using "reserved words" will lead to an error:

# In[ ]:

lambda = 5000     #  Some wavelength in Angstroms


# See p.10 of the textbook for a list of Python's reserved words. Some really common ones are:
# 
#     and, break, class, continue, def,
#     del, if, elif, else, except, False,
#     for, from, import, in, is, lambda, None,
#     not, or, pass, return, True, try, while

# ### Comments

# In[ ]:

#  Comments are specified with the pound symbol #
#  Everything after a # in a line is ignored by Python


# #### Q. What will the line below do?

# In[ ]:

print('this') # but not 'that'


# > As an approx value, it's good practice to comment about 50\% of your code!
# 
# But one can reduce that reasonbly, by choosing intelligle variable names.

# There is another way to specify "block comments": using two sets of 3 quotation marks ''' '''.

# In[ ]:

# Comments without ''' ''' or # create an error:
This is a comment
that takes
several lines.


# In[ ]:

#  However, in this form it does not, even for multiple lines:
#
'''
This is a really, super, super, super, super, super, super, super,
super, super, super, super, super, super, super, super, super,
long comment (not really).
'''
#
#  We will use block comments to document modules later!


# Notice that that `comment` was actually printed. That's because it's not technically a `comment` that is totally ignored, but just a multi-line string object.
# 
# It is being used in source code for documenting your code. Why does that work? Because that long multi-line string is not being assigned to a variable, so the Python interpreter just throws it away for not being used. But it's very useful for creating documented code!
# 
# ### Formatting text and numbers

# In[ ]:

from math import pi              # more in today's tutorial


# In[ ]:

#  With old style formatting

"pi = %.6f" % pi


# In[ ]:

#  With new style formatting. 
# It's longer in this example, but is much more powerful in general.
# You decide, which one you want to use.

"pi = {:.6f}".format(pi)


# In[ ]:

myPi = 3.92834234 
print("The Earth's mass is %.0f kilograms." % myPi)   # note the rounding that happens!
print("This is myPi: {} is awesome".format(str(int(myPi))))
# converting to int cuts off decimals


# Hard to read!!  (And, note the junk at the end.)

# Consider %x.yz
# 
#     % inside the quotes
#         - means a "format statement" follows
# 
#     x is the number of characters in the resulting string 
#         - Not required
# 
#     y is the number of digits after the decimal point 
#         - Not required
# 
#     z is the format (e.g. f (float), e (scientific), s (string))
#         - Required
# 
#     % outside and to the right of the quotes
#         - Separates text from variables -- more on this later
#         - Uses parentheses if there is more than one variable

# There is a list of print format specifications on p. 12 in the textbook
# 
#     %s          string (of ascii characters)
#     %d          integer
#     %0xd        integer padded with x leading zeros
#     %f          decimal notation with six decimals
#     %e or %E    compact scientific notation
#     %g or %G    compact decimal or scientific notation
#     %xz         format z right-justified in a field of width x
#     %-xy        same, left-justified
#     %.yz        format z with y decimals
#     %x.yz       format z with y decimals in a field of width x
#     %%          percentage sign

# ### The power of the new formatting
# 
# If you don't care about length of the print: The type is being chosen correctly for you.

# ### Some more examples

# In[ ]:

print(radius, force)  # still alive from far above!


# #### Q. What will the next statement print?

# In[ ]:

#  If we use triple quotes we don't have to 
#  use \ for multiple lines

print('''At the Earth's radius of %.2e meters,
the force is %6.0f Newtons.''' % (radius, force))


# In[ ]:

#  Justification

print("At the Earth's radius of %.2e meters, the force is %-20f Newtons." % (radius, force))


# Note when block comments are used, the text appears on 2 lines versus when using the \, the text appears all on 1 line.

# In[ ]:

print("At the Earth's radius of %.2e meters, the force is %.0f Newtons." % (radius, force))
print("At the Earth's radius of %.2e meters, the force is %i Newtons." % (radius, force))


# Note the difference between %.0f (float) and %i (integer) (rounding vs. truncating)
# 
# Also note, that the new formatting system actually warns you when you do something that would lose precision:

# In[ ]:

print("At the Earth's radius of {:.2e} meters, the force is {:.0f} Newtons.".format(radius, force))
print("At the Earth's radius of {:.2e} meters, the force is {:i} Newtons.".format(radius, force))


# In[ ]:

# Line breaks can also be implemented with \n

print('At the Earth radius of %.2e meters,\nthe force is\n%0.0f Newtons.' % (radius, force))


# Above would **not** be printed on 3 lines if used without the `print` command. Because the automatic notebook printing doesn't follow the same rules as the `print` command.
# 
# #### Q. What situations can you imagine in which printing information like this (i.e., full sentences, carefully formatted numbers) would be useful?

# ----

# ### Computer Science Glossary:

# Some terms we need to learn:
# (a few you know already, a few will appear in today's tutorial):
#     
#     OPERATING SYSTEM: the collection of programs that manage the hardware
#                       and software resources of the computer (e.g. Windows, Mac OS X, Linux)
#     
#     PYTHON: a program which interprets the text in our program files
#     
#     SYNTAX: the language of the programming language
#             (e.g. words, spelling, spacing, punctuation, etc)
# 
#     MODULE: a self-contained program called or used by other programs
#     
#     PACKAGE: a collection of modules
# 
#     LIBRARIES: modules and packages (like numpy)
#     
#     ALGORITHM: the steps the program takes to run
# 
#     SOURCE CODE: the text that constitutes the program
# 
#     STATEMENTS: a short collection of source code
#     
#     INPUT: the information that goes into the program
# 
#     OUTPUT: the result of the program (what comes out)
# 
