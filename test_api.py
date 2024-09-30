import requests

url = 'http://127.0.0.1:5000/analyze'  # Change this line
data = {'text': 'I love using this API!'}  # Example input text

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Failed to get response, Status Code:", response.status_code)
