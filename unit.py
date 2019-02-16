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

        shortest_path = wiki.find_shortest_path(start, goal, wiki_url)
        actual_shortest_path = 'Scottish_Terrier/Franklin_Delano_Roosevelt/Adolf_Hitler'
        self.assertEqual(shortest_path, actual_shortest_path)


    def test_smorgastarta(self):
        """
        Tests non-ascii letters
        """

        wiki_url = 'https://sv.wikipedia.org/wiki/'
        start = 'Smörgåstårta'
        goal = 'Svenskt_Näringsliv'

        shortest_path = wiki.find_shortest_path(start, goal, wiki_url)
        actual_shortest_path = 'Smörgåstårta/Sveriges_nationaldag/Svenskt_Näringsliv'
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
