def scrape():

    import pandas as pd
    from bs4 import BeautifulSoup
    import requests
    import os
    from splinter import Browser

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    scraped_data={}

    # # NASA Mars News
    url="https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title=soup.find("div", class_="content_title").text
    news_p=soup.find("div", class_="article_teaser_body").text
    scraped_data["news_title"]=news_title
    scraped_data["news_p"]=news_p


    # # JPL Mars Space Images - Featured Image
    url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    gah=soup.find("a",class_="button fancybox")
    feature_image_url=f'https://www.jpl.nasa.gov{gah["data-fancybox-href"]}'
    scraped_data["feature_image_url"]=feature_image_url


    # # Mars Weather
    url="https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    html=browser.html
    soup=BeautifulSoup(html, 'html.parser')
    mars_weather=soup.find("p", class_="js-tweet-text").text
    scraped_data["mars_weather"]=mars_weather


    # # Mars Facts
    url="https://space-facts.com/mars/"
    tables=pd.read_html(url)
    mars_facts_df=tables[0]
    mars_facts = mars_facts_df.to_html()
    
    scraped_data["mars_facts"] = mars_facts


    # Mars Hemispheres
    #url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    #browser.visit(url)
    #html=browser.html
    #soup=BeautifulSoup(html, 'html.parser')

    browser.quit()

    return(scraped_data)






