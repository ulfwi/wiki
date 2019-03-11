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

# filename = 'wikis/sv/articles/a/d/o/Adolf_Hitler_fdc0.html'
filename = 'wikis/sv/articles/s/e/n/Special%7ESenaste_%C3%A4ndringar_f194.html'
# filename = 'wikis/sv/articles/s/e/n/Special~Senaste_\xc3\xa4ndringar_f194.html'

a = unquote(filename).decode('utf8')

b = 'ö'
c = b.decode('utf-8')

a1 = 'g/ä/v'
b1 = a1.decode('utf8')

print b1
