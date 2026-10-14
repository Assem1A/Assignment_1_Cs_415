from fastapi import FastAPI

from tickets.router import router as tickets_router

app = FastAPI(
    title="CS415 Ticket API",
    description="Lab 2 example: Pydantic + FastAPI",
    version="1.0.0",
)

app.include_router(tickets_router)


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "CS415 Ticket API is running"}