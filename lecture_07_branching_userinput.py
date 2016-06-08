
# coding: utf-8

# # Today:  Branching and User Input

# ### Branching (If/Else blocks) -- Section 3.2

# "The flow of computer programs often needs to branch. 
# That is, if a condition is met, we do one thing, and if not, we do another thing." -p.104 of your book
# 
# This is referred to as branching into a block of statements.

# ====  Basic if  ====
# ```python
# if <condition>:
#     <do something>
# ```
# ====  Add an else  ====
# ```python
# if <condition>:
#     <do something>
# else:
#     <do something else>
# ```    
# ==== Add an elif  ====
# ```python
# if <condition>:
#     <do something>
# elif <a different condition>:
#     <do something else>
# else:
#     <do something else>
# ```

# In[3]:

x = 6.28  # set the variable x equal to tau, the real circular constant

# Note this is the only correct way to check equality on floats.
# Subtract the expected value and compare to your allowed error:

eps = 1e-10  # my deviation I allow until I call them 'equal'
if((x - 6.28) < eps):      # if x is equal to tau
    print("2*PI. Mmmm, lots of PI.")  # print something
else:                      # else
    print("No PI. Alas.")  # print something else


# In[4]:

from math import exp

def func1(value):
    if(0 <= value <= 1):     # note the math-like syntax here!
        result = exp(value)  # executed if value is between 0 and 1
    else:
        result = -10         # executed otherwise (if is false)
    
    return result            # Return the result


# #### Q. What should this yield?

# In[5]:

result = func1(1)  
result


# #### Q. And this?

# In[6]:

func1(1.5)  

We can have multiple branching with "else if" statements,
which are shortened to "elif":
# In[7]:

def func2(value):
    if 0 <= value < 1:
        result = exp(value)  # executed if value is between 0 (inclusive) and 1 (exclusive) 
    elif 1 <= value <= 2:
        result = -100        # executed if value is between 1 and 2 (inclusive)
    else:
        result = 0
        print('value is not between 0 and 2')
    
    return value, result


# #### Q. So, what will this print out?

# In[8]:

print("{}\t{}".format(*func2(0.5)))
print("{}\t{}".format(*func2(1)))
print("{}\t{}".format(*func2(1.5)))
print("{}\t{}".format(*func2(20)))


# I'm smelling a violation of the DRY principle!
# How can we improve? Another function:

# In[9]:

def calc_and_print(value):
    print("{}\t{}".format(*func2(value)))


# In[10]:

for val in [0.5, 1, 1.5, 20]:
    calc_and_print(val)


# Ahh, better. ;)
# 
# #### The ternary operator for if-else branching
# 
# Ternary operators are statements with 3 arguments, but usually this is the only one per language, so it's often called **THE** ternary operator:

# In[14]:

x = 3
'x equals 2' if x == 2 else 'x does not equal 2'

How handy!  Consider this:
# In[15]:

import math

def squareRoot(value):
    return math.sqrt(value) if value >= 0 else        'Imaginary numbers not supported!'


# #### Q. What will this do?

# In[16]:

print(squareRoot(2.0))
print(squareRoot(-2.0))  # my function protects against error
print(math.sqrt(-2))     # the original not


# ### Using break to end a `while` loop
# 
# a while loop with a limit on the maximum number of allowed iterations.  

# In[17]:

count = 0
while count < 100:
    count += 1
    
count


# In[19]:

count = 0
while True:  # obviously always True. So the while block needs to interrupt
    if count == 100:
        break           # Immediately jump out of the while loop
    else:
        pass           # this doesn't do anyting, maybe reminder to have an else case?
    count += 1
    
count


# Notice the new reserved words: "break" and "pass"
# 
# In this example, the else statement is optional, i.e. we could just do:

# In[20]:

i = 0
while True:
    if i == 100:
        break
    i += 1

i


# #### Gold case for `while` loop
# The previous code cell is not terribly useful, but consider an approximation of the sine curve.
# To make this more interesting, let's calculate sine to a particular accuracy (AKA tolerance).

# $$\sin(x) \approx \sum_{n=0}^N \frac{(-1)^n}{(2n + 1)!} x^{2n + 1}$$

# In[23]:

from math import pi, factorial, sin
tau = 2*pi   # read http://tauday.com ! ;)

x = tau / 3          # Evaluate at x = pi / 5 (just a number I chose) 
mathSin = sin(x)     # Use math.sin to calculate sin(x)
prevTotal = 1e5      # The previous value of the sine series.
                     # Just something big to start with; will be overwritten first 
                     # time through loop.
tolerance = 0.01
total     = 0.0      # The summation's running total
n         = 0        # The current summation term number

print("%5s  %12s  %12s" % ("count", "approx", "math.sin(x)"))

while True:
    term = (-1)**n * x**(2*n + 1) / factorial(2*n + 1)  # Calculate the current term
    
    total += term    # Add the term to the running total
    
    #  Print the current term number, running total, and math.sin value
    print('%5i  %12.8g  %12.8g' % (n, total, mathSin))
    
    # If the diff between prevTotal and total is less than the tolerance, stop the loop
    if abs(prevTotal - total) < tolerance:
        break
    
    prevTotal = total    # Update the previous total value
    
    n += 1               # Increment the summation count


# By adding the "if" statement, we can compare the previous total with the current total.  When the difference between the previous and current totals is less than the tolerance, the code "breaks" and the while loop is stopped.

# ### if statements in list comprehensions
# 
# We can add an if condition to a list comprehension.  We would do this when we wanted to limit or filter the values that are put into the resulting list.

# In[24]:

divisor = 3.25   # Number to divide by

# Create a list of numbers between 1 and 100 that are divisible by "divisor"
numList = [num for num in range(1, 101) if num % divisor == 0]
numList


# In[28]:

nameList = ['Samual', 'Charlie', 'Zarah', 'Robert', 'Liangyu', 'Jeffery', 'Brian', 'Aidan', 'Melissa', 'Gerardo',             'Emily', 'Parker', 'Amanda', 'Kristine', 'Tarek', 'Christian', 'Ian', 'Alex', 'Nathaniel',             'Samantha', 'Pengqi']

searchstr = 'ar'

# when reading list comprehensions, always make a mental break
# in front of the `for` keyword
filterList = [name for name in nameList if searchstr in name]

print("Zarah".find(text))

filterList


# ### User Input
# 
# Until now, we have provided the information necessary for a program to run 
# by typing it into our notebook cells.
# 
# This can be inconvenient, especially if we want to:
# 
# 1. Write an interactive program, or 
# 2. If the amount of information the program requires is huge.
# (e.g., 10-body system vs. 3-body system)
# 
# Today, we'll cover the first case: writing an interactive program.
# 
# Later, we'll discuss #2, where we must supply a lot of information 
# to a program, and it's best to read that information from a file rather than 
# supplying it "by hand."
# 
# ### input
# 
# The "input" function allows you (a user) to supply new information to 
# Python code as it runs. 
# 
# This can be useful for:
# * Supplying parameters (e.g., a blackbody temperature).
# * Changing how the code branches (e.g., what if user supplies
# bogus input? More discussion about this coming up.).

# In[29]:

x = input('Enter a float: ')

(Might not work in older ipython notebooks)
# In[30]:

x


# In[32]:

print(type(x))
x = float(x)


# #### Why bother?
# 
# Anytime we supply input, whether it be in an iPython session (via `input`), the Linux terminal, or from a file (later this semester), that input will be interpreted *as a string.*
# 
# Let's try inputting some values for the escape velocity equation.

# $$v=\sqrt{\frac{2GM}{r}}$$
# Equation for escape velocity in $\frac{meters}{second}$ where $G$ is the gravitational constant, $M$ is the mass of the planet, and $r$ is the radius of the planet.

# In[35]:

from math import sqrt

def escapeVel(mass, radius):                 # Define the function with 2 input variables
    G = 6.67e-11                             # Gravitational constant
    velocity = sqrt(2*G*mass / radius)       # Escape velocity equation
    
    return velocity                          # Return the escape velocity


# #### What will this do?

# In[47]:

maxCount = 100
count = 0

while True and count < maxCount:
    mass   = input("Please enter the planet's mass in kg:  ")
    radius = input("Please enter the planet's radius in m: ")
    
    if mass != "" and radius != "":
        print("The escape velocity is: %.1f m/s" % escapeVel(float(mass), float(radius)))
    else:
        print("Ending program!")
        break
    
    print()
    count += 1


# ### Now something complete different: Version control with git
# 
# Ever had something like `xxx_v0.txt`, `xxx_v1.txt`, `xxx_v2.txt` etc.? 
# 
# Did you always remember what's the best version? 
# 
# How did you compare the files? Manually, possibly?
# 
# Version control enables you:
# * Keep track on your changes over time
# * Compare your most recent changes with the currently `committed` (=stored) version
#  * With some more effort (=command-line-fu) compare with any version at any time
# * Work on a different idea while not disturbing your main codes (=`branching out`)
# * Collaborate more easily with others
# * show you logs of your changes, for everything, or per file
# * enable you to `blame` who did certain changes while collaborating
#      * that git function is indeed called `git blame`
# * bake a bread, make a coffee...
# 
# #### git <-> GitHub
# * `git` is the version control software we will be using.
# * `GitHub` is a web service for collaborating on software (and documentation), and it runs on `git`, but it **IS NOT** git.
# * `GitHub` offers a lot on top of your programs:
#  * Issue tracker
#  * Wiki
#  * Graphical browsing of differences
#  * Pull requests (more on that later)
#  * Offers a graphical desktop client program to interact with `git` and `GitHub`.
# * `git` has a steep learning curve, but it's absolutely worth it.
#  * Best strategy is to only use small set of commands at beginning, and then learn more when you want to solve a new issue.
# 
# We will run through a setup here and you will practice it in the tutorial, but please go through the 15 minutes of time of a beautifully made intro on https://try.github.io by the GitHub team.
# 
# #### First time
# * git init
# * < create a textfile.txt>
# * git add textfile.txt
#     * < now in staging phase, can add more files if required>
# * git commit
#  * will pop up editor, type in commit message:
# * "First commit"
#     * then <Ctrl-X>, <Y>, <Return> to leave editor with saving that message
# * git log
#   * Will show you name, time and commit message
#   * Also shows a very long hex-code. That's the unmistake-able identifier for this commit.
#   
# #### Usually
# * You have changed a file, let's look what's different
# * git diff
#   * shows all changes made to folder
# * If you are happy to commit this, you can omit staging phase and store everything:
# * git commit --all -m 'change this to that'
# * Done. Even didn't use nasty editor.
# 

# In[ ]:



