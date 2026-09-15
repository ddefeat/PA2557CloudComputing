"""Main function for the chess openings microservice.

Routes:
- /
- /health
- /api/openings ; returns an opening
- /api/openings{id} ; returns an opening by id
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from app.db import check_database, close_pool, open_pool, get_openings, get_opening_by_id

@asynccontextmanager
async def lifespan(app: FastAPI):
    open_pool()
    yield
    close_pool()


app = FastAPI(
    title="Opening Service",
    lifespan=lifespan,
)

# routes
@app.get("/")
def root():
    return {"service": "opening-service"}


@app.get("/health")
def health():
      try:
          if not check_database():
              # Tries to connect to db and SELECT
              raise RuntimeError("Database check failed")
      except Exception as error:
          raise HTTPException(
              status_code=503,
              detail="Database unavailable",
          ) from error
  
      return {
          "status": "ok",
          "database": "ok",
      }

@app.get("/api/openings")
def openings():
    # return the full list of openings
    return get_openings()

@app.get("/api/openings{id}")
def openings_by_id(id: int):
    # return a specific opening
    return get_opening_by_id(id)
