import httpx
from chat.config import API_KEY

response = httpx.get(
    "https://api.groq.com/openai/v1/models",
    headers={"Authorization": f"Bearer {API_KEY}"},
    timeout=30,
)
print(response.status_code)
for model in response.json()["data"]:
    print(model["id"])

