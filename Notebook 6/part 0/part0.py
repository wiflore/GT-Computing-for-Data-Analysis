
# coding: utf-8

# # Part 0: Mining the web
# 
# Perhaps the richest source of openly available data today is [the Web](http://www.computerhistory.org/revolution/networking/19/314)! In this lab, you'll explore some of the basic programming tools you need to scrape web data.
# 
# > **Warnings.**
# > 1. If you are using one of the cloud-based Jupyter installations to run this notebook, such as [Microsoft Azure Notebooks](https://notebooks.azure.com) or [Vocareum](https://vocareum.org), it's likely you will encounter problems due to restrictions on access to remote servers.
# > 2. Even if you are using a home or local installation of Jupyter, you may encounter problems if you attempt to access a site too many times or too rapidly. That can happen if your internet service provider (ISP) or the target website detect your accesses as "unusual" and reject them. It's easy to imagine accidentally writing an infinite loop that tries to access a page and being seen from the other side as a malicious program. :)

# ## The Requests module
# 
# Python's [Requests module](http://requests.readthedocs.io/en/latest/user/quickstart/) to download a web page.
# 
# For instance, here is a code fragment to download the [Georgia Tech](http://www.gatech.edu) home page and print the first 250 characters. You might also want to [view the source](http://www.computerhope.com/issues/ch000746.htm) of Georgia Tech's home page to get a nicely formatted view, and compare its output to what you see above.

# In[ ]:


import requests

response = requests.get('http://www.gatech.edu/')
webpage = response.text  # or response.content for raw bytes

print(webpage[0:250]) # Prints the first hundred characters only


# **Exercise 1.** Given the contents of the GT home page as above, write a function that returns a list of links (URLs) of the "top stories" on the page.
# 
# For instance, on Friday, September 9, 2016, here was the front page:
# 
# ![www.gatech.edu as of Fri Sep 9, 2016](./www.gatech.edu--2016-09-09--annotated-medium.png)
# 
# The top stories cycle through in the large image placeholder shown above. We want your function to return the list of URLs behind each of the "Full Story" links, highlighted in red. If no URLs can be found, the function should return an empty list.

# In[ ]:


import re # Maybe you want to use a regular expression?

def get_gt_top_stories(webpage_text):
    """Given the HTML text for the GT front page, returns a list
    of the URLs of the top stories or an empty list if none are
    found.
    """
#
# YOUR CODE HERE
#


# In[ ]:


top_stories = get_gt_top_stories(webpage)
print("Links to GT's top stories:", top_stories)


# ## A more complex example
# 
# Go to [Yelp!](http://www.yelp.com) and look up `ramen` in `Atlanta, GA`. Take note of the URL:
# 
# ![Yelp! search for ramen in ATL](./yelp-search-example.png)

# This URL encodes what is known as an _HTTP "get"_ method (or request). It basically means a URL with two parts: a _command_ followed by one or more _arguments_. In this case, the command is everything up to and including the word `search`; the arguments are the rest, where individual arguments are separated by the `&` or `#`.
# 
# > "HTTP" stands for "HyperText Transport Protocol," which is a standardized set of communication protocols that allow _web clients_, like your web browser or your Python program, to communicate with _web servers_.
# 
# In this next example, let's see how to build a "get request" with the `requests` module. It's pretty easy!

# In[ ]:


url_command = 'http://yelp.com/search'
url_args = {'find_desc': "ramen",
            'find_loc': "atlanta, ga"}
response = requests.get (url_command, params=url_args)

print ("==> Downloading from: '%s'" % response.url) # confirm URL
print ("\n==> Excerpt from this URL:\n\n%s\n" % response.text[0:100])


# **Exercise 2.** Given a search topic, location, and a rank $k$, return the name of the $k$-th item of a Yelp! search. If there is no $k$-th item, return `None`.
# 
# > The demo query above only gives you a website with the top 10 items, meaning you could only use it for $k \leq 10$. Figure out how to modify it to solve the problem when $k > 10$.

# In[ ]:


def find_yelp_item (topic, location, k):
    """Returns the k-th suggested item from Yelp! in Atlanta for the given topic."""
#
# YOUR CODE HERE
#


# In[ ]:


assert find_yelp_item('fried chicken', 'Atlanta, GA', -1) is None # Tests an invalid value for 'k'


# > Search queries on Yelp! don't always return the same answers, since the site is always changing! Also, your results might not match a query you do via your web browser (_why not?_). As such, you should manually check your answers.

# In[ ]:


item = find_yelp_item ('fried chicken', 'Atlanta, GA', 1)
print (item)

# The most likely answer on September 19, 2017:
#assert item in ['Gus’s World Famous <span class="highlighted">Fried</span> <span class="highlighted">Chicken</span>',
#                'Gus’s World Famous Fried Chicken']                


# In[ ]:


item = find_yelp_item ('fried chicken', 'Atlanta, GA', 5)
print (item)

# The most likely answer on September 19, 2017:
#assert item == 'Richards’ Southern Fried'


# In[ ]:


item = find_yelp_item('fried chicken', 'Atlanta, GA', 17)
print(item)

# Most likely correct answer as of September 19, 2017:
#assert item == 'Sway'


# One issue with the above exercises is that they treat HTML as a flat string, whereas the document is at least semi-structured. Moreover, web pages are such a common source of data today that you would expect better tools for processing them. Indeed, such tools exist! The next part of this assignment, Part 1, walks you through one such tool. So, head there when you are ready!
