#!/bin/python3

import math
import os
import random
import re
import sys

# Call print(*value, sep=" ") with value as a list to unpack and print the elements 
# of the list seperated by the zero or many characters contained in sep. To seperate 
# each element with a comma followed by a space, set sep to ", ".

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    reverse = arr[n::-1]
    print(*reverse)
    
