from bs4 import BeautifulSoup
from collections import deque
import urllib
import time
import re
import random
import articlename as an
import extractlinks as el
import newtab as nt


# Finds the path between articles using BFS.
def find_path(start_article, end_article, degree_of_connection):
    if(degree_of_connection == 0):
        return
    array_of_links = el.extract_links_to_list(start_article, 2) # list of lists
    #BFS:
    queue = deque(array_of_links)
    visited = dict() 
    queue.append(array_of_links[0])
    finished = False
    while queue: 
        if finished:
            break
        curr = queue.popleft()
        curr_article = curr[0]
        curr_degree = curr[1]
        parent_article = curr[2]
        # Checks whether the given level has been reached.
        if curr_degree > degree_of_connection: 
            print('\nWhoops...... No link exists :/')
            break
        if curr_article == end_article:
            print('\nArticle {} found at level'.format(curr_article), curr_degree)
            time.sleep(2)
            # Finds the path to the start article and adds them to a stack
            stack = deque()
            while curr_article != start_article:
                stack.append(curr_article)
                curr_article = visited[curr_article]
            stack.append(curr_article)
            nt.open_in_new_tab(stack)
            break
        visited[curr_article] = parent_article
        curr_array_of_links = el.extract_links_to_list(curr_article, curr_degree)
        for link in curr_array_of_links:
            if link[0] not in visited:
                link[1] = curr_degree + 1
                link[2] = curr_article
                queue.append(link)
                visited[link[0]] = link[2]
            if link[0] == end_article:
                article = link[0]
                print('Article {} found at level'.format(article), link[1])
                time.sleep(2)
                # Finds the path to the start article and adds them to a stack
                stack = deque()
                while article != start_article:
                    stack.append(article)
                    article = visited[article]
                stack.append(article)
                nt.open_in_new_tab(stack)
                finished = True
                break


def find_link(start_article, end_article):
    if(start_article == end_article):
        print('Searching............ \n')
        time.sleep(2)
        print('Oh wait! The destination article is the same as the source article :)')
        return
    find_path(start_article, end_article, 3)
