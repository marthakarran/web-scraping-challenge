#!/usr/bin/env python
# coding: utf-8

# In[24]:


# Import dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd 
import requests 


# In[25]:


# Set Executable Path & Initialize Chrome Browser
executable_path = {"executable_path": "./chromedriver.exe"}
browser = Browser("chrome", **executable_path)


# In[3]:


# Visit NASA Mars News Site 
url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[4]:


# Parse HTML with Beautiful Soup
html = browser.html
soup = BeautifulSoup(html, "html.parser") 


# In[5]:


# Retrieve the latest element that contains news title and news paragraph
news_title = soup.find('div', class_='content_title').find('a').text
news_p = soup.find('div', class_='article_teaser_body').text


# In[6]:


# Display  data 
print(news_title)
print(news_p)


# In[7]:


# Visit JPL Mars Space Images through splinter module
feat_img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(feat_img_url)


# In[8]:


# Parse HTML with Beautiful Soup
html_image = browser.html
soup = BeautifulSoup(html_image, 'html.parser')


# In[9]:


# Retrieve background-image url from style tag 
featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]


# In[10]:


# Website Url 
main_url = 'https://www.jpl.nasa.gov'


# In[11]:


# Concatenate website url with scrapped route
featured_image_url = main_url + featured_image_url


# In[12]:


# Display link to featured image
featured_image_url


# In[13]:


# Visit Mars Weather twitter account through splinter module
weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(weather_url)


# In[14]:


# Parse HTML with Beautiful Soup
html_weather = browser.html
weather_soup = BeautifulSoup(html_weather, 'html.parser')


# In[15]:


# Find tweet text 
mars_weather_tweet = weather_soup.find("div", 
                                       attrs={
                                           "class": "tweet", 
                                            "data-name": "Mars Weather"
                                        })


# In[19]:


# Retrieve weather
mars_weather = mars_weather_tweet.find("p", "tweet-text").get_text()
print(mars_weather)


# In[20]:


# Visit Mars facts url 
facts_url = 'http://space-facts.com/mars/'


# In[21]:


# Use Pandas to parse the url
mars_facts = pd.read_html(facts_url)


# In[22]:


# Create dataframe
mars_df = mars_facts[0]
mars_df.columns = ['Description','Value']
mars_df.set_index('Description', inplace=True)
mars_df.to_html()
data = mars_df.to_dict(orient='records')  # Here's our added param..
mars_df


# In[26]:


# Visit hemispheres website through splinter module 
hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemispheres_url)


# In[27]:


# Parse HTML with Beautiful Soup
html_hemispheres = browser.html
soup = BeautifulSoup(html_hemispheres, 'html.parser')


# In[28]:


# Retreive  items that contain info about Mars hemispheres
items = soup.find_all('div', class_='item')
hemisphere_image_urls = []


# In[29]:


# Store the URL 
hemispheres_main_url = 'https://astrogeology.usgs.gov'


# In[30]:


# Loop through the items previously stored
for i in items: 
    title = i.find('h3').text
    partial_img_url = i.find('a', class_='itemLink product-item')['href']
    browser.visit(hemispheres_main_url + partial_img_url)
    partial_img_html = browser.html
    soup = BeautifulSoup( partial_img_html, 'html.parser')
    img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
    hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
    
hemisphere_image_urls

