#!/usr/bin/python
# -*- coding: utf-8 -*-


from splinter import Browser

# open a browser
browser = Browser('chrome')
browser.visit('https://howtodoinjava.com/spring-mvc-tutorial/')

# I recommend using single quotes
# search_bar_xpath = '//*[@id="lst-ib"]'
# search_bar = browser.find_by_xpath(search_bar_xpath)[0]
#
# search_bar.fill("CodingStartups.com")

# search_button_xpath = '//*[@id="tsf"]/div[2]/div[3]/center/input[1]'
# search_button = browser.find_by_xpath(search_butt on_xpath)[0]
# search_button.click()

# //*[@id="rso"]/div/div/div[1]/div/div/h3/a
search_results_xpath = '//*[@id="menu-spring-mvc"]'  # simple, right?

search_results = browser.find_by_xpath(search_results_xpath)

scraped_data = []
for search_result in search_results:
    title = search_result.html  # trust me
    print(title)