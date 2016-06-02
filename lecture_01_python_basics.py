
# coding: utf-8

# ### Lecture #1: iPython notebooks

# In[1]:

#  This is also how to print text to the screen
print "Hello world!"


# In[2]:

#  This is how to print text to the screen using Python v3.x
print("Hello world!")


# ### Simple formulas

# In[4]:

4+2        #  Addition


# In[5]:

4-2        #  Subtraction


# In[7]:

4/3        #  Division


# In[8]:

4//3       # Integer Division in old style, cutting of decimals


# In[9]:

4*2        #  Multiplication


# In[10]:

4**2       #  Exponents (this reads 4 squared)


# In[11]:

4%2        #  Modulo (the answer is the remainder)


# In[12]:

5%2        #  Modulo (the answer is the remainder)


# ### Variable assignments and printing

# In[13]:

x = 3      #  x is now a variable


# In[14]:

print(x)   #  Print the variable x to the screen


# In[16]:

x          #  In Jupyter notebook this prints to the screen


# In[17]:

x**2
x = x**2
#  What does this print?


# In[19]:

print(x)
#  What is the value of x?


# ### Strings

# In[20]:

name = 'ASTR'            #  You can use single or double quotes


# In[22]:

name + '2600\'s'            #  Adding strings
name + "2600's"


# In[24]:

name = name + '2600   '

#  What is the value of name?
print(name)
print(name * 2)


# In[25]:

print(name ** 2)           #  Multiplying strings

#  What is printed?


# ### "Markdown," i.e., fancy typesetting (just for fun!)

# $\sqrt{2}$

# $\Gamma = 1.4$

# $\frac{1}{2} = 0.5$

# ### Raw Text 
The formatting we used in markdown is known as LaTeX formatting. For more information, a good place to start is:

http://en.wikibooks.org/wiki/LaTeX/Mathematics

or, just Google it!
# $\int e^x dx = e^x$

# ### Notebook Recap

# * Use <shift-enter> to execute cells, or select "Run" from the "Cell" drop-down menu.
# 
# * Use raw text to write short answers to questions that appear in homework.
# 
# * You don't need to know how to do markdown, but you're welcome to if you want.

# ### Path recap
# 
# > Remember: Everything on Linux is a file. A directory is just a special file that can contain other files.
# 
# There are 2 different kind of paths: absolute and relative paths.
# 
# Imagine your friend asks you how to get somewhere. You will instinctively ask where your friend is, so that you can give her instructions **relative to her current location**! That would be a relative path to where she wants to be.
# 
# Absolute paths are always correct and complete (hence absolute), and always start with a `/`, the "root" symbol. As `/` is the lowest point on a storage device, the path that is attached to it is always unique.
# 
# Relative paths are very flexible, they just take one instruction after the other, separated by the `/`. So, for example to go from `/home/student` to `/usr/bin`, the relative path would be `../../usr/bin`.
# 
# Note how it does **NOT** start with a `/` because from `/home/student` to go up one level is just `..`, not `/..`. (Even more so, `/..` does never make sense, can you see why?).
# 
# The `cd` command just knows it has stack path instructions one by one, separated by the `/` so to execute the above relative path in one go is totally okay (and don't forget to use <tab>, it will help you to maneuver paths immensely!). So here the command would be `cd ../../usr/bin`, if launched from `/home/student`.

# ### So, what's in a path?
# 
# Because everything in Linux is a file, everything in Linux has a path. This also means that there is not a very certain way to know what kind of object is at the end of a path. There is no strict rule for extensions like `.txt` or `.doc`. These are just conventions, but a Linux/Unix system does not need them to work.
# 
# So, at the end of a path can be a directory/folder, or it can be a `real` file. But that doesn't mean you know what that file is or can do. 
# 
# For example, for the path `/home/student/test2`, it could be any of these things:
# 
# * a folder
# * an executable progam
# * a text file with data or configuration values read by a program
# * a script to be executed by an interpreter like Bash or Python
# 
# You have several options to find out what something is:
# 
# * just look at it with the `less` command. If it's a huge bunch of binary, `less` will ask you if you really want to look at binary gibberish.
# * use the `file` command. It was written to exactly reduce the confusion what kind of thing could be at the end of a path. Use it like so: 
# 
#     `file /home/student/test2`

# In[ ]:



