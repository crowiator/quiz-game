import requests

# Parameters for API
parameters = {
  "amount": 30,
  "difficulty": "easy",
  "type": "boolean"
}
# Getting data from API
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
# Data
question_data = response.json()["results"]
