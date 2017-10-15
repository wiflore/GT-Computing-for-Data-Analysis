
# coding: utf-8

# # Part 1 of 2: Processing an HTML file
# 
# One of the richest sources of information is [the Web](http://www.computerhistory.org/revolution/networking/19/314)! In this notebook, we ask you to use string processing and regular expressions to mine a web page, which is stored in HTML format.

# **The data: Yelp! reviews.** The data you will work with is a snapshot of a recent search on the [Yelp! site](https://yelp.com) for the best fried chicken restaurants in Atlanta. That snapshot is hosted here: https://cse6040.gatech.edu/datasets/yelp-example
# 
# If you go ahead and open that site, you'll see that it contains a ranked list of places:
# 
# ![Top 10 Fried Chicken Spots in ATL as of September 12, 2017](https://cse6040.gatech.edu/datasets/yelp-example/ranked-list-snapshot.png)

# **Your task.** In this part of this assignment, we'd like you to write some code to extract this list.

# ## Getting the data
# 
# First things first: you need an HTML file. The following Python code will download a particular web page that we've prepared for this exercise and store it locally in a file.
# 
# > If the file exists, this command will not overwrite it. By not doing so, we can reduce accesses to the server that hosts the file. Also, if an error occurs during the download, this cell may report that the downloaded file is corrupt; in that case, you should try re-running the cell.

# In[1]:


import requests
import os
import hashlib

if os.path.exists('.voc'):
    data_url = 'https://cse6040.gatech.edu/datasets/yelp-example/yelp.htm'
else:
    data_url = 'https://github.com/cse6040/labs-fa17/raw/master/datasets/yelp.htm'

if not os.path.exists('yelp.htm'):
    print("Downloading: {} ...".format(data_url))
    r = requests.get(data_url)
    with open('yelp.htm', 'w', encoding=r.encoding) as f:
        f.write(r.text)

with open('yelp.htm', 'r') as f:
    yelp_html = f.read().encode(encoding='utf-8')
    checksum = hashlib.md5(yelp_html).hexdigest()
    assert checksum == "4a74a0ee9cefee773e76a22a52d45a8e", "Downloaded file has incorrect checksum!"
    
print("'yelp.htm' is ready!")


# **Viewing the raw HTML in your web browser.** The file you just downloaded is the raw HTML version of the data described previously. Before moving on, you should go back to that site and use your web browser to view the HTML source for the web page. Do that now to get an idea of what is in that file.
# 
# > If you don't know how to view the page source in your browser, try the instructions on [this site](http://www.wikihow.com/View-Source-Code).

# **Reading the HTML file into a Python string.** Let's also open the file in Python and read its contents into a string named, `yelp_html`.

# In[2]:


with open('yelp.htm') as yelp_file:
    yelp_html = yelp_file.read()
    
# Print first few hundred characters of this string:
print("*** type(yelp_html) == {} ***".format(type(yelp_html)))
n = 1000
print("*** Contents (first {} characters) ***\n{} ...".format(n, yelp_html[:n]))


# Oy, what a mess! It will be great to have some code read and process the information contained within this file.

# ## Exercise (5 points): Extracting the ranking
# 
# Write some Python code to create a variable named `rankings`, which is a list of dictionaries set up as follows:
# 
# * `rankings[i]` is a dictionary corresponding to the restaurant whose rank is `i+1`. For example, from the screenshot above, `rankings[0]` should be a dictionary with information about Gus's World Famous Fried Chicken.
# * Each dictionary, `rankings[i]`, should have these keys:
#     * `rankings[i]['name']`: The name of the restaurant, a string.
#     * `rankings[i]['stars']`: The star rating, as a string, e.g., `'4.5'`, `'4.0'`
#     * `rankings[i]['numrevs']`: The number of reviews, as an **integer.**
#     * `rankings[i]['price']`: The price range, as dollar signs, e.g., `'$'`, `'$$'`, `'$$$'`, or `'$$$$'`.
#     
# Of course, since the current topic is regular expressions, you might try to apply them (possibly combined with other string manipulation methods) find the particular patterns that yield the desired information.

# In[3]:


from bs4 import BeautifulSoup
import re

#https://webscraping.com/blog/Web-scraping-with-regular-expressions/
#https://regex101.com

response = requests.get(data_url)
strweb = (response.content.decode("utf-8"))
results_page = BeautifulSoup(response.content,'lxml')
all_names = results_page.find_all(class_="biz-name js-analytics-click")
star_all = re.findall('title="[0-9].[0-9]', strweb)
numrevs_all = re.findall('([0-9]+\sreviews)', strweb)
price_all = results_page.find_all(class_="business-attribute price-range")
checkAd = results_page.find_all(class_="search-result-title")

rankings = []
for i, item in enumerate(all_names):
    if "Ad" not in checkAd[i].get_text():
        name = item.get_text()
        if "&" in name:
            name = name.replace("&","&amp;")
        stars = star_all[i].split("\"")[1]
        numrevs = int(numrevs_all[i].split(" ")[0])
        price = price_all[i].get_text()
        rankings.append({"name":name, "stars":stars, 'numrevs':numrevs, 'price':price})


# In[4]:


# Test cell: `rankings_test`

assert type(rankings) is list, "`rankings` must be a list"
assert all([type(r) is dict for r in rankings]), "All `rankings[i]` must be dictionaries"

print("=== Rankings ===")
for i, r in enumerate(rankings):
    print("{}. {} ({}): {} stars based on {} reviews".format(i+1,
                                                             r['name'],
                                                             r['price'],
                                                             r['stars'],
                                                             r['numrevs']))

assert rankings[0] == {'numrevs': 549, 'name': 'Gus’s World Famous Fried Chicken', 'stars': '4.0', 'price': '$$'}
assert rankings[1] == {'numrevs': 1777, 'name': 'South City Kitchen - Midtown', 'stars': '4.5', 'price': '$$'}
assert rankings[2] == {'numrevs': 2241, 'name': 'Mary Mac’s Tea Room', 'stars': '4.0', 'price': '$$'}
assert rankings[3] == {'numrevs': 481, 'name': 'Busy Bee Cafe', 'stars': '4.0', 'price': '$$'}
assert rankings[4] == {'numrevs': 108, 'name': 'Richards’ Southern Fried', 'stars': '4.0', 'price': '$$'}
assert rankings[5] == {'numrevs': 93, 'name': 'Greens &amp; Gravy', 'stars': '3.5', 'price': '$$'}
assert rankings[6] == {'numrevs': 350, 'name': 'Colonnade Restaurant', 'stars': '4.0', 'price': '$$'}
assert rankings[7] == {'numrevs': 248, 'name': 'South City Kitchen Buckhead', 'stars': '4.5', 'price': '$$'}
assert rankings[8] == {'numrevs': 1558, 'name': 'Poor Calvin’s', 'stars': '4.5', 'price': '$$'}
assert rankings[9] == {'numrevs': 67, 'name': 'Rock’s Chicken &amp; Fries', 'stars': '4.0', 'price': '$'}

print("\n(Passed!)")


# **Fin!** This cell marks the end of Part 1. Don't forget to save, restart and rerun all cells, and submit it. When you are done, proceed to Part 2.
