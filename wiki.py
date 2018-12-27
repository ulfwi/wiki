from urllib.request import urlopen
from urllib.parse import quote, unquote
from anytree import Node, find_by_attr
from collections import deque
import time

wiki = 'https://en.wikipedia.org/wiki/'
# wiki = 'https://sv.wikipedia.org/wiki/'

# start wiki-page
# start = 'Eva_Braun'
# start = 'Rome'
# start = 'Scottish_Terrier'
# start = 'Monopoly_(game)'
# start = 'Zara_Larsson'
# start = 'Torslanda'
# start = 'Gävle'
start = 'Smörgåstårta'
# start = 'Salata_de_boeuf'
# start = 'Adolf_Hitler'

# goal wiki-page
goal = 'Adolf_Hitler'
# goal = 'Zara_Larsson'

# convert to percentage encoding
start = quote(start)

# TODO
# class Node():
# make wiki_list_open into a queue (collections.deque)

print_time_bool = False

def get_url_deque(wiki_url):

    # download html
    html = urlopen(wiki_url).read().decode('utf-8')

    regexp_beg = 'href="/wiki/'
    regexp_end = '"'

    beg = 0
    end = len(html)
    wiki_deque = ([])

    while beg != -1:
        # find regexp_beg in html string
        beg = html.find(regexp_beg, beg + 1, end)
        if beg != -1:
            # find last index of url
            end_url = html.find(regexp_end, beg + 6, end)

            # extract subject
            url = html[beg + 12:end_url]

            # don't include urls with : in them
            if url.find(':') == -1:
                wiki_deque.append(url)

    return wiki_deque


start_node = Node('')
parent_node = Node(start, parent=start_node)
wiki_deque_open = deque([start])
wiki_deque_closed = deque([])
while wiki_deque_open:

    # pop url from open list
    url_parent = wiki_deque_open.popleft()

    t = time.time()
    parent_node = find_by_attr(start_node, url_parent)
    if print_time_bool: print('Finding parent node: ' + str(time.time() - t))

    # convert from percentage encoding 
    print(unquote(str(parent_node)[8:-2]))

    t = time.time()
    # get children of url
    wiki_deque = get_url_deque(wiki + url_parent)
    if print_time_bool: print('Downloading html: ' + str(time.time() - t))

    t = time.time()

    # add url to closed list
    wiki_deque_closed.append(url_parent)

    for url in wiki_deque:
        if not url in wiki_deque_closed and not url in wiki_deque_open:
            if url == goal:
                print('\n' + goal + ' was found!')
                goal_node = Node(url, parent=parent_node)
                print('Shortest path: ' + unquote(str(goal_node)[8:-2]))

                # break out of while loop
                wiki_deque_open = deque([])
                break
            else:
                wiki_deque_open.append(url)
                Node(url, parent=parent_node)
    
    if print_time_bool: print('Iterating over wiki_list: ' + str(time.time() - t))
