from fastapi import FastAPI
# from routes import players
from auth.auth_router import router as auth_router
from database import init_db
from routes.players import router as player_router

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="Poker Tournament Manager", lifespan=lifespan)

# app.include_router(players.router, prefix="/players", tags=["Players"])
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(player_router, prefix="/players", tags=["Players"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Poker Tournament Manager!"}
