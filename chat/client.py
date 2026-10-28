import httpx
from config import API_KEY, API_URL, MODEL_NAME
from errors import APIError


def send_message(messages) -> dict:
    try:
        response = httpx.post(
            API_URL, 
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}"
            },
            json={
                "model": MODEL_NAME, 
                "messages":  [{
                        "role": "user",
                        "content": messages
                    }],
            },
            timeout=30,
        )
    except httpx.TimeoutException as error:
        raise APIError("The request time out. Try again") from error 
    except httpx.ConnectError as error:
        raise APIError("Cannot reach the server. Check your internet connection") from error 

    # print(response.status_code)
    if response.status_code != 200:
        return response.status_code

    return {
        "id": response.json()["id"],
        "object": response.json()["object"],
        "created_at": response.json()["created"],
        "model": response.json()["model"],
        "assistant": [data["message"]["role"] for data in response.json()["choices"]],
        "content": [data["message"]["content"] for data in response.json()["choices"]],
    }

answer = send_message("Why is the color of atmosphere blue?")
print(answer)
