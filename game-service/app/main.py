"""Main function for the chess game microservice."""

from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.db import close_pool, open_pool, add_game_to_db, get_game_by_id, get_all_games


class GameRequest(BaseModel):
    moves: str
    p1: str
    p2: str
    result: str
    date: str

@asynccontextmanager
async def lifespan(app: FastAPI):
    open_pool()
    yield
    close_pool()


app = FastAPI(
    title="Game Service",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"service": "game-service"}


@app.get("/health")
def health():
    return {
        "status": "ok",
    }

@app.post("/add_game")
def add_game(game: GameRequest):
    id = add_game_to_db(game.moves, game.p1, game.p2, game.result, game.date)
    if id != -1:
        return {"status": "ok", "game_id": id}
    return {"status": "failed"}


@app.get("/get_game/{id}")
def _get_game(id: int):
    game = get_game_by_id(id)
    if game:
        return game
    return {"status": "not found"}


@app.get("/get_game")
def _get_all_games():
    return get_all_games()
