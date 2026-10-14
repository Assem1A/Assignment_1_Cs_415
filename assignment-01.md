# Assignment 01: Modular Programming & Ollama API

**Deadline:** Before the next lab session.

## Part 1: Code Modularization

### Objective

Refactor the FastAPI application from Section 02 into a modular Python project.

### Requirements

1. Split `sec-02/main.py` into separate Python modules.
2. Give each module a clear responsibility.
3. Separate Pydantic models, API routes, and application logic.
4. Use Python imports to connect the modules.
5. Keep `main.py` as the application entry point.
6. Preserve all existing functionality.
7. Make sure all API endpoints still work.

You may choose your own project structure.

### Verification

Run the FastAPI application and open <http://127.0.0.1:8000/docs> to verify
that all endpoints work:

```bash
fastapi dev src/main.py
```

## Part 2: Ollama API Integration

### Objective

Build a Python application that communicates with a large language model using
the Ollama API.

Use either a local Ollama model or Ollama Cloud. The application must send a
prompt through an API, receive the model response, extract the generated text,
and display it. Model interaction must happen programmatically; direct
terminal interaction with a model does not meet the requirement.

Cloud requests require an API key. Never include API keys directly in source
code or upload them to GitHub.

### Submission

Submit the refactored FastAPI code, the Python script demonstrating Ollama API
communication, and a README explaining the module organization, selected
model, local or cloud setup, and how to run the code.

### References

- <https://ollama.com>
- <https://docs.ollama.com/cloud>
- <https://docs.ollama.com/api>
