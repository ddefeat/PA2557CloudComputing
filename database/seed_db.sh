#!/usr/bin/env bash
set -e

PSQL=(
    psql
    --username "$POSTGRES_USER"
    --dbname "$POSTGRES_DB"
    --no-password
    --set ON_ERROR_STOP=1
)
  
DATA_DIR="/docker-entrypoint-initdb.d/data"

"${PSQL[@]}" <<'SQL'
DROP TABLE IF EXISTS staging_openings;

CREATE TABLE staging_openings (
    eco  TEXT NOT NULL,
    name TEXT NOT NULL,
    pgn  TEXT NOT NULL
);
SQL

for file in "$DATA_DIR"/*.tsv; do
    echo "Import: $file"

    "${PSQL[@]}" -c \
      "\copy staging_openings (eco, name, pgn) FROM '$file' WITH (FORMAT csv, HEADER true, DELIMITER E'\t')"
done

"${PSQL[@]}" <<'SQL'
WITH normalized AS (
    SELECT
        eco,
        name AS title,
        pgn,
        TRIM(
            REGEXP_REPLACE(
                REGEXP_REPLACE(
                    pgn,
                    '[0-9]+\.[[:space:]]*',
                    '',
                    'g'
                ),
                '[[:space:]]+',
                ' ',
                'g'
            )
        ) AS moves
    FROM staging_openings
)
INSERT INTO openings (
    eco,
    title,
    pgn,
    moves,
    ply
)
SELECT
    eco,
    title,
    pgn,
    moves,
    CARDINALITY(string_to_array(moves, ' '))
FROM normalized
WHERE moves <> ''
ON CONFLICT (eco, title, pgn) DO NOTHING;

DROP TABLE staging_openings;
SQL