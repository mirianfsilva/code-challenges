#Generalized GCD factors numbers
import math 

def generalizedGCD(num, arr):
    factors = arr[0]
    for i in range(0, len(arr)):
        factors = math.gcd(factors, arr[i])
    return factors