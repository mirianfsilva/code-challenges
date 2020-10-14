#!/bin/python3

import math
import os
import random
import re
import sys
import operator

def max_repetition(binary):
    n = len(binary) 
    count = 0
    cur_count = 1
  
    for i in range(n):
        if ( i+1 < n and (binary[i] == binary[i+1]) and binary[i] == '1'): 
            cur_count += 1
        else:
            if (cur_count > count):
                count = cur_count
            cur_count = 1
    print(max(count, cur_count)) 

if __name__ == '__main__':
    n = int(input())
    binary = str("{0:b}".format(n))
    max_repetition(binary)
