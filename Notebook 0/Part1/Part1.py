
# coding: utf-8

# # Sample notebook: Part 1
# 
# This notebook is Part 1 of two parts (Parts 0 and 1): in the computer science tradition, we will try to number beginning at 0. Together, the two parts comprise an ungraded *lab notebook assignment* (or just *lab* or *assignment*). Although it's ungraded, use it as practice for completing and submitting an assignment.

# ## Getting input data
# 
# Throughout the course, we'll use a variety of methods to get data for use in the notebook environment.
# 
# One technique is to use [magic commands or shell commands](https://ipython.readthedocs.io/en/stable/interactive/tutorial.html#magics-explained). These are code-like constructs that are specific to Jupyter but outside the base language (e.g., Python). They typically appear on lines of code prefixed by `!` or `%`.
# 
# Here is an example that downloads a file containing a secret message.
# 
# > This example is a *shell command*. It invokes a command-line utility called `curl` to do the download, which you can read more about [here](https://curl.haxx.se/docs/manpage.html).

# In[1]:


# Download:
get_ipython().system('curl -O https://cse6040.gatech.edu/datasets/message_in_a_bottle.txt.zip')

# Confirm (from shell):
get_ipython().system('echo && echo "=== Files in the current directory (from a shell command) ===" && echo && ls -al')

# Confirm (from Python):
import os
print("\n=== Files in the current directory (from Python) ===\n{}".format(os.listdir('.')))


# **Exercise 0** (1 point). In the code cell below, create a variable named `filename` and initialize it to a string containing the name `message_in_a_bottle.txt.zip`. The test cell that follows it will unpack this file, assuming it is available in the current working directory, unpack it, and then print its contents.

# In[2]:


uncompressed_name = 'message_in_a_bottle.txt'
compressed_extension = '.zip'
filename = uncompressed_name + compressed_extension


# In[3]:


# Test cell: `filename_test`

print("`filename`: '{}'".format(filename))
from zipfile import ZipFile
with ZipFile(filename, 'r') as input_zip:
    with input_zip.open(filename[:-4], 'r') as input_file:
        message = input_file.readline().decode('utf-8')
print("\n=== BEGIN MESSAGE ===\n{}=== END MESSAGE ===".format(message))


# This is the end of Part 1. If everything seems to have worked, try submitting it!

# In[ ]:




