# CS415 Ticket API and Ollama Demo

This project contains a modular FastAPI ticket-classification example and a
standalone script that sends a prompt to Ollama.

## Project structure

- `src/main.py`: FastAPI application entry point.
- `src/tickets/schemas.py`: Pydantic request and response models.
- `src/tickets/router.py`: Ticket API endpoint.
- `src/tickets/service.py`: Ticket classification logic.
- `src/ollama.demo.py`: Ollama chat API example.
- `src/core/config.py`: Loads Ollama settings and optional credentials.

## Setup

From the project directory, create and activate a virtual environment, then
install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run the ticket API

```powershell
fastapi dev src/main.py
```

Open <http://127.0.0.1:8000/docs> to try the API.

## Run the Ollama demo

The default configuration uses Local Ollama with the `llama3.2:3b` model. Make
sure Ollama is running and that the model is available, then run:

```powershell
python src/ollama.demo.py
```

For Ollama Cloud, copy the example settings file to `src/core/.env` and set
`OLLAMA_API_URL` to `https://ollama.com/api/chat` and `OLLAMA_API_KEY` to your
key. Set `OLLAMA_MODEL` to a model available to your account. You can also
provide these settings as environment variables; environment variables take
precedence over the `.env` file.

```powershell
Copy-Item src\core\.env.example src\core\.env
```

Never commit `src/core/.env` or put real credentials in source files. The
`.env.example` file contains placeholders only, and `.gitignore` excludes
secret environment files.
