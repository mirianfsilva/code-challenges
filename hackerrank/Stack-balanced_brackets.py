#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    open_brackets = ["(", "[", "{"]
    close_brackets = [")", "]", "}"]
    stack = []
    for bracket in s: 
        if (bracket in open_brackets):
            stack.append(bracket) 
        elif (bracket in close_brackets):
            closed = close_brackets.index(bracket) 
            if ((len(stack) > 0) and (open_brackets[closed] == stack[len(stack)-1])): 
                stack.pop() 
            else:
                return ("NO")
    if (len(stack) == 0): 
        return ("YES")
    else:
        return("NO")


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        print(result)