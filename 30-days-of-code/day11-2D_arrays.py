#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    max_sum = - sys.maxsize - 1

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    for i in range(0,6):
        for j in range(0,6):
            if (i+2 < 6 and j+2 < 6):
                arr_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
                if (arr_sum > max_sum):
                    max_sum = arr_sum
            else:
                pass
    
    print(max_sum)
                
