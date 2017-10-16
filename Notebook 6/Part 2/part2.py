
# coding: utf-8

# # Part 2: Mining the web: Web APIs
# 
# We hope the preceding exercise was painful: even with tools to process HTML, it is rough downloading raw HTML and trying to extract information from it!
# 
# > Can you think of any other reasons why scraping websites for data in this way is not a good idea?
# 
# Luckily, many websites provide an application programming interface (API) for querying their data or otherwise accessing their services from your programs. For instance, Twitter provides a web API for gathering tweets, Flickr provides one for gathering image data, and Github for accessing information about repository histories.
# 
# These kinds of web APIs are much easier to use than, for instance, the preceding technique which scrapes raw web pages and then has to parse the resulting HTML. Moreover, there are more scalable in the sense that the web servers can transmit structured data in a less verbose form than raw HTML.
# 
# As a starting example, here is some code to look at the activity on Github related to the public version of our course's materials.

# In[ ]:


import requests

response = requests.get ('https://api.github.com/repos/cse6040/labs-fa17/events')

print ("==> .headers:", response.headers, "\n")


# Note the `Content-Type` of the response:

# In[ ]:


print (response.headers['Content-Type'])


# The response is in JSON format, which is an open format for exchanging semi-structured data. (JSON stands for **J**ava**S**cript **O**bject **N**otation.) JSON is designed to be human-readable and machine-readable, and maps especially well in Python to nested dictionaries. Let's take a look.
# 
# > See also [this tutorial](http://www.w3schools.com/json/) for a JSON primer. JSON is among _the_ universal formats for sharing data on the web; see, for instance, https://www.sitepoint.com/10-example-json-files/.

# In[ ]:


import json
print(type(response.json ()))
print(json.dumps(response.json()[:3], sort_keys=True, indent=2))


# **Exercise 0.** It should be self-evident that the JSON response above consists of a sequence of records, which we will refer to as _events_. Each event is associated with an _actor_. Write some code to extract a dictionary of all actors, where the key is the actor's login and the value is the actor's URL.

# In[ ]:


def extract_actors (json_github_events):
    """Given JSON records for events in a GitHub repo,
    returns a dictionary of the actors and their URLs.
    """
#
# YOUR CODE HERE
#


# In[ ]:


actor_urls = extract_actors(response.json ())

for actor, url in actor_urls.items ():
    print ('{}: {}'.format(actor, url))
    assert url == "https://api.github.com/users/{}".format(actor)


# **Exercise 1.** Write some code that goes to each actor's URL and determines their name. If an actor URL is invalid, that actor should not appear in the output.

# In[ ]:


def lookup_names (actor_urls):
    """Given a dictionary of (actor, url) pairs, looks up the JSON at
    the URL and extracts the user's name (if any). Returns a new
    dictionary of (actor, name) pairs.
    """
#
# YOUR CODE HERE
#


# In[ ]:


actor_names = lookup_names (actor_urls)

for actor, name in actor_names.items ():
    print ("{}: {}".format (actor, name))
    
assert actor_names['rvuduc'] == 'Rich Vuduc (personal account)'


# That's the end of this notebook. Processing JSON is fairly straightforward, because it maps very naturally to nested dictionaries in Python. You might search the web for other sources of JSON data, including [this one](https://www.yelp.com/dataset/challenge), and do your own processing!
