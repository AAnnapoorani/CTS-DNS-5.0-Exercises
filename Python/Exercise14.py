# Exercise 14

def assign_grade(score):
	if not (0 <= score <= 100):
		return "Invalid Score"

	if score >= 80:
		grade = "A"
	elif score >= 60:
		grade = "B"
	else:
		grade = "C"

	return f"Grade: {grade}"


score = 88

print(assign_grade(score))
