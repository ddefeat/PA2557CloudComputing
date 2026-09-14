CREATE TABLE openings(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    moves TEXT NOT NULL,
    eco VARCHAR(3),
    CONSTRAINT openings_unique_entry UNIQUE (eco, title, moves)
)