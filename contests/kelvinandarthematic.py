import string
# from sortedcontainers import SortedList
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from typing import List, Set, Tuple, Optional
from itertools import pairwise, permutations, combinations
from heapq import heappush, heappop
from random import shuffle
from functools import cmp_to_key, lru_cache
from fractions import Fraction

def main() :
    n = int(input())
    arr = list(map(int , input().split()))
    odds = evens = points = s = 0
    for val in arr :
        if val % 2 == 0 : evens += 1
        else : odds += 1

    pairs = min(odds, evens)
    print(pairs)
    
    

t = int(input())
for i in range(t) : main()