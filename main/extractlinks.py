from bs4 import BeautifulSoup
import random
import urllib
import re

# Returns the URL for the given article.
def get_url(article_name):
    return 'https://en.wikipedia.org/wiki/' + article_name


# Opens the given article and parses the html page. 
# Finds the links in the page and refines them and adds them to a list along with the level and parent article.
def extract_links_to_list(article, level):
    url = get_url(article)
    html_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_page,'lxml')
    array_of_links = []
    soup = soup.find(id='bodyContent')
    array_of_links = (soup.find_all(href=re.compile("^/wiki/")))
    for i in range(len(array_of_links)): 
        array_of_links[i] = [array_of_links[i]['href'].split('/')[2], level, article] 
    # Prints a random fact from the facts.txt file
    lines = open('facts.txt').read().splitlines() 
    myline = random.choice(lines)
    print(myline)
    # Removes unwanted links such as images and help articles
    for link in array_of_links[:]:
        if (link[0].find(':') != -1 or link[0].find('(disambiguation)') != -1 or link[0].find('.png') != -1):
            array_of_links.remove(link)
    return array_of_links