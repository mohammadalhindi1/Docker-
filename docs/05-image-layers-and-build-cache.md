# 05 — Image Layers, Cache, and Multi-Stage Builds

## Layers

Docker images are composed of read-only layers. Build instructions such as `RUN`, `COPY`, and `ADD` affect the image filesystem and normally create new layers.

Layers are content-addressed. Images can share identical layers, reducing storage and network transfer.

~~~bash
docker history IMAGE
docker image inspect IMAGE
~~~

## Build cache

Docker can reuse a previous build result when the instruction and its required inputs have not changed. Once a layer changes, later dependent layers usually rebuild.

Cache-friendly order:

~~~dockerfile
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
~~~

Application source changes frequently; dependency manifests usually change less often.

Force a clean build only when needed:

~~~bash
docker build --no-cache -t app:v1 .
~~~

## Multi-stage builds

Multi-stage builds separate compilation tools from the final runtime image.

~~~dockerfile
FROM gcc:14 AS build
WORKDIR /src
COPY . .
RUN make

FROM debian:bookworm-slim
COPY --from=build /src/program /usr/local/bin/program
USER 10001
ENTRYPOINT ["program"]
~~~

The final image contains the binary and required runtime libraries, not the compiler or source tree.

## Image size investigation

~~~bash
docker image ls
docker history app:v1
docker system df
~~~

A smaller image usually downloads faster and has a smaller attack surface, but size is not the only quality metric. Correctness, maintainability, and security matter more than chasing the smallest possible number.
