from fastapi import FastAPI

from app.routers import tickets

app=FastAPI(title="supportDesk")

app.include_router(tickets.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}