# Exercise 19

def is_palindrome(s):
	s = ''.join(e for e in s.lower() if e.isalnum())
	return s == s[::-1]


word = "Racecar"

print(is_palindrome(word))

