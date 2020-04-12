#!/bin/python3

import sys

S = input().strip()

try:
    S.isdigit() == True
    print(int(S))
except:
    print("Bad String")

