def fatorial(n):
	fat = 1
	for i in range(1,n+1):
		fat = fat * i
		#print (i)
	return fat

def fib(n):
	k = 0 
	if (n == 0 or n == 1):
		k = k + n
		return n
	else:
		return fib(n -1) + fib(n-2)  

def primo(n):
	k = 2

	if (n < 0):
		n = n * (-1)

	while (k*k <= n): # O(sqrt(n))
		if (n % k == 0):
			return False;
		k = k + 1
	return True


temp = primo(13)
if temp == False:
	print("no")
elif temp == True:
	print("yes")
