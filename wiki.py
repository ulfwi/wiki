from urllib.request import urlopen
from urllib.parse import quote, unquote
from anytree import Node, find_by_attr
from collections import deque
import time


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


def find_shortest_path(start, goal, wiki_url, print_time_bool=False):

    # convert to percentage encoding
    start = quote(start)

    shortest_path = None
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
        wiki_deque = get_url_deque(wiki_url + url_parent)
        if print_time_bool: print('Downloading html: ' + str(time.time() - t))

        t = time.time()

        # add url to closed list
        wiki_deque_closed.append(url_parent)

        for url in wiki_deque:
            if not url in wiki_deque_closed and not url in wiki_deque_open:
                if url == goal:

                    goal_node = Node(url, parent=parent_node)
                    shortest_path = unquote(str(goal_node)[8:-2])

                    # break out of while loop
                    wiki_deque_open = deque([])
                    break
                else:
                    wiki_deque_open.append(url)
                    Node(url, parent=parent_node)
        
        if print_time_bool: print('Iterating over wiki_list: ' + str(time.time() - t))
    
    return shortest_path


def main():
    
    wiki_url = 'https://en.wikipedia.org/wiki/'
    # wiki_url = 'https://sv.wikipedia.org/wiki/'

    # start wiki-page
    start = 'Scottish_Terrier'
    # start = 'Zara_Larsson'
    # start = 'Torslanda'
    # start = 'Gävle'
    # start = 'Smörgåstårta'
    # start = 'Adolf_Hitler'

    # goal wiki-page
    goal = 'Adolf_Hitler'
    # goal = 'Zara_Larsson'


    # find shortest path between start and goal
    shortest_path = find_shortest_path(start, goal, wiki_url)

    if shortest_path is not None:
        print('\n' + goal + ' was found!')
        print('Shortest path: ' + shortest_path)
    else:
        print('\nNo path was found.')


if __name__ == '__main__':
    main()