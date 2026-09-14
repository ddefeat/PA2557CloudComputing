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