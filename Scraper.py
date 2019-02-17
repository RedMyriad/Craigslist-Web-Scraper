# author: Francisco J Lopez
# Project purposes only
# Purpose: To scrape Craigslist for the latest graphics card deals
# 2/10/2019

import bs4 as bs
import urllib3
import sys
import PyQt5

bad_input = True
# while(True):
#     user_location = input('''Please enter your location
# Example: Pasco, WA
# Location: ''')
#     # cleaning up intput
#     user_location = user_location.lower()
#     user_location = ''.join(user_location.split())
#     if user_location.find(',') == -1 or user_location.find(',') == 0:
#         print('Error: incorrect format.')
#         continue
#     else:
#         user_location = user_location.split(',')
#         for term in user_location:
#             if term.isnumeric():
#                 break
#             else:
#                 bad_input = False
#
#         if bad_input == False:
#             break
#         print('Error: incorrect format.')
#


def populate_list(phrase, region):

    user_location = region
    searchable = phrase

    user_location = user_location.lower()
    user_location = ''.join(user_location.split())
    user_location = user_location.split(',')

    searchable = searchable.lower()
    searchable = searchable.split(' ')
    items = 0
    if len(searchable) == 1:
        items = 1

    search_modified = ""
    for i in searchable:
        search_modified += i + "%20"

    if items != 1:
        searchable = search_modified[0:-3]
    else:
        searchable = search_modified
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://www.craigslist.org/about/sites')
    page_html = r.data

    location_soup = bs.BeautifulSoup(page_html, 'lxml')
    location_soup = location_soup.find('div', {'colmask'})

    # Start: creates a dictionary populated with states as keys
    states = []
    for state in location_soup.findAll('h4'):
        states.append(state.get_text())

    cities = []
    for city_group in location_soup.findAll('ul'):
        cities.append(city_group)

    location_dict = {}
    for i in range(len(cities)):
        city_list = []
        # cities is populated with 'ul' tags which have cities in them
        # this code separates those cities in each ul tag and puts them
        # in a new list which go into a dictionary
        for city in cities[i].findAll('li'):
            city_list.append(city)
        location_dict[str(states[i]).lower()] = city_list

    # End

    # find what state the user is from
    user_region = ''
    for state in location_dict:
        state = str(state)
        if state.startswith(user_location[1]) == True:
            for city in location_dict[state]:
                city_name = city.find('a').get_text()
                if city_name.find(user_location[0]) != -1:
                    # get the specific string url location-string for the region
                    user_region = city.find('a')['href']
                    user_region = user_region.split('//')
                    user_region = user_region[1]
                    user_region = user_region.split('.')
                    user_region = user_region[0]

    # find postings in that region with the "graphics card" keyword
    http = urllib3.PoolManager()

    r = http.request('GET', 'https://{}.craigslist.org/search/sss?query={}'.format(user_region, searchable))
    page_html = r.data
    soup = bs.BeautifulSoup(page_html, 'lxml')

    posts = []
    for post in soup.findAll('li', {'class': 'result-row'}):
        post_data = {}
        post_data['date'] = post.time['title']
        post_data['title'] = post.find('a', {'class': 'result-title'}).get_text()
        if(post.select_one('span[class*=result-price]') != None):
            post_data['price'] = post.select_one('span[class*=result-price]').text
        else:
            post_data['price'] = 'None'

        post_data['link'] = post.find('a', {'class':'result-title'})['href']
        posts.append(post_data)

    return posts
