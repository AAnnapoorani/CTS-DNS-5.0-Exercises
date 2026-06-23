# Exercise 27

def capitalize_words(s):
	return ' '.join(w.capitalize() for w in s.split())


print(capitalize_words("hello world from python"))

