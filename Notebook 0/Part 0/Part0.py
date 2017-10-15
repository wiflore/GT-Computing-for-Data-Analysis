
# coding: utf-8

# # Sample notebook: Part 0
# 
# This notebook is Part 0 of two parts (Parts 0 and 1): in the computer science tradition, we will try to number beginning at 0. Together, the two parts comprise an ungraded *lab notebook assignment* (or just *lab* or *assignment*). Although it's ungraded, use it as practice for completing and submitting an assignment.

# ## Python code cells
# 
# Run the following code cell to determine the version of Python running in this environment. Make a mental note of the Python version

# In[ ]:


import sys
print(sys.version)
py_ver = sys.version.split('|')[0]
print("\n** You appear to be running Python version {}**".format(py_ver))


# In this course, notebook assignments will consist mainly of exercises like the following. You'll see a question, its point value, and a "code cell," which is placeholder cell for coding up your solution. Following that code cell will typically be another code cell to help you *test and debug* your code. Indeed, the autograder works by verifying that these test cells pass.
# 
# > The autograder may also test other cases that you do *not* get to see, so when writing up your solution be sure to follow the specifications of the problem carefully.

# **Exercise 0** (`x_test`: 1 point). Create a variable named `x` and assign it the integer value of 1.

# In[1]:


x = 1


# In[2]:


# x_test: This cell tests your code from above.

print("Your x:", x)
assert x == 1

print("\nPassed!")


# ## Markdown cells
# 
# Besides cells for code, you can edit or create cells intended to contain *formatted* text. The "language" used for such cells is called *Markdown*, which you can read a little more about [here](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Working%20With%20Markdown%20Cells.html). It's like a simplified HTML designed to be readable both as plain text but also rendered as formatted text.
# 
# Unfortunately, there are many flavors of Markdown and it is not always clearly documented what features are available in any particular environment. You may need to do some experimenting to figure out how to get text look the way you want, so just do your best when required.

# **Exercise 1** (ungraded). The cell below has been set up to accept Markdown text. Edit it to display the image at this URL: http://cse6040.gatech.edu/datasets/mystery-image.jpg
# 
# > For the Markdown syntax to embed an image, refer to this page: https://daringfireball.net/projects/markdown/basics

# 

# This is the end of Part 0. If everything seems to have worked, try submitting it!
# 
# > **Tip 1.** Before submitting, make sure you save your notebook first. (`File` $\rightarrow$ `Save and checkpoint`)
# 
# > **Tip 2.** Also, remember to run everything from the top! That is, just before submitting, we recommend that you first restart the kernel and clear outputs (`Kernel` $\rightarrow$ `Restart & Clear Output`) and then run all cells (`Cell` $\rightarrow$ `Run All`).

# ![](http://cse6040.gatech.edu/datasets/mystery-image.jpg)
# 
# *Markdown* $e^{2}$
# 
