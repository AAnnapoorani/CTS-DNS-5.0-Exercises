# Exercise 28

def write_greeting(name):
	with open('greeting.txt', 'w') as f:
		f.write(f"Hello, {name}!")


write_greeting('Annapoorani')
