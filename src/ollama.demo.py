import requests

from core.config import OLLAMA_API_KEY, OLLAMA_API_URL, OLLAMA_MODEL


def ask_model(prompt: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "stream": False,
    }

    headers = {}
    if OLLAMA_API_KEY:
        headers["Authorization"] = f"Bearer {OLLAMA_API_KEY}"

    response = requests.post(
        OLLAMA_API_URL,
        json=payload,
        headers=headers,
    )

    response.raise_for_status()

    data = response.json()

    generated_text = data["message"]["content"]

    return generated_text


def main() -> None:
    prompt = "Explain what FastAPI is in one short paragraph."

    response = ask_model(prompt)

    print("Prompt:")
    print(prompt)

    print("\nModel Response:")
    print(response)


if __name__ == "__main__":
    main()