# coding=utf-8
""" Contains a class that can find the shortest path to Hitler on wikipedia """
import sys
import os
import time
from collections import deque
from tree import Tree

# check python version
if sys.version_info[0] < 3:
    from six.moves import urllib
    from urllib import urlopen, quote, unquote
else:
    from urllib.request import urlopen
    from urllib.parse import quote, unquote


class WikiSearcher(object):
    """ Class that can find the shortest path to Hitler on wikipedia """

    def __init__(self, wiki_url, retrieval_mode='online'):
        """ Creates a Wiki Search object """
        self.wiki_url = wiki_url
        self.retrieval_mode = retrieval_mode

    def set_wiki_url(self, wiki_url):
        """ Change the wiki url """
        self.wiki_url = wiki_url

    def set_retrieval_mode(self, retrieval_mode):
        """ Change the retrieval mode (online or offline) """
        self.retrieval_mode = retrieval_mode

    def get_url_deque(self, subject_parent):
        """ Returns a deque object containing all urls that the page subject_parent links to """

        if self.retrieval_mode == 'online':
            url = self.wiki_url + subject_parent

            # download html
            html = urlopen(url).read()

            regexp_beg = 'href="/wiki/'

        elif self.retrieval_mode == 'offline':
            filename = 'wikis/sv/articles/' + unquote(subject_parent)

            try:
                with open(filename) as wiki_file:
                    html = wiki_file.read()
            except:
                return ([])

            regexp_beg = 'href="../../../../articles/'

        regexp_end = '"'

        beg = 0
        end = len(html)
        wiki_deque = ([])

        while beg != -1:
            # find regexp_beg in html string
            beg = html.find(regexp_beg, beg + 1, end)
            if beg != -1:
                # find last index of url
                end_url = html.find(regexp_end, beg + len(regexp_beg), end)

                # extract subject
                url = html[beg + len(regexp_beg):end_url]

                # don't include urls with : in them
                if url.find(':') == -1 \
                    and url.find(quote('~')) == -1:
                    # and url.find(quote('Bild~')) == -1 \
                    # and url.find(quote('Användardiskussion~')) == -1 \
                    # and url.find(quote('Användare~')) == -1 \
                    # and url.find(quote('Kategori~')) == -1:
                    wiki_deque.append(url)

        return wiki_deque

    def find_offline_file(self, subject):
        """ Finds offline file corresponding to the subject """

        # get first three letters
        idx = 0
        let0 = subject[idx].lower()
        # check if unicode characters
        if let0 == '\xc2' or let0 == '\xc3':
            let0 = subject[idx:idx+2].lower()
            idx += 1
        idx += 1
        let1 = subject[idx].lower()
        if let1 == '\xc2' or let1 == '\xc3':
            let1 = subject[idx:idx+2].lower()
            idx += 1
        idx += 1
        let2 = subject[idx].lower()
        if let2 == '\xc2' or let2 == '\xc3':
            let2 = subject[idx:idx+2].lower()

        path = 'wikis/sv/articles/' + let0 + '/' + let1 + '/' + let2 + '/'

        # iterate over all files in the directory
        file_name_list = os.listdir(path)
        for file_name in file_name_list:

            # check if the file name matches the subject (10 represents _xxxx.html)
            if file_name[:len(subject)] == subject \
                and ((len(file_name) == len(subject) + 10 and file_name[len(subject)] == '_') \
                or len(file_name) == len(subject) + len('.html')):

                file_path = let0 + '/' + let1 + '/' + let2 + '/' + file_name
                return file_path

        return None


    def find_shortest_path(self, start, goal, print_time_bool=False):
        """ Finds shortest path between start and goal on wikipedia """

        # find offline file
        if self.retrieval_mode == 'offline':
            start = self.find_offline_file(start)
            goal = self.find_offline_file(goal)

        # convert to percentage encoding
        start = quote(start)
        goal = quote(goal)

        # create node tree
        tree = Tree()

        shortest_path = None
        node = tree.add_node(start)
        wiki_deque_open = deque([start])
        wiki_deque_closed = deque([])
        while wiki_deque_open:

            # pop subject from open list
            subject_parent = wiki_deque_open.popleft()

            t_0 = time.time()
            node = tree.find(subject_parent)
            if print_time_bool:
                print('Finding parent node: ' + str(time.time() - t_0))

            # convert from percentage encoding
            print(unquote(tree.get_ancestors_str(node)))

            t_0 = time.time()
            # get children of url
            wiki_deque = self.get_url_deque(subject_parent)
            if print_time_bool:
                print('Downloading html: ' + str(time.time() - t_0))

            t_0 = time.time()

            # add url to closed list
            wiki_deque_closed.append(subject_parent)

            for url in wiki_deque:
                if not url in wiki_deque_closed and not url in wiki_deque_open:
                    if url == goal:

                        goal_node = tree.create_child(url, node)
                        shortest_path = unquote(tree.get_ancestors_str(goal_node))
                        print(shortest_path)

                        # break out of while loop
                        wiki_deque_open = deque([])
                        break
                    else:
                        wiki_deque_open.append(url)
                        tree.create_child(url, node)

            if print_time_bool:
                print('Iterating over wiki_list: ' + str(time.time() - t_0))

        return shortest_path
