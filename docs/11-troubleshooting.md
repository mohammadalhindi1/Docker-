# 11 — Docker Troubleshooting

Use evidence before changing configuration.

## First five commands

~~~bash
docker ps -a
docker logs CONTAINER
docker inspect CONTAINER
docker stats --no-stream
docker system df
~~~

## Container exits immediately

Check:

~~~bash
docker logs CONTAINER
docker inspect -f '{{.State.ExitCode}} {{.State.Error}}' CONTAINER
~~~

Typical causes:

- main process completed
- incorrect command
- missing file or dependency
- invalid environment variable
- permission error
- application bound to the wrong address

## Port does not work

~~~bash
docker ps
docker port CONTAINER
docker logs CONTAINER
~~~

Confirm:

- syntax is `HOST_PORT:CONTAINER_PORT`
- the host port is unused
- the application listens on the internal port
- the application listens on `0.0.0.0`
- firewall rules allow the required access

## Container cannot reach another container

Confirm they share a network:

~~~bash
docker inspect CONTAINER
docker network inspect NETWORK
~~~

Use the container or Compose service name, not `localhost`.

## Build cache appears incorrect

~~~bash
docker build --progress=plain -t app:test .
docker build --no-cache -t app:test .
~~~

Before disabling cache, inspect the Dockerfile order and build context.

## Disk usage grows

~~~bash
docker system df
docker ps -a
docker image ls
docker volume ls
~~~

Remove exact unused resources first. Use prune commands carefully, especially for volumes.

## Permission denied

Check:

- the runtime user
- file ownership inside the image
- mounted host-directory permissions
- executable bits
- Linux security controls such as SELinux/AppArmor where applicable

Avoid solving permission problems by permanently running everything as root.
