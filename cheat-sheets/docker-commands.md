# Docker Command Reference

This file is a practical reference. Learn commands by using the labs, not by memorizing the table.

## Help and system information

| Command | Purpose |
|---|---|
| `docker --version` | Print the CLI version |
| `docker version` | Show client and server versions |
| `docker info` | Show Engine, storage, runtime, and system information |
| `docker help` | Display general CLI help |
| `docker <command> --help` | Display help for one command |

## Images

| Command | Purpose |
|---|---|
| `docker pull nginx:1.27` | Download an image |
| `docker image ls` | List local images |
| `docker image inspect nginx` | Show detailed image metadata |
| `docker history nginx` | Show image layer history |
| `docker image rm nginx` | Remove an unused image |
| `docker image prune` | Remove dangling images |
| `docker tag app:local user/app:v1` | Add another name/tag |
| `docker push user/app:v1` | Upload an image |

## Container lifecycle

| Command | Purpose |
|---|---|
| `docker run IMAGE` | Create and start a new container |
| `docker create IMAGE` | Create without starting |
| `docker start NAME` | Start an existing container |
| `docker stop NAME` | Gracefully stop a container |
| `docker restart NAME` | Stop and start a container |
| `docker kill NAME` | Immediately send a signal |
| `docker rm NAME` | Remove a stopped container |
| `docker rm -f NAME` | Force-remove a running container |

## Common run options

| Option | Meaning |
|---|---|
| `--name web` | Assign a container name |
| `-d` | Run in detached mode |
| `-it` | Allocate an interactive terminal |
| `--rm` | Automatically remove after exit |
| `-p 8080:80` | Map host port 8080 to container port 80 |
| `-e KEY=value` | Set an environment variable |
| `--env-file .env` | Load environment variables from a file |
| `-v volume:/path` | Mount a volume |
| `--mount ...` | Use the explicit mount syntax |
| `--network app-net` | Connect to a Docker network |
| `--restart unless-stopped` | Configure a restart policy |
| `--cpus 1` | Limit available CPU |
| `--memory 512m` | Limit available memory |

Example:

~~~bash
docker run -d --name web -p 8080:80 --restart unless-stopped nginx:1.27
~~~

Port syntax is always:

~~~text
HOST_PORT:CONTAINER_PORT
~~~

## Inspection and debugging

| Command | Purpose |
|---|---|
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker logs NAME` | Read container output |
| `docker logs -f NAME` | Follow container output |
| `docker exec -it NAME sh` | Start a shell in a running container |
| `docker inspect NAME` | Display low-level JSON metadata |
| `docker stats` | Show live resource usage |
| `docker top NAME` | Show processes running in a container |
| `docker port NAME` | Show published port mappings |
| `docker cp NAME:/path ./path` | Copy files from a container |

`docker exec` does not create a new container. It starts another process inside an existing running container.

## Building images

| Command | Purpose |
|---|---|
| `docker build -t my-app:v1 .` | Build using the current directory as context |
| `docker build --no-cache -t my-app:v1 .` | Build without layer cache |
| `docker builder prune` | Remove unused build cache |

The final dot in `docker build ... .` is the build context, not decorative syntax.

## Volumes

~~~bash
docker volume create app-data
docker volume ls
docker volume inspect app-data
docker volume rm app-data
docker volume prune
~~~

## Networks

~~~bash
docker network create app-net
docker network ls
docker network inspect app-net
docker network connect app-net web
docker network disconnect app-net web
docker network rm app-net
~~~

## Cleanup

~~~bash
docker container prune
docker image prune
docker volume prune
docker network prune
docker system df
docker system prune
~~~

Prune commands delete unused resources. Review the target and confirmation prompt before continuing. Volumes are treated carefully because they may contain important data.

## Docker Compose

~~~bash
docker compose up
docker compose up -d
docker compose ps
docker compose logs -f
docker compose build
docker compose down
docker compose down -v
~~~

`docker compose down -v` also removes declared volumes and can delete persistent data.
