# Lab 06 — Docker Compose

Start the application from this directory:

~~~bash
docker compose config
docker compose up -d
docker compose ps
~~~

Open `http://localhost:8080`.

Follow logs:

~~~bash
docker compose logs -f
~~~

Change `site/index.html` and refresh the browser. The bind mount makes the change visible without rebuilding an image.

Inspect the resolved service:

~~~bash
docker compose images
docker compose top
~~~

Stop and remove the Compose resources:

~~~bash
docker compose down
~~~

Challenges:

1. Change the published host port.
2. Add a second service on the Compose network.
3. Find the generated network with `docker network ls`.
4. Explain why the site directory is mounted with `:ro`.
