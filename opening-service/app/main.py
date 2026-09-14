from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from app.db import check_database, close_pool, open_pool

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

@app.get("api/openings")
def openings():
    pass

@app.get("api/openings{id}")
def openings_by_id():
    pass