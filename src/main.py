from fastapi import FastAPI
from routes import players

app = FastAPI(title="Poker Tournament Manager")

app.include_router(players.router, prefix="/players", tags=["Players"])
# app.include_router(tournaments.router, prefix="/tournaments", tags=["Tournaments"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Poker Tournament Manager!"}
