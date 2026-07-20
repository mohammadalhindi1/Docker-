# 02 — Images and Containers

## The shortest correct explanation

An **image** is an immutable template used to create containers.

A **container** is an instance of an image with runtime configuration and a writable layer.

~~~text
One image -> many independent containers
~~~

## Docker images

An image contains the files needed by an application, such as:

- application code
- runtime
- libraries
- default command
- metadata and configuration

Images are built in layers. Each relevant Dockerfile instruction normally creates a layer. Layers are content-addressed and can be reused between images, which saves download time and disk space.

Images downloaded from a registry are transferred as compressed layers. Docker stores and manages the extracted content in its internal data directory. Do not manually edit that directory.

List local images:

~~~bash
docker image ls
~~~

## Containers

A container adds runtime state to an image:

- a writable layer
- a name and ID
- networking
- environment variables
- mounted volumes
- process state
- resource configuration

Changes written only inside a container's writable layer are removed when that container is deleted. Important data should be stored in a volume or bind mount.

List running containers:

~~~bash
docker container ls
~~~

List running and stopped containers:

~~~bash
docker container ls -a
~~~

## run versus start

~~~bash
docker run nginx
~~~

`docker run` creates a **new container** and starts it. Running it five times creates five containers.

~~~bash
docker start web
~~~

`docker start` starts an **existing stopped container**. It does not create a new one.

Equivalent mental model:

~~~text
docker run = docker create + docker start
~~~

## stop, kill, and remove

- `docker stop` asks the main process to terminate gracefully, then forces it after a timeout.
- `docker kill` sends a signal immediately; by default it uses SIGKILL.
- `docker rm` removes a stopped container.
- `docker rm -f` force-removes a running container and should be used carefully.

## A practical lifecycle

~~~bash
docker pull nginx
docker create --name web -p 8080:80 nginx
docker start web
docker ps
docker stop web
docker start web
docker rm -f web
~~~

## Image tags

In `nginx:1.27`:

- `nginx` is the repository name.
- `1.27` is the tag.

If no tag is specified, Docker uses `latest`. The `latest` tag does not mean “the newest safe version”; it is simply a tag. Pin explicit versions for reproducible environments.

## IDs, names, and tags

- Containers have IDs and optional human-friendly names.
- Images are identified internally by content digests.
- Tags are movable labels that point to image versions.
- A digest such as `image@sha256:...` identifies exact content.

## Check your understanding

1. Does `docker run` reuse a stopped container?
2. Can many containers be created from one image?
3. Where should important database data be stored?
4. Does `latest` guarantee a stable release?
5. What is added to an image when a container is created?
