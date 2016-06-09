
# coding: utf-8

# # Making your own modules

# If a function will be used in multiple programs, it should be written 
# as a module instead. 
# 
# All one has to do is put the functions in a program_name.py
# file and import it (the whole thing) or the functions, then 
# use them in the main program.
# 
# Exactly the same way how you import and use other libraries.
# 
# ## Example
# Given mass and velocity, this function calculates the kinetic energy of a particle
# in meters/kilograms/seconds (mks) units.

# $$E_k = \frac{1}{2} \cdot mv^2$$

# In[ ]:

def eKinetic(mass, velocity):
    return 0.5 * mass * velocity**2


# In[ ]:

eKinetic(1, 10)


# #### Q. What will the output be?

# The following function calculates the x, y, and z accelerations 
# of a particle resulting from forces acting upon it given its mass.
# 
# All units are SI.

# $a=\frac{F}{m}$ rearranged from $F=ma$
# 
# > Note: These techniques are also related to some of the tasks in the homework and the final project.

# In[ ]:

def acceleration(xForce, yForce, zForce, mass):
    xAccel = float(xForce) / float(mass)
    yAccel = float(yForce) / float(mass)
    zAccel = float(zForce) / float(mass)
    
    return (xAccel, yAccel, zAccel)


# #### Q. What will this do?

# In[ ]:

acceleration(10, 20, 30, 5)

I put eKinetic and acceleration in a module called kinematics.py using a text editor.

Now, try the module in an IPython session:
# In[ ]:

# remember that this line overwrites the local definition
# because it has the same name as above!

from kinematics import eKinetic, acceleration

mass = 100
velocity = 10
xForce = 10
yForce = 20
zForce = 30

kEnergy = eKinetic(mass, velocity)
mAccel = acceleration(xForce, yForce, zForce, mass)

kEnergy, mAccel


# ### Providing program arguments on the command-line

# Input is often supplied to Python scripts via the command line.
# 
# Put another way, "arguments" are provided to scripts.
# 
# Here are some Linux examples:
# 
# ```bash
# echo $PATH
# ```    
# 
# echo is the command, `$PATH` is an argument. Or, 
# 
# ```bash
# cd some_directory
# ```
# 
# cd is the commmand, `some_directory` is an argument.
# 
# ```bash
#     cd
# ```
# 
# No arguments here -- default behavior: cd $HOME

# We can do the same sort of thing in Python using the sys module. 
# The following script (lecture_08_wavetofreq.py) converts a 
# user-supplied wavelength (in Angstroms) to frequency (in Hz).
# 
# I show you here how to quickly load an existing script into the notebook, using %load:

# In[ ]:

# %load lecture_08_wavetofreq.py
#!/usr/bin/env python

import sys
wave = float(sys.argv[1])
freq = 3.0e8 / (wave / 1e10)
print('frequency (Hz) = %e' % freq)


# In[ ]:

import sys                   # "sys" is short for "system"
wave = float(sys.argv[1])
freq = 3.0e8 / (wave / 1e10) # pass wavelength in Angstroms
print('frequency (Hz) = %e' % freq)


# In[ ]:

sys.argv


# sys.argv contains a list of the command line arguments to the program. 
# 
# sys.argv[0] is always the name of the program.

# To run it in a Linux terminal (must be in same directory as file):
# 
# ```bash
# python lecture_08_wavetofreq.py 5000
# ```
# 
# To run it within here or a simple ipython terminal (file must be in same directory that you 
# launched the notebook from):

# In[ ]:

get_ipython().magic('run lecture_08_wavetofreq.py 5000')


# #### Q. What if there is more than one command-line input required?













Consider the following script:
# In[ ]:

import sys

for i, element in enumerate(sys.argv):
    print("Argument #{} = {}".format(i, element))

I have it saved in a file called lecture_08_systest.py
# #### Q. What will the following command do in a Linux session?
python lecture_08_systest.py 'hello' 2 4 6
# You will practice with sys in the tutorial!

# In[ ]:

get_ipython().magic("run lecture_08_systest.py 'hello' 2 4 6")


# ### Error Handling

# The script lecture_08_wavetofreq.py expects an argument, the 
# wavelength in Angstroms:
# 

# In[ ]:

# lecture_08_wavetofreq.py

import sys
wave = float(sys.argv[1])          # Attempting to use the argument here.
freq = 3.0e8 / (wave / 1e10)       # Convert wavelength in Angstroms to frequency in Hz
print('frequency (Hz) = %e' % freq)


# If we forget to supply that argument, we get an error message:

# In[ ]:

get_ipython().magic('run lecture_08_wavetofreq.py')


# It tells us what file and what line where the error occured and 
# the type of error (IndexError)

# #### Q. What is a simple way we could tell if the user forgot the  argument and exit the program gracefully without a crash?
Hint:  Where are the arguments held again?













We could test the length of sys.argv and if it is < 2; if so, we could 
abort with an error message (this script is saved in 
lecture_08_wavetofreq2.py):
# In[ ]:

# lecture_08_wavetofreq2.py

import sys

if len(sys.argv) < 2:
    print('Enter the wavelength in Angstroms on the command line.')
    sys.exit(1) # Exits and 1 indicates failure
                # sys.exit() or sys.exit(0) is used to indicate success

wave = float(sys.argv[1])
freq = 3.0e8 / (wave / 1e10)
print('frequency (Hz) = %e' % freq )


# #### Q. What will the following yield?

# In[ ]:

get_ipython().magic('run lecture_08_wavetofreq2.py 5000')


# #### Q. And this?

# In[ ]:

get_ipython().magic('run lecture_08_wavetofreq2.py')


# In[ ]:

get_ipython().magic('tb')


# ### Exception Handling

# Alternatively, the program can try to run the code and 
# if errors are found, jump to statements that handle 
# the error as desired.
# 
# This is done with two new reserved words, "try" and "except", 
# which are used in a similar way as "if" and "elif". 

# This is the script lecture_08_wavetofreq3.py:

# In[ ]:

# lecture_08_wavetofreq3.py

import sys

try:
    wave = float(sys.argv[1])
except:
    print('Enter the wavelength in Angstroms on the command line.')
    sys.exit(1)

freq = 3.0e8 / (wave / 1e10)
print('frequency (Hz) = %e' % freq)


# If the command in the try block produces an error, the except block 
# is executed.

# #### Q. What does "wave = float(sys.argv[1])" attempt to do?

# #### Q. What if we try to do the following:

# In[ ]:

get_ipython().magic('run lecture_08_wavetofreq3.py x')


# In[ ]:

get_ipython().magic('tb')


# > The program could also fail if something other than a number is given 
# on the command line!

# That produces a ValueError, not an IndexError.
# 
# We can fix this with two separate exceptions appropriate for the two 
# possible errors (this is similar to if/elif/elif):

# In[ ]:

# lecture_08_wavetofreq4.py

import sys

try:
    wave = float(sys.argv[1])
    
except IndexError:
    print('Enter the wavelength in Angstroms on the command line.')
    sys.exit(1)

except ValueError as error:
    #print 'The wavelength must be a number'\
    #' not %s.' % type(sys.argv[1])
    print("The error is:", error)
    sys.exit(2)

freq = 3.0e8 / (wave / 1e10)
print('frequency (Hz) = %e' % freq)

This script is saved in the file lecture_08_wavetofreq4.py
# #### Q. What do these yield?

# In[ ]:

get_ipython().magic('run lecture_08_wavetofreq4.py 5000')


# In[ ]:

get_ipython().magic('run lecture_08_wavetofreq4.py')


# In[ ]:

get_ipython().magic('run lecture_08_wavetofreq4.py x')


# ### Common error types
IndexError for indices out of range:
# In[ ]:

data = range(9)
data[9]

Q. Why does it fail?


Converting a str to a float gives a ValueError:
# In[ ]:

y = float('x')


# In[ ]:

y = float('3')
y

Using an uninitialized variable gives a NameError:
# In[ ]:

x

Division by zero raises a ZeroDivisionError exception:
# In[ ]:

4.0/0

Syntax errors lead to SyntaxErrors!
# In[ ]:

iff 2 > 1:
    print('it is.')

Multiplying a string by a float yields a TypeError:
# In[ ]:

10.0 * 'blah'


# #### Q. But what will this do?

# In[ ]:

5 * 'blah '


# Nice flowchart on error handling (http://i.imgur.com/WRuJV6r.png):
# 
# ![errors](http://i.imgur.com/WRuJV6r.png "Error handling")
