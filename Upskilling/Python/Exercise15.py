# Exercise 15

def login(user, pwd):

	if user.strip() == "":
		return "Username cannot be empty"

	if pwd.strip() == "":
		return "Password cannot be empty"

	if user == "admin":
		if pwd == "pass123":
			return "Login Successful"
		else:
			return "Incorrect Password"
	else:
		return "Invalid User"


user = "admin"
pwd = "pass123"

print(login(user, pwd))

