# Lab 03 — Build a Custom Image

## Objective

Build an image from source code, run it as a container, change runtime configuration, and inspect the result.

## Understand the Dockerfile

~~~dockerfile
FROM python:3.13-alpine
WORKDIR /app
COPY app.py .
ENV APP_MESSAGE="Hello from Docker"
EXPOSE 8000
CMD ["python", "app.py"]
~~~

- `FROM` selects the base image.
- `WORKDIR` sets the working directory.
- `COPY` adds the application file.
- `ENV` supplies a default environment variable.
- `EXPOSE` documents the container port; it does not publish it.
- `CMD` specifies the default process.

## Build

From this lab directory:

~~~bash
docker build -t docker-learning-app:v1 .
docker image ls
docker history docker-learning-app:v1
~~~

The dot is the build context. Docker can access files in that context unless they are excluded by `.dockerignore`.

## Run

~~~bash
docker run -d --name learning-app -p 8000:8000 docker-learning-app:v1
curl http://localhost:8000
~~~

You can also open `http://localhost:8000` in a browser.

## Configure without rebuilding

~~~bash
docker rm -f learning-app
docker run -d --name learning-app -p 8000:8000 \
  -e APP_MESSAGE="Configured at runtime" \
  docker-learning-app:v1
~~~

The image did not change. The environment variable changed the container's runtime configuration.

## Inspect and debug

~~~bash
docker logs learning-app
docker exec learning-app hostname
docker inspect learning-app
~~~

## Rebuild experiment

Change the default message in the Dockerfile, then build another tag:

~~~bash
docker build -t docker-learning-app:v2 .
docker image ls
~~~

Both versions can exist locally.

## Cleanup

~~~bash
docker rm -f learning-app
docker image rm docker-learning-app:v1 docker-learning-app:v2
~~~

## Challenges

1. Run two containers from the same image on ports 8001 and 8002.
2. Give each container a different `APP_MESSAGE`.
3. Explain which parts belong to the image and which belong to the container.
4. Change `app.py`, rebuild, and identify which build layers are reused.
