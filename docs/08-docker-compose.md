# 08 — Docker Compose

Docker Compose defines a multi-container application in a YAML file, normally `compose.yaml`.

## Core concepts

- **service:** a container configuration
- **image/build:** use an existing image or build one
- **network:** connectivity between services
- **volume:** persistent or mounted data
- **environment:** runtime configuration
- **healthcheck:** application health test
- **dependency:** startup ordering, not automatically application readiness

## Example

~~~yaml
services:
  web:
    build: .
    ports:
      - "8080:8000"
    environment:
      DATABASE_HOST: db
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:17-alpine
    environment:
      POSTGRES_PASSWORD: example
    volumes:
      - db-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 3s
      retries: 10

volumes:
  db-data:
~~~

Compose creates a default network. Services reach each other using service names such as `db`.

## Essential commands

~~~bash
docker compose config
docker compose build
docker compose up
docker compose up -d
docker compose ps
docker compose logs -f
docker compose exec web sh
docker compose stop
docker compose down
docker compose down -v
~~~

Use `docker compose config` to validate and view the resolved configuration.

`down` removes containers and the default network. `down -v` also removes declared volumes and can delete persistent data.

## Compose is not Kubernetes

Compose is excellent for local development, demonstrations, testing, and single-host workloads. It does not provide the full orchestration, scheduling, and self-healing model of Kubernetes.
