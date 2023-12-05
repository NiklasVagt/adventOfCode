import re
from collections import defaultdict

def taskOne():
  with open('day3/input.txt') as f:
    lines = f.readlines()
    dic = defaultdict(dict)
    for index in range(len(lines)):
      symbols = [*lines[index]]
      for indexS in range(len(symbols)):
        dic[index][indexS] = symbols[indexS]
    print(dic)
    

taskOne()