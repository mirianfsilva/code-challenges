# Enter your code here. Read input from STDIN. Print output to STDOUT
import string
import sys

n = int(input())
# string[start : stop : step size]

for i in range (0,n):
    mystr = input()
    print( mystr[0::2] , mystr[1::2] )
