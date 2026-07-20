# 04 — Dockerfile

A Dockerfile is a text file containing instructions used to build an image.

## Core instructions

| Instruction | Purpose |
|---|---|
| `FROM` | Select the base image |
| `WORKDIR` | Set the working directory |
| `COPY` | Copy files from the build context |
| `RUN` | Execute a command while building |
| `ENV` | Define an environment variable |
| `ARG` | Define a build-time variable |
| `EXPOSE` | Document the application port |
| `USER` | Select the runtime user |
| `ENTRYPOINT` | Define the main executable |
| `CMD` | Define default arguments or command |
| `HEALTHCHECK` | Describe how container health is tested |

## Example

~~~dockerfile
FROM python:3.13-alpine

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

USER 10001
EXPOSE 8000
CMD ["python", "app.py"]
~~~

## Build context

In `docker build -t app:v1 .`, the final dot is the build context. `COPY` can access files inside this directory. Use `.dockerignore` to exclude Git history, secrets, logs, dependencies, and build output.

## CMD versus ENTRYPOINT

- `ENTRYPOINT` defines the executable the container is built to run.
- `CMD` supplies a default command or default arguments.
- Runtime arguments replace `CMD`, but normally append to an exec-form `ENTRYPOINT`.

Prefer the JSON exec form:

~~~dockerfile
CMD ["python", "app.py"]
~~~

It handles signals more correctly than shell form.

## Good practices

- pin deliberate base-image versions
- use small, trusted base images
- copy dependency files before source code to improve cache reuse
- combine related package installation and cleanup
- avoid installing unnecessary tools
- run as a non-root user
- never copy credentials into an image
- use multi-stage builds for compiled applications
