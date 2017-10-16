
# coding: utf-8

# ## Part 1: Tools to process HTML
# 
# In Part 0, you downloaded real web pages and manipulated them using "conventional" string processing tools, like [`str`]() functions or [regular expressions]().
# 
# However, web pages are stored in HTML ([hypertext markup language]()), which is a highly structured format. As such, it makes sense to use specialized tools to understand and process its structure. That's the subject of this notebook.

# ## Parsing HTML: The Beautiful Soup module
# 
# One such package to help process HTML is [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/). The following is a quick tutorial on how to use it.
# 
# Any HTML document may be modeled as an object in computer science known as a [tree](https://en.wikipedia.org/wiki/Tree_(data_structure)):
# 
# ![HTML as a tree](./html-slide.png)
# 
# There are different ways to define trees, but for our purposes, the following will be sufficient.

# Consider a tree is a collection of _nodes_, which are the labeled boxes in the figure, and _edges_, which are the line segments connecting nodes, with the following special structure.
# 
# * The node at the top is called the _root_. Here, the root is labeled `html` and abstractly represents the entire HTML document.
# * Regard each edge as always "pointing" from the node at its top end to the node at its bottom end. For any edge, the node at its top end is the _parent_ and the node at the bottom end is a _child_. Like real families, a parent can be a child. For example, the node labeled `head` is the child of `html` and the parent of `meta`, `title`, and `style`.
# * The _descendant_ of a node $x$ is any node $y$ for which there is a path from $x$ going down to $y$. For example, the node labeled `6x span` is a descendant of the node `body`. All nodes are descendants of the root.
# * Any node with _no_ descendants is a _leaf_.
# * Any node that is neither a root nor a leaf is an _internal node_.
# * There are no _cycles_. A cycle would be a loop. For instance, if you were to add an edge between the two lower rightmost nodes labeled, `strong` and `strong`, that would create a loop and the object would no longer be a tree.
# 
# > For whatever reason, [computer scientists usually view trees upside down](https://www.quora.com/Why-are-trees-in-computer-science-generally-drawn-upside-down-from-how-trees-are-in-real-life), with the "root" at the top and the "leaves" at the bottom.

# The Beautiful Soup package gives you a data structure for traversing this tree. For instance, consider an HTML file with the contents below, shown both as code and pictorially.

# In[ ]:


some_page = """
<html>
  <body>
    <p>First paragraph.</p>
    <p>Second paragraph, which links to the <a href="http://www.gatech.edu">Georgia Tech website</a>.</p>
    <p>Third paragraph.</p>
  </body>
</html>
"""
print(some_page)


# ![Two visual representations of `some_page`](./html-viz.png)

# **Exercise 0.** Besides HTML files, what else have we seen in this class that could be represented by a tree? Briefly and roughly explain what and how.

# **Answer.** One thing that has a natural tree representation is a Python program! For example, can you draw the following program as a tree?
# 
# ```python
# import re
# 
# def scan_lines(text, pattern):
#     matches = []
#     for line in text.split('\n'):
#         if re.search(pattern, text) is not None:
#             matches.append(True)
#         else:
#             matches.append(False)
#     return matches
# ```

# ## Using Beautiful Soup
# 
# Here is how you might use Beautiful Soup to inspect the structure of `some_page`.
# 
# Let's start by taking the contents of the page above (`some_page`) and asking Beautiful Soup to process it. Let's store the result in object named `soup`, and then explore its contents:

# In[ ]:


from bs4 import BeautifulSoup

soup = BeautifulSoup(some_page, "lxml")

print('1. soup ==', soup) # Print the HTML contents
print('\n2. soup.html ==', soup.html) # Root of the tree
print('\n3. soup.html.body ==', soup.html.body) # A child tag
print('\n4. soup.html.body.p ==', soup.html.body.p) # Another child tag
print('\n5. soup.html.body.contents ==', type(soup.html.body.contents), '::', soup.html.body.contents)


# Observe that the `.` notation allows us to reference HTML tags---that is, the stuff enclosed in angle brackets in the original HTML, e.g., `<html> ... </html>`, `<body> ... </body>`---as they are nested. But in the case of the `<body> ... </body>` tag, there are multiple subtags. Evidently, `soup.html.body.contents` contains these, as a list, which we know how to manipulate.

# In[ ]:


# Enumerate all tags within the <body> ... </body> tag:
for i, elem in enumerate (soup.html.body.contents):
    print ("[{:4d}]".format (i), type (elem), '\n\t==>', "'{}'".format (elem))

# Reference one of these, element 3:
elem3 = soup.html.body.contents[3]
ßprint(elem3.contents)


# **Exercise 1.** Write a statement that navigates to the tag representing the GT website link. Store this resulting tag object in a variable called `link`.

# In[ ]:


#
# YOUR CODE HERE
#

print(link)


# In[ ]:


# Checks your link. Can you understand what it is doing?
import bs4
assert type(link) is bs4.element.Tag
assert link.name == 'a'
assert link['href'] == 'http://www.gatech.edu'
assert link.contents == ['Georgia Tech website']


# ### Other navigation tools
# 
# This lab includes a static copy of the Yelp! results for a search of "universities" in ATL. Let's start by downloading this file.

# In[ ]:


# Run me: Code to download sample HTML file

import requests
import os
import hashlib

yelp_htm = 'yelp_atl_unies.html'
yelp_htm_checksum = 'a940e7cd0c8c408a5dd2098a87303afe'

if os.path.exists('.voc'):
    data_url = 'https://cse6040.gatech.edu/datasets/yelp-example-uni/{}'.format(yelp_htm)
else:
    data_url = 'https://github.com/cse6040/labs-fa17/raw/master/datasets/{}'.format(yelp_htm)

if not os.path.exists(yelp_htm):
    print("Downloading: {} ...".format(data_url))
    r = requests.get(data_url)
    with open(yelp_htm, 'w', encoding=r.encoding) as f:
        f.write(r.text)

with open(yelp_htm, 'r') as f:
    yelp_html = f.read().encode(encoding='utf-8')
    checksum = hashlib.md5(yelp_html).hexdigest()
    assert checksum == yelp_htm_checksum, "Downloaded file has incorrect checksum!"
    
print("'{}' is ready!".format(yelp_htm))


# Next, inspect and run this code, which prints the top (number one) result.

# In[ ]:


uni_html_text = open (yelp_htm, 'r').read()
uni_soup = BeautifulSoup(uni_html_text, "lxml")

print("The number 1 ATL university according to Yelp!:")

uni_1 = uni_soup.html.body     .contents[7]     .contents[9]     .contents[3]     .contents[1]     .contents[3]     .contents[1]     .contents[1]     .contents[7]     .contents[3]     .contents[5]     .contents[1]     .contents[1]     .contents[1]     .contents[1]     .contents[3]     .contents[1]     .contents[1]     .contents[1]     .contents[0]     .contents[0]
    
print(uni_1)


# We hope it is self-evident that the above method to navigate to a particular tag or element is not terribly productive or robust, particularly if there are small modifications to the HTML.
# 
# Here is an alternative. Inspect the raw HTML and observe that every non-ad search result appears in a tag of the form,
# 
# ```html
# <span class="indexed-biz-name">1.         <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="/biz/georgia-institute-of-technology-atlanta-2" data-hovercard-id="gBX8UvhOwtdD5tGJeU-hxg" ><span >Georgia Institute of Technology</span></a>
# </span>
# ```
# 
# Beautiful Soup gives us a way to search for specific tags.

# In[ ]:


indexed_unies = uni_soup.find_all(attrs={'class': 'indexed-biz-name'})
print("*** First 5 of {} results ***\n\n{}".format(len(indexed_unies), indexed_unies[:5]))


# **Exercise 2.** Based on the above, write a function that, given a Yelp! search results page such as `uni_soup` above, returns the name of the number 1 indexed search result.

# In[ ]:


def get_top_yelp_result(soup):
    """Given a Yelp! search result as a Beautiful Soup page,
    returns the name of the number 1 indexed result.
    """
#
# YOUR CODE HERE
#


# In[ ]:


print(get_top_yelp_result(uni_soup))
assert get_top_yelp_result(uni_soup) == 'Georgia Institute of Technology'


# This mini-tutorial only scratches the surface of what is possible with Beautiful Soup. As always, refer to the [package's documentation](https://www.crummy.com/software/BeautifulSoup/) for all the awesome deets!
