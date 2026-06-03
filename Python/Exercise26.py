# Exercise 26

def count_words(s):
	if not s:
		return 0

	return len(s.split())


print(count_words("Hello world from Python"))
