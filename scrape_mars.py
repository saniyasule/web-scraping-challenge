# Dependencies
import os
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
import html5lib 

def init_browser():
    executable_path = {"executable_path": "C:/Program Files/chromedriver_win32/chromedriver.exe"}
    return Browser("chrome", **executable_path,headless= False)

def scrape():
    # create a python dictionary to store all the data 
    scrape_dict = {}

    #Scrape nasa news
    nasa_url = 'https://mars.nasa.gov/news/'
    response = requests.get(nasa_url)
    nasa_soup = BeautifulSoup(response.text, 'html.parser')
    # Parse HTML with Beautiful Soup

    news_title = nasa_soup.find('div',class_ ="content_title").find('a').text
    

    p_results= nasa_soup.find_all("div", class_="rollover_description_inner")
    news_p = p_results[0].text.strip()
   

    # store into python dictionary
    scrape_dict['news_title']=news_title
    scrape_dict['news_p']=news_p 
    
    # Scrape JPL Mars Space Images
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    response = requests.get(jpl_url)
    # Parse HTML with Beautiful Soup
    jpl_soup = BeautifulSoup(response.text, 'html.parser')

    featured = jpl_soup.find('div',class_ ="default floating_text_area ms-layer")
    featured_image = featured.find('footer')
    featured_image_url = 'https://www.jpl.nasa.gov'+ featured_image.find('a')['data-fancybox-href']
    print(str(featured_image_url))
    
    # store into python dictionary
    scrape_dict['featured_image_url']=featured_image_url

    # Scrape Mars Weather
    weather_url = "https://twitter.com/marswxreport?lang=en"
    response = requests.get(weather_url)
    # Parse HTML with Beautiful Soup
    weather_soup = BeautifulSoup(response.text, 'lxml')

    tweets = weather_soup.find('div',class_ ="js-tweet-text-container")
    mars_weather = tweets.find('p',class_="js-tweet-text").text
    mars_weather
    # store into python dictionary
    scrape_dict['mars_weather']=mars_weather

    # Scrape Mars Facts
        # Mars Facts
    # visit the webset 
    facts1_url = 'https://space-facts.com/mars/'
    # extract mars facts and make it a dataframe
    facts1 = pd.read_html(facts1_url)
    facts1_df = facts1[0]
    facts1_df_html = facts1_df.to_html()
    # visit the webset 
    facts2_url = 'https://space-facts.com/mars/'
    # extract mars facts and make it a dataframe
    facts2 = pd.read_html(facts2_url)
    facts2_df = facts2[1]
    facts2_df_html = facts2_df.to_html()

    scrape_dict["Facts1"]= facts1_df_html

    scrape_dict["Facts2"]= facts2_df_html

       # Mars Hemispheres
    # visit the webse
    

    return scrape_dict 

