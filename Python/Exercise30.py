# Exercise 30

def append_text(text):
	with open('notes.txt', 'a') as f:
		f.write(text + '\n')


append_text('This is a note')

