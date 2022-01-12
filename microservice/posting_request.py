import requests

param = {"1": "Kafka", "2": "RabbitMQ"}
url = f"http://127.0.0.1:5000/data/DBS"

# print(requests.post(url, param).json())
print(requests.delete(url).json())
