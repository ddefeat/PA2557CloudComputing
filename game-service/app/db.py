import os
from psycopg_pool import ConnectionPool

# Constants
DATABASE_URL = os.getenv(
      "DATABASE_URL",
      "postgresql://postgres:postgres@chess-db:5432/chess",
)

pool = ConnectionPool(
    DATABASE_URL,
    min_size=1,
    max_size=5,
    open=False,
)


def open_pool() -> None:
    pool.open(wait=True)


def close_pool() -> None:
    pool.close()


def check_database() -> bool:
      with pool.connection() as connection:
          with connection.cursor() as cursor:
              cursor.execute("SELECT 1")
              return cursor.fetchone() == (1,)

def add_game_to_db(moves: str, p1: str, p2: str, result, date):
    with pool.connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO games (white, black, result, moves, played_on) VALUES (%s, %s, %s, %s, %s) RETURNING id",(p1, p2, result, moves, date))
            game_id = cursor.fetchone()[0]
            if not game_id:
                return -1
            return game_id

def get_game_by_id(game_id):
    with pool.connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, white, black, result, moves, played_on, opening_id, created_at FROM games WHERE id = %s", (game_id,))
            return cursor.fetchone()

def get_all_games():
    with pool.connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, white, black, result, moves, played_on, opening_id, created_at FROM games")
            return cursor.fetchall()