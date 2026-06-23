import configparser

class Config:
	pass


class DatabaseConfig(Config):

	def load(self, filename):

		config = configparser.ConfigParser()
		config.read(filename)

		required = ["host", "user", "password", "database"]

		for key in required:
			if key not in config["DATABASE"]:
				raise ValueError(f"Missing {key}")

		return config["DATABASE"]


db = DatabaseConfig()

settings = db.load("db.ini")

for key, value in settings.items():
	print(key, "=", value)

