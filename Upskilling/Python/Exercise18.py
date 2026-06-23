# Exercise 18

def convert_seconds(sec):
	if sec < 0:
		return "Invalid"

	hrs = sec // 3600
	sec %= 3600
	mins = sec // 60
	sec %= 60

	return f"{hrs}h {mins}m {sec}s"


total_seconds = 10000

print(convert_seconds(total_seconds))
