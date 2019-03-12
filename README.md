# wiki

Finds shortest path between two wikipedia pages.

Download link to swedish wikipedia: https://dumps.wikimedia.org/other/static_html_dumps/current/sv/

Profiler: python -m cProfile main.py

# TODO

* Check if wikipage actually exists
    * Add unit test for this
        * No path was found maybe?

* Add unit test for long paths

* Write node module in C instead

* Save the title of the page in the node (e.g. "Adolf Hitler" instead of Adolf_Hitler)

* File name searcher is not very sofisticated

* Remove last _xxxx from print

* Change so that wiki_url also can be file path to offline storage

* Add user input
