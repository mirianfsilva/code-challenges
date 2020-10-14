"""
The deque will be acting very much like an ordinary queue. I use of the dual functionality of the deque. 
The front of the deque will hold the first character of the string and the rear of the deque will hold the last character.

Since we can remove both of them directly, we can compare them and continue only if they match. 
If we can keep matching first and the last items, we will eventually either run out of characters
or be left with a deque of size 1 depending on whether the length of the original string was even 
or odd. In either case, the string must be a palindrome.
"""

from collections import deque

def is_palindrome(characters):
	char_deque = deque(characters)

	while len(char_deque) > 1:
		first =	char_deque.popleft() 
		last = char_deque.pop()

		if (first != last):
			return False

	return True


is_palindrome('radar') # => true
is_palindrome('word') # => false 