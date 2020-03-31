# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 

n = int(input())
phonebook = dict()

def check_key(dict, key):
    if key in dict:
        print("{}={}".format(key, dict[key]))
        # print(key, dict[key])
    else:
        print("Not found")

for _ in range(0,n):
    name, phonenumber = input().split()
    phonebook[name] = phonenumber

while True: 
    try:
        key =input()
        check_key(phonebook,key)
    except EOFError:
        break
