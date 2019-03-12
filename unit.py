# coding=utf-8
""" Unit tests for wiki.py """
import unittest
import wiki


class TestWiki(unittest.TestCase):
    """ Unit tests for wiki.py """

    def test_terrier(self):
        """
        Tests if the correct path from Scottish_Terrier to Adolf_Hitler is found
        """

        wiki_url = 'https://en.wikipedia.org/wiki/'
        start = 'Scottish_Terrier'
        goal = 'Adolf_Hitler'

        wiki_searcher = wiki.WikiSearcher(wiki_url)

        shortest_path = wiki_searcher.find_shortest_path(start, goal)
        actual_shortest_path = 'Scottish Terrier/Franklin Delano Roosevelt/Adolf Hitler'
        self.assertEqual(shortest_path, actual_shortest_path)


    def test_offline(self):
        """
        Tests offline
        """

        wiki_url = ''
        start = 'Torslanda'
        goal = 'Adolf_Hitler'

        wiki_searcher = wiki.WikiSearcher(wiki_url, retrieval_mode='offline')

        shortest_path = wiki_searcher.find_shortest_path(start, goal)
        actual_shortest_path = 'Torslanda/Göteborgs kommun/1938/Adolf Hitler fdc0'
        self.assertEqual(shortest_path, actual_shortest_path)

    def test_underscore_input(self):
        """
        Tests offline
        """

        wiki_url = ''

        # with underscore
        start = 'Skolor_i_Arboga'
        goal = 'Adolf_Hitler'

        wiki_searcher = wiki.WikiSearcher(wiki_url, retrieval_mode='offline')

        shortest_path = wiki_searcher.find_shortest_path(start, goal)
        actual_shortest_path = 'Skolor i Arboga 217d/Arboga/1952/Adolf Hitler fdc0'
        self.assertEqual(shortest_path, actual_shortest_path)

        # without underscore
        start = 'Skolor i Arboga'
        goal = 'Adolf Hitler'

        shortest_path = wiki_searcher.find_shortest_path(start, goal)
        self.assertEqual(shortest_path, actual_shortest_path)

    def test_offline_gavle(self):
        """
        Tests offline with first page with a non-ascii letter
        """

        wiki_url = ''
        start = 'Gävle'
        goal = 'Svenskt_Näringsliv'

        wiki_searcher = wiki.WikiSearcher(wiki_url, retrieval_mode='offline')

        shortest_path = wiki_searcher.find_shortest_path(start, goal)
        actual_shortest_path = 'Gävle/Gävleborgs län/Jämtlands län/Svenskt Näringsliv af61'
        self.assertEqual(shortest_path, actual_shortest_path)


    def test_smorgastarta(self):
        """
        Tests non-ascii letters
        """

        wiki_url = 'https://sv.wikipedia.org/wiki/'
        start = 'Smörgåstårta'
        goal = 'Svenskt_Näringsliv'

        wiki_searcher = wiki.WikiSearcher(wiki_url)

        shortest_path = wiki_searcher.find_shortest_path(start, goal)
        actual_shortest_path = 'Smörgåstårta/Sveriges nationaldag/Svenskt Näringsliv'
        self.assertEqual(shortest_path, actual_shortest_path)

    # def test_long_path(self):
    #     """
    #     Tests long path to Hitler
    #     """

    #     wiki_url = 'https://sv.wikipedia.org/wiki/'
    #     start = 'Smörgåstårta'
    #     goal = 'Svenskt_Näringsliv'

    #     shortest_path = wiki.find_shortest_path(start, goal, wiki_url)
    #     actual_shortest_path = 'Smörgåstårta/Sveriges_nationaldag/Svenskt_Näringsliv'
    #     self.assertEqual(shortest_path, actual_shortest_path)

if __name__ == '__main__':
    unittest.main()
