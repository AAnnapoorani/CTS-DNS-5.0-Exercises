# Exercise 36

def common_skills(set1, set2):

	if not isinstance(set1, set) or not isinstance(set2, set):
		return "Invalid Input"

	return set1 & set2


skills1 = {"Python", "SQL", "Java"}

skills2 = {"Python", "C++", "SQL"}

print("Common Skills:", common_skills(skills1, skills2))
