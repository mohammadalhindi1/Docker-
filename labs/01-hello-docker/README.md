# Lab 01 — Hello Docker

## Objective

Run a container, observe its lifecycle, and prove the difference between an image and a container.

## Steps

~~~bash
docker run hello-world
docker image ls
docker ps
docker ps -a
~~~

The container is stopped because its main process printed a message and exited.

Run it again:

~~~bash
docker run hello-world
docker ps -a
~~~

You now have another container. `docker run` created a new one.

## Inspect the result

Copy a container ID from `docker ps -a`:

~~~bash
docker inspect CONTAINER_ID
docker logs CONTAINER_ID
~~~

Look for:

- image reference
- state and exit code
- creation time
- network settings
- the command that ran

## Cleanup

~~~bash
docker container prune
~~~

Read the confirmation carefully before accepting it.

## Challenge

Without running the commands first, predict:

1. Will `docker start CONTAINER_ID` create a third container?
2. Will the started container remain running?
3. Will deleting the container also delete the `hello-world` image?

Write your prediction, test it, and explain the result.
