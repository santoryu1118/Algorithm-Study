#(6) - 2294 동전 2
'''
n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 
그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.
'''

import sys
from collections import deque

n, k = map(int, input().split())
coins = list(map(int, sys.stdin.readlines()))

