# twitter_networkx
This Python application provides a means to calculate the rolling average degree of a vertex in a Twitter hashtag graph within a 60-second window.

The following python packages are used:
_ json
_ Datetime
_ itertools
_ networkx

The two main scripts are:
1/ avgDegree.py:
  contains the main function for calculation the rolling average degree of a vertex.
2/ twtFunc.py
  contains 4 user-defined functions for i) getting the hashtag txt; ii)sort and remove expired hashtags; iii)creating list of edges among hashtags and iv)calculating the number of nodes and degrees using networkx
