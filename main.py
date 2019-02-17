# coding=utf-8
""" Main function that uses the WikiSearcher class """
import time
import wiki

def main():
    """ Wiki main function """

    # wiki_url = 'https://en.wikipedia.org/wiki/'
    wiki_url = 'https://sv.wikipedia.org/wiki/'

    # start wiki-page
    # start = 'Scottish_Terrier'
    # start = 'Zara_Larsson'
    # start = 'Torslanda'
    # start = 'Gävle'
    start = 'Smörgåstårta'
    # start = 'Adolf_Hitler'

    # goal wiki-page
    # goal = 'Adolf_Hitler'
    # goal = 'Zara_Larsson'
    goal = 'Svenskt_Näringsliv'

    # create wiki search object
    wiki_searcher = wiki.WikiSearcher(wiki_url)

    t_0 = time.time()
    # find shortest path between start and goal
    shortest_path = wiki_searcher.find_shortest_path(start, goal)

    if shortest_path is not None:
        print('\n' + goal + ' was found in ' + str(round(time.time()-t_0, 2)) + ' seconds!')
        print('Shortest path: ' + shortest_path)
    else:
        print('\nNo path was found.')


if __name__ == '__main__':
    main()