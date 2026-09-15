FROM postgres:17

COPY schema.sql /docker-entrypoint-initdb.d/01-schema.sql
COPY seed_db.sh /docker-entrypoint-initdb.d/02-seed.sh
COPY data /docker-entrypoint-initdb.d/data

RUN chmod +x /docker-entrypoint-initdb.d/02-seed.sh