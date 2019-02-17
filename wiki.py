# coding=utf-8
""" Contains a class that can find the shortest path to Hitler on wikipedia """
import sys
from collections import deque
import time
from node import Node

# check python version
if sys.version_info[0] < 3:
    from six.moves import urllib
    from urllib import urlopen, quote, unquote
else:
    from urllib.request import urlopen
    from urllib.parse import quote, unquote


class WikiSearcher(object):
    """ Class that can find the shortest path to Hitler on wikipedia """

    def __init__(self, wiki_url):
        """ Creates a Wiki Search object """
        self.wiki_url = wiki_url

    def set_wiki_url(self, wiki_url):
        """ Change the wiki url """
        self.wiki_url = wiki_url

    def get_url_deque(self, subject_parent):
        """ Returns a deque object containing all urls that the page subject_parent links to """

        url = self.wiki_url + subject_parent

        # download html
        html = urlopen(url).read().decode('utf-8')

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


    def find_shortest_path(self, start, goal, print_time_bool=False):
        """ Finds shortest path between start and goal on wikipedia """

        # convert to percentage encoding
        start = quote(start)
        goal = quote(goal)

        shortest_path = None
        node = Node(start)
        wiki_deque_open = deque([start])
        wiki_deque_closed = deque([])
        while wiki_deque_open:

            # pop subject from open list
            subject_parent = wiki_deque_open.popleft()

            t_0 = time.time()
            node = Node.find(subject_parent)
            if print_time_bool:
                print('Finding parent node: ' + str(time.time() - t_0))

            # convert from percentage encoding
            print(unquote(str(node)))

            t_0 = time.time()
            # get children of url
            wiki_deque = WikiSearcher.get_url_deque(self, subject_parent)
            if print_time_bool:
                print('Downloading html: ' + str(time.time() - t_0))

            t_0 = time.time()

            # add url to closed list
            wiki_deque_closed.append(subject_parent)

            for url in wiki_deque:
                if not url in wiki_deque_closed and not url in wiki_deque_open:
                    if url == goal:

                        goal_node = node.create_child(url)
                        shortest_path = unquote(str(goal_node))

                        # break out of while loop
                        wiki_deque_open = deque([])
                        break
                    else:
                        wiki_deque_open.append(url)
                        node.create_child(url)

            if print_time_bool:
                print('Iterating over wiki_list: ' + str(time.time() - t_0))

        return shortest_path
