# Project — Two-Tier Containerized Web Application

This project demonstrates a small but complete multi-container architecture:

~~~text
Browser -> published Nginx frontend -> private backend network -> Python API
~~~

The backend is not published directly to the host. Nginx reaches it by the Compose service name `backend`.

## Run

~~~bash
docker compose config
docker compose up -d --build
docker compose ps
~~~

Open `http://localhost:8080` and select **Call backend**.

## Inspect

~~~bash
docker compose logs -f
docker compose exec frontend wget -q -O - http://backend:8000/health
docker network ls
~~~

Concepts demonstrated:

- custom image build
- two services
- reverse proxy
- service-name DNS
- health-based dependency
- separate frontend and internal backend networks
- runtime environment configuration
- non-root backend
- read-only backend filesystem
- temporary writable filesystem
- no-new-privileges security option

## Stop

~~~bash
docker compose down
~~~

## Experiments

1. Scale the backend: `docker compose up -d --scale backend=3`.
2. Run repeated API requests and observe backend hostnames.
3. Remove the shared backend network and explain the failure.
4. Publish the backend port temporarily and compare exposure.
5. Change `APP_MESSAGE` without rebuilding the image.
