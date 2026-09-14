"""Script to populate the database with openings data."""

# Imports
import csv
from pathlib import Path
import psycopg

# Set up paths
PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "database" / "data"

# Define DB URL
DATABASE_URL = ("postgresql://chessuser:chesspassword@localhost:5000/chessdb")

# These are the files we have
FILES = ["a", "b", "c", "d", "e"]

for i in FILES:
    with open(f"database//data/{i}.tsv", "r") as f:
        # open each file one by one