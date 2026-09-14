CREATE TABLE openings (
    id     SERIAL PRIMARY KEY,
    eco    CHAR(3)      NOT NULL,          -- "C60"
    title  VARCHAR(255) NOT NULL,          -- "Ruy Lopez: Morphy Defense"
    pgn    TEXT         NOT NULL,          -- "1. e4 e5 2. Nf3 Nc6 3. Bb5 a6"
    moves  TEXT         NOT NULL,          -- normalised SAN: "e4 e5 Nf3 Nc6 Bb5 a6"
    ply    INTEGER      NOT NULL,          -- number of half-moves, = word count of moves
    CONSTRAINT openings_unique_entry UNIQUE (eco, title, pgn)
);
CREATE INDEX openings_moves_idx ON openings (moves);
CREATE INDEX openings_title_idx ON openings (lower(title));

CREATE TABLE games (
    id         SERIAL PRIMARY KEY,
    white      VARCHAR(100) NOT NULL,
    black      VARCHAR(100) NOT NULL,
    result     VARCHAR(7)   NOT NULL CHECK (result IN ('1-0', '0-1', '1/2-1/2', '*')),
    played_on  DATE,
    moves      TEXT         NOT NULL,      -- normalised SAN
    opening_id INTEGER,                    -- no FK, see "Data ownership"
    created_at TIMESTAMPTZ  NOT NULL DEFAULT now()
);