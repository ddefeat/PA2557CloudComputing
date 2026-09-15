import os
from psycopg_pool import ConnectionPool

# Constants
DATABASE_URL = os.getenv(
      "DATABASE_URL",
      "postgresql://chessuser:chesspassword@localhost:5433/chessdb",
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
          
def get_openings() -> list[tuple]:
    """Return all openings as a list of tuples"""
    with pool.connection() as connection:
              with connection.cursor() as cursor:
                  cursor.execute("SELECT id, title, pgn, moves FROM openings")
                  rows = cursor.fetchall()
                  return rows

def get_opening_by_id(id:int) -> list[tuple]:
    """Return a specfic opening by id"""
    with pool.connection() as connection:
                  with connection.cursor() as cursor:
                      cursor.execute("SELECT id, title, pgn, moves FROM openings WHERE id = %s",(id,))
                      rows = cursor.fetchall()
                      return rows


# local testing
open_pool()
print(get_opening_by_id("1"))
close_pool