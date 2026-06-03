import requests

def get_weather():

	url = "https://api.openweathermap.org/data/2.5/weather"

	try:

		response = requests.get(url)

		if response.status_code == 404:
			print("Resource Not Found")
			return

		response.raise_for_status()

		data = response.json()

		temp = data["main"]["temp"]
		condition = data["weather"][0]["description"]

		print(f"Temperature: {temp}")
		print(f"Condition: {condition}")

	except requests.exceptions.ConnectionError:
		print("Network Error")

	except requests.exceptions.RequestException:
		print("API Error")


get_weather()

# Note: Replace the URL with a valid API endpoint and API key before execution.


