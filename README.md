# PA2557CloudComputing
This repo contains a microservices-based application for the PA2557 Cloud Computing course. The
application is a simple chess database. You can find openings based on ID, you can also add your
own games to the database.

## Architecture
We have three different services and a database.

1. **Frontend**: The frontend is a simple UI. It allows users to see chess openings and add their
   games. The frontend is also responsible for routing button clicks to the microservices.
2. **Opening Service**: The opening service is a microservice (with fastAPI). This service allows
   users to get different openings from the database. This service owns the openings data. It also
   reads from the database,
3. **Game Service**: The game service is a microservice (with fastAPI). This service allows users to add
    their games to the database. The game service owns all game records. It also reads and writes to
    the database.
4. **Database**: The database is a PostgreSQL database. It contains the chess openings and the games added
   by users. This database is a single instance and is shared among the microservices.

The application is built on a microservices architecture, with each service responsible for a specific aspect of the chess database.

## Scaling
The microservices are horisontally scalable. To scale, edit: `kubernetes.yml`. Under each service
you can enter the amount of replicas.

## Running the app
The application is deployed to a local Kubernetes cluster via minikube. Make sure
[Docker](https://docs.docker.com/get-docker/), [minikube](https://minikube.sigs.k8s.io/docs/start/),
and [kubectl](https://kubernetes.io/docs/tasks/tools/) are installed.

```bash
make up
make open
```

You can also check status:

```bash
make status
```

And clean up:
```bash
make clean
```

## Project structure

```
frontend/           # nginx + static UI, serves the browser client
opening-service/     # FastAPI microservice for chess openings
game-service/        # FastAPI microservice for games
database/            # Postgres schema, seed data, Dockerfile
kubernetes.yml       # Kubernetes manifests (Services, Deployments, StatefulSet)
makefile             # build/push/deploy automation
docker-compose.yml   # local dev setup (not used for the Kubernetes deployment)
```
