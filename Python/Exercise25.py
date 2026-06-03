# Exercise 25

def contains_vowel(s):
	return any(ch in 'aeiouAEIOU' for ch in s)


print(contains_vowel("Rhythm"))

